import time
import datetime
import sys

while True:
    file = open("Temp.txt","r")
    TEMPavg = file.read()
    TEMPavg = float(TEMPavg)
    if (TEMPavg < 26):
        OFF = 300
    elif (TEMPavg >=26 and TEMPavg <= 32):
        OFF = 290
    elif (TEMPavg >32 and TEMPavg < 35):
        OFF = 280
    elif (TEMPavg >= 35 and TEMPavg <= 38):
        OFF = 260
    elif (TEMPavg > 38 and TEMPavg < 41 ):
        OFF = 250
    elif (TEMPavg >= 41):
        OFF = 240
    file2 = open("OFF.txt","w")
    file2.write(str(OFF))
    time.sleep(900)
