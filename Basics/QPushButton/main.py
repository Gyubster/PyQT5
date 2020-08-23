import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel('Hello. World!', self)
        label.setAlignment(Qt.AlignCenter)
        font = label.font()
        font.setPointSize(20)
        label.setFont(font)

        btn1 = QPushButton('&Ok', self)
        btn1.setCheckable(True)
        btn1.toggle()

        btn2 = QPushButton(self)
        btn2.setText('&Cancel')
        btn2.clicked.connect(QCoreApplication.instance().quit)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(label)
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
