import sys
from PyQt5 import uic   # 유저 인터페이스
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 클래스 OOP
class qTemplate(QWidget):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./pyqt02/basic01.ui', self)
        self.initUI()
    
    def initUI(self) -> None:
        self.addControls()
        self.show()

    def addControls(self) -> None:
        self.btn1.clicked.connect(self.btn1_clicked)
    
    def btn1_clicked(self):
        self.label.setText(f'메시지 : btn1 버튼 클릭')
        QMessageBox.critical(self, 'signal', 'btn1_clicked')

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()