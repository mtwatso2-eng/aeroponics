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

# Configure ADC connections
# Try to create an I2C device
i2c = busio.I2C(board.SCL, board.SDA)

# Try to create an SPI device
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
print("Connected")

# Set Sensor Type and Pin Number (BCM)
DHT_TYPE = Adafruit_DHT.DHT22
DHT_PIN = 23

#init list with pin numbers
#pinList = [21, 22, 27, 17]

#Set all pins high
#for i in pinList:
#    GPIO.setup(i, GPIO.OUT)
#    GPIO.output(i, GPIO.HIGH)

#Set loop time in seconds
FREQUENCY_SECONDS       = 30

#PrintToConsole
print('Logging sensor measurements to {0} every {1} seconds.')
print('Press Ctrl-C to quit.')

#setvariables and type
humidity = 0.0
temperature = 0.0
ads = 0.0
chan = 0.0

#create lists
HUM = []
TEMP = []
LIGHT = []

#Loop
while True:
    #Read sensors
    humidity, temperature = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
    ads = ADS.ADS1115(i2c)
    chan = AnalogIn(ads, ADS.P2)
    if humidity is None or temperature is None:
        time.sleep(2)
        continue
    HUM.append(humidity)
    TEMP.append(temperature)
    LIGHT.append(chan.value)
    count = len(HUM)
    if (count >= 5):
        HUM.append(humidity)
        TEMP.append(temperature)
        LIGHT.append(chan.value)
    else:
        continue
    print(len(HUM), len(TEMP), len(LIGHT))
    HUMsum = sum(HUM)
    TEMPsum = sum(TEMP)
    LIGHTsum = sum(LIGHT)
    HUMavg = HUMsum/5
    TEMPavg = TEMPsum/5
    LIGHTavg = LIGHTsum/5
    print(HUMavg, TEMPavg, LIGHTavg)
    HUM.pop()
    TEMP.pop()
    LIGHT.pop()
    time.sleep(FREQUENCY_SECONDS)



    #Save Data locally
    #with open('output.csv', 'a', newline='') as output:
    #    output = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #    output.writerow([humidity, temperature, chan.value, chan.voltage])
    #time.sleep(FREQUENCY_SECONDS)
