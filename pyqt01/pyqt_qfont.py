import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

class qTemplate(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    # 화면 정의를 위해서 만든 사용자 함수
    def initUI(self) -> None:
        self.setGeometry(300, 100, 640, 400)
        self.setWindowTitle('QTemplate!')
        self.text = 'What a Wonderful World!'
        self.show()

    def paintEvent(self, event) -> None:
        paint = QPainter()
        paint.begin(self)
        # 그리는 함수 추가
        self.drawText(event, paint)
        paint.end()

    # 텍스트를 그리기 위한 사용자 함수
    def drawText(self, event, paint):
        paint.setPen(QColor(50, 50, 50))
        paint.setFont(QFont('NanumSquare', 20))
        paint.drawText(105, 100, 'HELL WORLD~')   # ← 이거는 내장 함수
        paint.setPen(QColor(0, 250, 10))   # 글자색
        paint.setFont(QFont('NanumGothic', 10))   # 글자폰트
        paint.drawText(event.rect(), Qt.AlignCenter, self.text)   # event.rect() : 정중앙에 들어옴

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()