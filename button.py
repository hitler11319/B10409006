import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class First_gui(QWidget):
    def __init__(self, parent=None):
        super(First_gui, self).__init__(parent)
        self.setWindowTitle('my first gui')
        self.outputArea = QTextBrowser(self)
        self.startButton = QPushButton("點我開始")
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.outputArea)
        self.layout().addWidget(self.startButton)

        self.startButton.clicked.connect(self.start)

    def start(self):
        self.outputArea.append("歡迎使用我的第一個GUI！")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    first_gui = First_gui()
    first_gui.show()
    sys.exit(app.exec_())
