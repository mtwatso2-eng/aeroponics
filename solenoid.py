#!/usr/bin/python

#import RPi.GPIO as GPIO
import time
import sys
import datetime
import csv
import pandas as pd

#Set Relay Pins
#GPIO.setmode(GPIO.BCM)

#init list with pin numbers
#pinList = [21, 22, 27, 17]

#Set all pins high
#for i in pinList:
#    GPIO.setup(i, GPIO.OUT)
#    GPIO.output(i, GPIO.HIGH)

#Set loop time in seconds
#FREQUENCY_SECONDS       = 60

#Loop
while True:
    #Save Data locally
    df = pd.read_csv(output)
    Humidity = df.Humidity
    Temp = df.Temp
    LightVa = df.LightValue
    LightVo = df.LightVoltage

print (Humidty, Temp, LightVa, LightVo)
