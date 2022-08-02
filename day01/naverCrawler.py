import os
import sys
import urllib.request
import datetime
import time
import json

client_id = 'jpj18gb48p4fCPR8W1jt'
client_secret = 'yD5omERM_d'


# url 접속 요청 후 응답 리턴 함수
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header('X-Naver-Client-Id', client_id)
    req.add_header('X-Naver-Client-Secret', client_secret)

    try:
        res = urllib.request.urlopen(req)  #200 OK / 40X error(예: error404) / 50X server error
        if res.getcode() == 200:
            print(f'[{datetime.datetime.now()}] Url Request success')  #책에 있는 방식 대신 이걸로 하면 됨
            return res.read().decode('utf-8')

    except Exception as e:
        print(e)
        print(f'[{datetime.datetime.now()}] Error for URL : {url}')
        return None


# 핵심 함수, 네이버 API 검색
def getNaverSearch(node, srcText, start, display):
    base = 'https://openapi.naver.com/v1/search'
    node = f'/{node}.json'
    text = urllib.parse.quote(srcText)  #url 주소에 맞춰서 파싱 - 아스키코드 형식이 아닌 글자를 URL 인코딩 시켜줍니다
    params = f'?query={text}&start={start}&display={display}'

    url = base + node + params
    resDecode = getRequestUrl(url)

    if resDecode == None:
        return None
    else:
        return json.loads(resDecode)


def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    originallink = post['originallink']
    link = post['link']

    #날짜 형식이 약간 다르므로 변경해준다
    pubDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    pubDate = pubDate.strftime('%Y-%m-%d %H:%M:%S')  #2022-08-02 15:56:34 모양으로 만들어주기

    jsonResult.append({'cnt':cnt, 'title':title, 'description':description,
                       'originallink':originallink, 'link':link, 'pubDate':pubDate})


# 실행 최초 함수
def main():
    node = 'news'
    srcText = input('검색어를 입력하세요 : ')
    cnt = 0
    jsonResult = []

    jsonRes = getNaverSearch(node, srcText, 1, 50)
    # print(jsonRes)
    total = jsonRes['total']  #검색된 뉴스 갯수

    while ((jsonRes != None) and (jsonRes['display'] != 0)):
        for post in jsonRes['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt)

        start = jsonRes['start'] + jsonRes['display']  # 1+50
        jsonRes = getNaverSearch(node, srcText, start, 50)

    print(f'전체 검색 : {total}건')

    # FILE OUTPUT
    with open(f'./{srcText}_naver_{node}.json', mode='w', encoding='utf-8') as outfile:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(jsonFile)

    print(f'가져온 데이터 : {cnt} 건')
    print(f'{srcText}_naver_{node}.json SAVED')



if __name__ == '__main__':
    main()