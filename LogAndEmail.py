import time
import json
import sys
import datetime
import csv

# For Pi Board inputs
import board
import digitalio
import busio
#Log sensor data, log locally, append to the cloud
# For Pi Software
import Adafruit_DHT
import socket

#For email
import smtplib
import ssl
port = 465
password = input("")
