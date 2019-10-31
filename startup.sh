#!/bin/sh
# startup.sh
# change directories and execute startup programs

cd /home/pi/code/aeroponics
sudo python3 solenoid.py
sudo python3 spreadsheet.py
cd
