#!/usr/bin/python

import RPi.GPIO as GPIO
from setup import pinList

# loop through pins and set mode and state to 'high'

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 2

# main loop

try:
  GPIO.output(21, GPIO.LOW)
  print ("ONE")
  time.sleep(SleepTimeL);
  GPIO.output(22, GPIO.LOW)
  print ("TWO")
  time.sleep(SleepTimeL);
  GPIO.output(27, GPIO.LOW)
  print ("THREE")
  time.sleep(SleepTimeL);
  GPIO.output(17, GPIO.LOW)
  print ("FOUR")
  time.sleep(SleepTimeL);
  GPIO.cleanup()
  print ("Good bye!")

# End program cleanly with keyboard
except KeyboardInterrupt:
  print ("  Quit")

  # Reset GPIO settings
  GPIO.cleanup()
