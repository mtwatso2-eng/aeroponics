#!/usr/bin/python3
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# import libraries
# For Pi Board inputs
import board
import digitalio
import busio

# For Pi Software
import Adafruit_DHT
import socket
import csv
import time
import datetime
import sys
import threading

#This is for the Photoresistor
# Configure ADC connections
# Try to create an I2C device
#i2c = busio.I2C(board.SCL, board.SDA)
# Try to create an SPI device
#import adafruit_ads1x15.ads1115 as ADS
#from adafruit_ads1x15.analog_in import AnalogIn
#print("Connected")

# Set Sensor Type and Pin Number (BCM)
DHT_TYPE = Adafruit_DHT.DHT22
DHT_PIN = 23

# How often a measurement will be taken
FREQUENCY_SECONDS = 10

# Create humidity and temperature arrays for running averages
HUM = []
TEMP = []
#LIGHT = []

#Loop
while True:
    #Read sensors
    humidity, temperature = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
    #ads = ADS.ADS1115(i2c)
    #chan = AnalogIn(ads, ADS.P2)

    #Check for null data and remeasure
    if humidity is None or temperature is None:
        time.sleep(2)
        continue
    #add value to the end of the list
    HUM.append(humidity)
    TEMP.append(temperature)
    #LIGHT.append(chan.voltage)
    #check length of list
    count = len(HUM)
    #amount of values to average
    length = 15
    #check for correct amount. Removes or adds
    if (count == length):
        continue
    elif (count > length):
        HUM.pop(0)
        TEMP.pop(0)
        #LIGHT.pop(0)
    elif (count < length):
        HUM.append(humidity)
        TEMP.append(temperature)
        #LIGHT.append(chan.value)
    #Average the values
    count = len(HUM)
    HUMsum = sum(HUM)
    TEMPsum = sum(TEMP)
    #LIGHTsum = sum(LIGHT)
    HUMavg = HUMsum/count
    TEMPavg = TEMPsum/count
    #LIGHTavg = LIGHTsum/count
    #Clean everything up
    TEMPavg = round(TEMPavg, 3)
    HUMavg = round(HUMavg, 3)
    #Remove first value of the list
    HUM.pop(0)
    TEMP.pop(0)
    #LIGHT.pop(0)
    if (TEMPavg < 26):
        OFF = 5
    elif (TEMPavg >=26 and TEMPavg <= 32):
        OFF = 6
    elif (TEMPavg >32 and TEMPavg < 35):
        OFF = 7
    elif (TEMPavg >= 35 and TEMPavg <= 38):
        OFF = 8
    elif (TEMPavg > 38 and TEMPavg < 41 ):
        OFF = 9
    elif (TEMPavg >= 41):
        OFF = 10
    print(OFF)
    file2 = open("OFF.txt","w")
    file2.write(str(OFF))
    time.sleep(FREQUENCY_SECONDS)

        #Save Data locally
        #with open('output.csv', 'a', newline='') as output:
        #    output = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #    output.writerow([humidity, temperature, chan.value, chan.voltage])
        #time.sleep(FREQUENCY_SECONDS)
