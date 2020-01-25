#led blink
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
for loop in range (1,500000,1):
    GPIO.output(21,1)
    time.sleep(1)
    GPIO.output(21,0)
    time.sleep(1)
    print('siayaan')
GPIO.cleanup()
