#!/user/bin/python3
import json
import sys
import time
import datetime
# For Pi Board inputs
import board
import digitalio
import busio
# For Pi Software
import Adafruit_DHT
import socket
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [21, 22, 27, 17]


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

while True:
    # Attempt to get sensor reading.
    humidity, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
    ads = ADS.ADS1115(i2c)
    chan = AnalogIn(ads, ADS.P2)

    print('Temperature: {0:0.1f} C'.format(temp))
    print('Humidity:    {0:0.1f} %'.format(humidity))
    print(chan.value, chan.voltage)

    time.sleep(4)
