import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)
for x in range(0,10):
        print "LED ON"
	GPIO.output(23,GPIO.HIGH)
	time.sleep(100)
	print "LED OFF"
	GPIO.output(23,GPIO.LOW)
	time.sleep(100)
