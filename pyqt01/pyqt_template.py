import sys
from PyQt5.QtWidgets import QApplication, QWidget

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자(원래부터 class에 속해있는 것들) : 기본적으로 리턴 값이 없다 / -> None : 리턴하는게 없다는 뜻
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    def initUI(self) -> None:
        self.setGeometry(300, 100, 640, 400)  # 그 위치에 이런 크기의 윈도우를 만들겠다
        self.setWindowTitle('QTemplate!')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()