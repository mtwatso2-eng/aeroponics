#!/bin/sh
# startup.sh
# change directories and execute startup programs

sudo python3 spreadsheet.py &
sudo python3 mainloop.py &
sleep 1m
sudo python3 analysis.py &
sleep 10
sudo python3 solenoid-cutting.py &

