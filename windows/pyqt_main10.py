import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self) :
        self.setWindowTitle('RPi LED Control')
        #윈도우 기본설정
        self.setGeometry(100, 100, 300, 350)

        self.label.setFont(QFont('Arial', 15))
        self.label.setText('LED Control')
        self.label.setAlignment(Qt.Alignment)

        self.btnOn = QPushButton('LED ON', self )
        self.btnOff = QPushButton('LED OFF', self)
       

        #시그널
        self.btnOn.clicked.connect(self.btnOn_clicked)
        self.btnOn.clicked.connect(self.btnOff_clicked)
    
        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.label)

        self.hbox = QHBoxLayout(self)
        self.hbox.addChildWidget(self.btnOn)
        self.hbox.addChildWidget(self.btnOff)
        
        self.vbox.addLayout(self.hbox)

        self.show()

    def btnOn_clicked(self):
        self.label.setText("LED ON!")

    def btnOff_clicked(self):
        self.label.setText("LED OFF!")
    

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    wnd = MyApp()
    app.exec_()       