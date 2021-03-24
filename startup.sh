#!/bin/sh
# change directories and execute startup programs
cd $(dirname $(realpath $0))
sudo python3 environmentalLogger.py &
sudo python3 solenoid-control.py &
