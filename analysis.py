import time
import datetime
import sys

while True:
    TEMPavg = open("Temp.txt","r")
    print(TEMPavg)
    int(TEMPavg)
    if (TEMPavg < 26):
            continue
        elif (TEMPavg >=26 and TEMPavg <= 32):
            OFF = 10
        elif (TEMPavg >32 and TEMPavg < 35):
            OFF = 8
        elif (TEMPavg >= 35 and TEMPavg <= 38):
            OFF = 6
        elif (TEMPavg > 38 and TEMPavg < 41 ):
            OFF = 4
        elif (TEMPavg >= 41):
            OFF = 2
        file = open("OFF.txt","w")
        file.write(str(OFF))
        time.sleep(15*60)
