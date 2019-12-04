#!/usr/bin/python

#import RPi.GPIO as GPIO
import time
import sys
import datetime
import ON from mainloop
import OFF from mainloop
import RPi.GPIO as GPIO
from setup import pinList
import time

# loop through pins and set mode and state to 'high'
#Set Relay Pins
GPIO.setmode(GPIO.BCM)

#init list with pin numbers
pinList = [21]

for i in pinList:
    #Set all pins high
    #for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

# main loop
while True:
    try:
      GPIO.output(21, GPIO.LOW)
      print ("ON")
      time.sleep(ON);
      GPIO.output(21, GPIO.HIGH)
      time.sleep(OFF)
      GPIO.cleanup()
