#!/bin/sh
# startup.sh
# change directories and execute startup programs
#cd ~/aeroponics
sudo python3 mainloop.py &
sleep 2
sudo python3 analysis.py &
sleep 2
#sudo python3 solenoid-cutting.py
