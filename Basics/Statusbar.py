import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        btn = QPushButton('Change', self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.btn1_clicked)

        self.setWindowTitle('Statusbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def btn1_clicked(self):
        QMessageBox.about(self, 'Message', 'Changed')
        self.statusBar().showMessage('Finished')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())