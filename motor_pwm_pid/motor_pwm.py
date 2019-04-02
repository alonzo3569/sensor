import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
#try:
#    while True:
GPIO.output(21,False)

GPIO.output(20,True)
print "hi"

#pwm = GPIO.PWM(20,80)
#
#pwm.start(0)

#print "ready to try"
#try:
#    while True:
#        for i in range(0,101,1):
#            pwm.ChangeDutyCycle(100)
#            time.sleep(.02)
#            print "turn on"
#
#        for i in range(100,-1,-1):
#            pwm.ChangeDutyCycle(100)
#            time.sleep(.02)
#            print "turn off"

#except KeyboardInterrupt:
#    pass


#finally:
#    pwm.stop()
#    GPIO.cleanup()
