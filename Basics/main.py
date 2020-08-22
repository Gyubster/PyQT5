import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class Cal(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))
        # self.setToolTip('This is <b>quit button</b> widget')

        btn = QPushButton('Quit', self)
        btn.setToolTip('This is <b>quit button</b> widget')
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.statusBar().showMessage('Ready')
        self.setWindowTitle('Caculator')
        self.setWindowIcon(QIcon('Cal.jpg'))
        self.setGeometry(300, 300, 300, 200)
        self.show()

# self.move는 창을띄었을때 위치
# self.resize는 창 크기 조절
# 위 두개를 없애면 정중앙에 나타남.
# setGeometry 함수로 창의위치와 크기 한번에 조절가능.(move + resize)한 것임.

# self.로 setToolTip을 쓰는경우에는 전부다 툴팁이나오는..?

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = Cal()
   sys.exit(app.exec_())
