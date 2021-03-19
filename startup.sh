#!/bin/sh
# change directories and execute startup programs
sudo python3 watering-frequency.py &
sleep 1.3
sudo python3 solenoid-control.py &
