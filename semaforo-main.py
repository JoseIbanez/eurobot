import time
from adafruit_pca9685 import PCA9685
from board import SCL, SDA
import busio


i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c, address=64)
pca.frequency = 1000

pca.channels[4].duty_cycle = 0x0
pca.channels[5].duty_cycle = 0x0
pca.channels[6].duty_cycle = 0x0
pca.channels[8].duty_cycle = 0x0
pca.channels[9].duty_cycle = 0x0
pca.channels[10].duty_cycle = 0x0



#rojo
pca.channels[4].duty_cycle = 0xFFFF
pca.channels[10].duty_cycle = 0xFFFF
time.sleep(3)

#amarillo
pca.channels[5].duty_cycle = 0xFFFF
pca.channels[4].duty_cycle = 0x0

pca.channels[10].duty_cycle = 0x0
pca.channels[9].duty_cycle = 0xFFFF


time.sleep(1)

#verde
pca.channels[5].duty_cycle = 0x0
pca.channels[6].duty_cycle = 0xFFFF

pca.channels[10].duty_cycle = 0xFFFF
pca.channels[9].duty_cycle = 0x0


time.sleep(3)


pca.channels[4].duty_cycle = 0x0
pca.channels[5].duty_cycle = 0x0
pca.channels[6].duty_cycle = 0x0
pca.channels[8].duty_cycle = 0x0
pca.channels[9].duty_cycle = 0x0
pca.channels[10].duty_cycle = 0x0


