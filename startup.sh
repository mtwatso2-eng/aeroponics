#!/bin/sh
# change directories and execute startup programs
sudo python3 watering-frequency.py &
sleep 5
sudo python3 solenoid-control.py &
