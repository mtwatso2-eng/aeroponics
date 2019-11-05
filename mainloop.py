#Set all pins high
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

#Set loop time in seconds
FREQUENCY_SECONDS       = 60

#PrintToConsole
print('Logging sensor measurements to {0} every {1} seconds.')
print('Press Ctrl-C to quit.')

#Loop
while True:
    #Read sensors
    humidity, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
    ads = ADS.ADS1115(i2c)
    chan = AnalogIn(ads, ADS.P2)
    #Check for errors
        if humidity is None or temp is None:
            error = True
            time.sleep(5)
            continue
        if error = True


    #Save Data locally
    with open('output.csv', mode='w') as output
        output = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        output.writerow([humidity, temp, humidity, chan.value, chan.voltage, error])
    try:
        GPIO.output(21, GPIO.LOW)
        print ("ONE")

    if Error
