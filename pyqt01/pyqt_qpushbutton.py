import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자(원래부터 class에 속해있는 것들) : 기본적으로 리턴 값이 없다 / -> None : 리턴하는게 없다는 뜻
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    def initUI(self) -> None:
        self.addControls()
        self.setGeometry(300, 100, 640, 400)  # 그 위치에 이런 크기의 윈도우를 만들겠다
        self.setWindowTitle('QPushbutton 예제')
        self.show()

    def addControls(self) -> None:   # self는 넣어도 되고 빼도 됨 - 넣는게 더 정확
        self.label = QLabel('메시지 :', self)
        self.label.setGeometry(10, 10, 600, 40)
        self.btn1 = QPushButton('클릭', self)
        self.btn1.setGeometry(510, 350, 120, 40)
        self.btn1.clicked.connect(self.btn1_clicked)   # 시그널 연결

    # event = signal (python)
    def btn1_clicked(self):
        # QMessageBox.information(self, 'signal', 'btn1_clicked')   # 일반정보창
        # QMessageBox.warning(self, 'signal', 'btn1_clicked')   # 경고창
        self.label.setText(f'메시지 : btn1 버튼 클릭')
        QMessageBox.critical(self, 'signal', 'btn1_clicked')   # 에러창

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()