#PyQt5 템플릿 소스

import sys
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyApp(QWidget): # QMainWindow로 변경 요망

    def __init__(self):
        super(MyApp, self).__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('./windows/UI/navernews.ui', self) #UI 파일변경 요
        self.show