#!/usr/bin/python


while True:
    import RPi.GPIO as GPIO
    import time
    # loop through pins and set mode and state to 'high'

    pinList = [21]

    GPIO.setmode(GPIO.BCM)

    for i in pinList:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)

    # time to sleep between operations in the main loop

        SleepTimeL = 4

    # main loop

    try:
      GPIO.output(21, GPIO.LOW)
      print ("ONE")
      GPIO.cleanup()
      print ("Good bye!")

    # End program cleanly with keyboard
    except KeyboardInterrupt:
        print ("  Quit")

    # Reset GPIO settings
    GPIO.cleanup()
