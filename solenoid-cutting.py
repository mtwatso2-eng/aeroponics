#!/usr/bin/python

#import RPi.GPIO as GPIO
import time
import sys
import datetime
import ON from mainloop
import OFF from mainloop

#Set Relay Pins
GPIO.setmode(GPIO.BCM)

#init list with pin numbers
pinList = [21]

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
