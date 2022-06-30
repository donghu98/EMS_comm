# Custom Signal & Slot

import sys
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyApp(QWidget): # QMainWindow로 변경 요망
    closeSignal = pyqtSignal() #커스텀 시그널

    def __init__(self):

    def initUI(self):
        self.setWindowTitle('Close Demo')
        self.resize(300,300)

        self.btnClose = QPushButton('close',self)
        self.btnClose.clikcked.connect(self.btnCloseClicked)
        self.closeSignal.connect(self.onClose)

        self.show()

    def btnCloseClicked(self):
        self.closeSignal()

    def onClose(self):
        self.close()

if __name__ == '__main__':