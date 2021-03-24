#!/usr/bin/python

#import RPi.GPIO as GPIO
import time
import sys
import datetime
import RPi.GPIO as GPIO
import math

#init list with pin numbers
pinList = [21]

# for ON time calculation based on plant age
startTime = datetime.datetime.now()


# time to sleep between operations in the main loop
ON = 1
# Set initial off duration – this changes based on OFF time
OFF = 5

# main loop
while True:
    file = open("daysOffset.txt","r")
    daysOffset = file.read(float(file))
    daysOld = daysOffset - (startTime - datetime.datetime.now()).total_seconds() / 86400
    maxDuration = 3
    minDuration = 1
    rateConstant = 0.5
    daysMidpoint = 7
    ON = maxDuration - (maxDuration - minDuration) / (1 + math.exp(-rateConstant * (daysOld - daysMidpoint)))
    # equation for desmos.com:
    # y\ =\ \frac{\left(3-1\right)}{1+\ e^{-0.5\left(x-7\right)}}+1

    try:
        file = open("temperature.txt", "r")
        TEMPavg = float(file.read())
        maxPeriod = 300
        minPeriod = 250
        rateConstant = 0.5
        temperatureMidpoint = 31
        OFF = maxPeriod - (maxPeriod - minPeriod) / (1 + math.exp(-rateConstant * (TEMPavg - temperatureMidpoint)))
        # equation for desmos.com:
        # y\ =\ -\frac{\left(300-250\right)}{1+\ e^{-0.5\left(x-31\right)}}+300
    except:
        pass

    # uncomment to see ON/OFF times without running solenoid
    # print(ON)
    # print(OFF)
    # time.sleep(2)
    # continue

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
