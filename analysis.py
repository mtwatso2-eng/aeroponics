import time
import datetime
import sys

while True:
    file = open("Temp.txt","r")
    TEMPavg = file.read()
    print(TEMPavg)
    TEMPavg = float(TEMPavg)
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
    file2 = open("OFF.txt","w")
    file2.write(str(OFF))
    time.sleep(900)
