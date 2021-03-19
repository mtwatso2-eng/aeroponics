#!/usr/bin/python

#import RPi.GPIO as GPIO
import time
import sys
import datetime
import RPi.GPIO as GPIO
#from setup import pinList
import time


# loop through pins and set mode and state to 'high'
#Set Relay Pins


#init list with pin numbers
pinList = [21]
#GPIO.cleanup()

#Set all pins high
#for i in pinList:

# time to sleep between operations in the main loop

ON = 4
# Set initial off duration – this changes based on OFF time
OFF = 5

# main loop
while True:
    file = open("watering-frequency.txt", "r")
    print(OFF)
    try:
    	OFF = int(file.read())
    except:
    	pass
    GPIO.setmode(GPIO.BCM)
    for i in pinList:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)
    try:
        GPIO.output(21, GPIO.LOW)
        print ("ON")
        time.sleep(ON);
        GPIO.output(21, GPIO.HIGH)
        print("OFF")
        time.sleep(OFF)
        GPIO.cleanup()
        continue
    except (KeyboardInterrupt, SystemExit):
        GPIO.cleanup()
        break