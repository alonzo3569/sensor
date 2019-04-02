import RPi.GPIO as GPIO
import curses
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

stdscr = curses.initscr()
stdscr.clear()

GPIO.output(27,GPIO.HIGH)
time.sleep(5)
GPIO.output(22,GPIO.LOW)
GPIO.output(23,GPIO.HIGH)
time sleep(5)
GPIO.output(24,GPIO.LOW)



