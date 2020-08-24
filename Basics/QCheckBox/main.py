import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import*

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox('Title', self)
        cb.toggle()
        cb.stateChanged.connect(self.ChangeTitle)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(cb)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(2)

        self.setLayout(vbox)
        # 이걸 쳐야 적용.

        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def ChangeTitle(self, state):
        if state == Qt.checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('Changed')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())