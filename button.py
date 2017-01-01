import sys
from PyQt5.QtGui import *

class First_gui(QWidget):
    def __init__(self):
        super().__init__(self, windowTitle="我的第一個GUI")
        self.outputArea = QTextBrowser(self)
        self.startButton = QPushButton(self.trUtf8("點我開始"), self)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.outputArea)
        self.layout().addWidget(self.startButton)

        self.startButton.clicked.connect(self.start)

    def start(self):
        self.outputArea.append(self.trUtf8("歡迎使用我的第一個GUI！"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    first_gui = First_gui()
    first_gui.show()
    sys.exit(app.exec_())
