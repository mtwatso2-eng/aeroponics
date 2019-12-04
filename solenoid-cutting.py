#!/usr/bin/python

#import RPi.GPIO as GPIO
import time
import sys
import datetime
import RPi.GPIO as GPIO
from setup import pinList
import time
import threading

# loop through pins and set mode and state to 'high'
#Set Relay Pins
GPIO.setmode(GPIO.BCM)

#init list with pin numbers
pinList = [21]

#Set all pins high
#for i in pinList:

# time to sleep between operations in the main loop

# main loop
while True:
    from mainloop import OFF
    for i in pinList:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)
    try:
        GPIO.output(21, GPIO.LOW)
        print ("ON")
        time.sleep(ON);
        GPIO.output(21, GPIO.HIGH)
        time.sleep(OFF)
        GPIO.cleanup()
        continue
    except KeyboardInterrupt:
        print ("  Quit")
