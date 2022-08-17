from os import link
import sys
from turtle import title
from PyQt5 import uic   # 유저 인터페이스
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from urllib.parse import quote
import urllib.request
import json
import webbrowser



# 클래스 OOP
class qTemplate(QWidget):
    def __init__(self) -> None:   # 생성자
        super().__init__()
        uic.loadUi('./navernews.ui', self)
        self.initUI()
    
    def initUI(self) -> None:
        self.addControls()
        self.show()

    def addControls(self) -> None:   # 위젯 정의, 이벤트(시그널) 처리
        self.btnSearch.clicked.connect(self.btnSearchClicked)
        self.txtSearch.returnPressed.connect(self.btnSearchClicked)   # 엔터 쳤을때도 검색할 수 있도록 - 엔터를 눌렀을 때 동작하는 것
        self.tblResult.itemSelectionChanged.connect(self.tblResultSelected)

    def btnSearchClicked(self) -> None:   # 슬롯(이벤트 핸들러)
        jsonResult = []
        totalResult = []
        keyword = 'news'
        search_word = self.txtSearch.text()
        display_count = 100

        # QMessageBox.information(self, '결과', search_word)
        jsonResult = self.getNaverSearch(keyword, search_word, 1, display_count)
        # print(jsonResult)
        
        for post in jsonResult['items']:
            totalResult.append(self.getPostData(post))
        
        # print(totalResult)
        self.makeTable(totalResult)
        return

    def tblResultSelected(self) -> None:
        selected = self.tblResult.currentRow()   # 현재 선택된 열의 인덱스
        link = self.tblResult.item(selected, 1).text()
        webbrowser.open(link)

    def makeTable(self, result):   # 테이블위젯 설정(set)
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblResult.setColumnCount(2)
        self.tblResult.setRowCount(len(result))   # display count에 따라서 변경, 현재는 50
        self.tblResult.setHorizontalHeaderLabels(['기사제목', '뉴스링크'])
        self.tblResult.setColumnWidth(0, 350)
        self.tblResult.setColumnWidth(1, 100)
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers)   # read-only

        i = 0
        for item in result:
            title = self.strip_tag(item[0]['title'])
            link = item[0]['originallink']
            self.tblResult.setItem(i, 0, QTableWidgetItem(title))
            self.tblResult.setItem(i, 1, QTableWidgetItem(link))
            i += 1

    def strip_tag(self, title):   # html 태그 없애는 함수
        ret = title.replace('&lt;', '<')
        ret = ret.replace('&gt;', '>')
        ret = ret.replace('&quot;', '"')
        ret = ret.replace('&apos;', "'")    # 홑따옴표 없애주는거니까 겉에 구분되도록 쌍따옴표로 표기
        ret = ret.replace('&amp;', '&')
        ret = ret.replace('<b>', '')
        ret = ret.replace('</b>', '')
        return ret

    def getPostData(self, post):
        temp = []
        title = post['title']
        description = post['description']
        originallink = post['originallink']
        link = post['link']
        pubDate = post['pubDate']

        temp.append({'title':title, 'description':description, 'originallink':originallink, 'link':link})

        return temp

    # 네이버 API 크롤링을 위한 함수
    def getNaverSearch(self, keyword, search, start, display):
        url = f'https://openapi.naver.com/v1/search/{keyword}.json' \
              f'?query={quote(search)}&start={start}&display={display}'
        print(url)
        req = urllib.request.Request(url)

        # 네이버 인증 추가
        req.add_header('X-Naver-Client-Id', 'jpj18gb48p4fCPR8W1jt')
        req.add_header('X-Naver-Client-Secret', 'yD5omERM_d')

        res = urllib.request.urlopen(req)
        if res.getcode() == 200:
            print('URL request succeed')
        else:
            print('URL request failed')

        ret = res.read().decode('utf-8')
        if ret == None:
            return None
        else:
            return json.loads(ret)

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()