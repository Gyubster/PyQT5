import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.move(60, 40)

        # 라벨 추가

        qle = QLineEdit(self)
        qle.move(60, 100)
        # qle.textChanged[str].connect(self.onChanged)
        qle.returnPressed.connect(self.onChanged)
        # 왜 안되는지 모르겠음

        # QLineEdit 추가

        self.setWindowTitle('QLineEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())