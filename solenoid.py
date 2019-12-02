#!/usr/bin/python

#import RPi.GPIO as GPIO
import time
import sys
import datetime
import HUMavg from mainloop
import TEMPavg from mainloop
import LIGHTavg from mainloop

FREQUENCY_SECONDS = 60*15

OFF = 300
ON = 7

While True:
    if 

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
#print("live")
#Loop
#while True:
    #Save Data locally
#    df = pd.read_csv("output.csv")
#    Humidity = df.Humidity
#    Temp = df.Temp
#    LightVa = df.LightValue
#    LightVo = df.LightVoltage
#    break

print(Humidity, Temp, LightVa, LightVo)
