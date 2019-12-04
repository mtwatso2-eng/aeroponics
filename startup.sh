#!/bin/sh
# startup.sh
# change directories and execute startup programs

python3 mainloop.py &
sleep 2m &
python3 analysis.py &
sleep 10 &
python3 solenoid-cutting.py &

