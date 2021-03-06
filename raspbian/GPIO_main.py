## submoter test
import RPi.GPIO as GPIO
import time 

SERVO = 12

GPIO.setmode(GPIO.BOARD) #
GPIO.setup(SERVO, GPIO.OUT)

pwm = GPIO.PWM(SERVO, 50) #50Hz
pwm.start(50.0)  #0.6ms

time.sleep(10.0)
pwm.ChangeDutyCycle(0.0)

pwm.stop()
GPIO.cleanup()
