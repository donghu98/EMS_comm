## LED Control UI
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import RPi.GPIO as GPIO
import time

BUTTON = 3
RED = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN)

class MyApp(QWidget) :
    def __init__(self) :
        super().__init__()
        self.initUI()

    def initUI(self) :
        self.setWindowTitle('RPi LED Control')
        # 윈도우 기본 설정
        self.setGeometry(100, 100, 300, 350)

        self.dial = QDial(self)
        self.dial.setRange(0,13)
        self.label.setFont(QFont('Arial', 15))
        self.label.setText("MOTOR CONTROL")
        self.label.setAlignment(Qt.AlignCenter) # 라벨 정중앙
     

        # 시그널 정의
        self.dial.valueChanged.connect(self.Dial_Changed)

        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.dial)
        self.vbox.addWidget(self.label)

        self.show()

    def Dial_Changed(self):
        self.label.setText(str(self, self.dial.value()))


if __name__ == '__main__' :
    app = QApplication(sys.argv)
    wnd = MyApp()

    app.exec_()        