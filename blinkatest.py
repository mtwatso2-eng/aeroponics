import board
import digitalio
import busio

    # Try to create an I2C device
i2c = busio.I2C(board.SCL, board.SDA)
print("I2C ok!")

    # Try to create an SPI device
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

ads = ADS.ADS1115(i2c)
chan - AnalogIn(ads, ADS.PO)
print(chan.value, chan.voltage)
