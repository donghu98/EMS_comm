# EMS 대시보드앱
from nturl2path import url2pathname
import sys
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import dashboard_rc #리소스 py코드 추가 
import requests
import json
import paho.mqtt.client as mqtt #mqtt subscribe를 위해서 추가 
import time

broker_url = '127.0.0.1'

class Worker(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.host = broker_url
        self.port = 1883
        self.client = mqtt.Client(client_id = 'Dashboard')

    def onConnect(self, mqtt, obj, flags, rc):
        print(f'connected with result code > {rc}')

    def onMessage(self, mqtt, obj, msg):
        rcv_msg = str(msg.payload.decode('utf-8'))
        print(f'{msg.topic} / {rcv_msg}')

        time.sleep(2.0)

    def mqttloop(self):
        self.client.loop()
        print('MQTT client loop')

    def run(self): #Thread에서는 run() 필수 
    self.client.on_connect = self.onConnect
    self.client.on_message = self.onMessage
    self.client.connect(self.host, self.port)
    self.client.subscribe(topic='ems/rasp/data/')
    self.client.loop_forever()




class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.initUI()
        self.showTime()
        self.showWeather()
        self.initThread()

    def initThread(self):
        self.myThread = Worker(self)
        self.myThread.start()

    def showWeather(self):
        url = 'https://api.openweathermap.org/data/2.5/weather?q=seoul&appid=0a9f6aeb854114111d15d53b5a76469d&lang=kr&units=metric'

        result = requests.get(url)
        result = json.loads(result.text)
        weather = result['weather'][0]['main'].lower()
        print(weather)
        self.weatherFrame.setStyleSheet(
            (
                f'border : none; '
                 'background-image: url(:/{weather});'
                 'background-repeat: none;'
            )
        )

    
    

    def initUI(self):
        uic.loadUi('./windows/UI/dashboard.ui', self)
        self.setWindowIcon(QIcon('iot_64.png'))

        self.show()
    
    def showTime(self):
        today = QDateTime.currentDateTime()
        currDate = today.date()
        currTime = today.time()
        currDay = today.toString('dddd')
        

        self.lblDate.setText(currDate.toString('yyyy-MM-dd'))
        self.lblDay.setText(currDay)
        self.lblTime.setText(currTime.toString('HH:mm'))
        if today.time().hour() > 10 and today.time().hour() < 12:
            self.lblGreeting.setText('Good Morning')
        elif today.time().hour() >= 12 and today.time().hour() < 18:
            self.lblGreeting.setText('Good Afternone')
            
             self.lblGreeting.setText('Good Morning')
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyApp()
    app.exec_()