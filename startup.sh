#!/bin/sh
# change directories and execute startup programs
sudo python3 solenoid-frequency.py &
sleep 5
sudo python3 solenoid-control.py &
