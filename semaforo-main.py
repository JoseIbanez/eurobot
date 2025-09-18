import time
from adafruit_pca9685 import PCA9685
from board import SCL, SDA
import busio


i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c, address=64)
pca.frequency = 1000

pca.channels[4].duty_cycle = 0xFFFF
time.sleep(1)

pca.channels[5].duty_cycle = 0xFFFF
time.sleep(1)

pca.channels[6].duty_cycle = 0xFFFF
time.sleep(1)


pca.channels[4].duty_cycle = 0x0
pca.channels[5].duty_cycle = 0x0
pca.channels[6].duty_cycle = 0x0
pca.channels[7].duty_cycle = 0x0


