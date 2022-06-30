#thread 없이 동작

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super(MyApp, self).__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('./windows/UI/threadtask.ui', self) #UI 파일변경 요
        self.btnStart.clicked.connect(self.btnStartClicked)
        self.show()

    def btnStartClicked(self):
        self.pgbTask.setRange(0,99999)
        for i in range(0, 100000):
            print(f'출력 > {i}')
            self.pgbTask.setValue(i)
            self.txbLog.append(f'출력 > {i}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyApp()
    app.exec_()
