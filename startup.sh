#!/bin/sh
# change directories and execute startup programs
sudo python3 environmentalLogger.py &
sudo python3 solenoid-control.py &
