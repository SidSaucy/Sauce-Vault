#led blink
import time,random
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
sid=[21,16,20,17,19,6 ]
GPIO.setup(sid,GPIO.OUT)
GPIO.setup(12,GPIO.IN)

# A green - 21
# A yellow - 16
# A red - 20

# B green - 6
# B yellow - 17
# B red - 19

def series():
    for i in sid:
       
        GPIO.output(i,1)
        time.sleep(.2)
        GPIO.output(i,0)
        time.sleep(.2)

def rand():
    random.shuffle(sid)
    for i in sid:
       
        GPIO.output(i,1)
        time.sleep(.2)
        GPIO.output(i,0)
        time.sleep(.2)
    sid.reverse()
    for i in sid:
       
        GPIO.output(i,1)
        time.sleep(.2)
        GPIO.output(i,0)
        time.sleep(.2)

while 1:
    n=GPIO.input(12)
    print(n)
    if n == 1:
        GPIO.output(16,1)
        GPIO.output(17,1)
        GPIO.output(20,0)
        GPIO.output(6,0) 
        time.sleep(1)
        GPIO.output(16,0)
        GPIO.output(17,0)
        GPIO.output(21,1)
        GPIO.output(19,1)
        
    if n==0:
        GPIO.output(20,1)
        GPIO.output(6,1)
        GPIO.output(19,0)
        GPIO.output(21,0)
        GPIO.output(19,0)
       
    
    
      
        
                                                                                      

GPIO.cleanup()
