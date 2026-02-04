"""
Servo Motor Test Script (adafruit_motor version)

This script replicates the functionality of servo-main.py using the lower-level
adafruit_motor and adafruit_pca9685 libraries.

It initializes the PCA9685 (address 0x41) and performs a movement test 
on servos connected to channel 0 and channel 15.
"""
import time
import board
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize PCA9685 class
pca = PCA9685(i2c, address=0x41)
pca.frequency = 50

# Create Servo objects
# servo-main.py used range 500-2400
servo0 = servo.Servo(pca.channels[0], min_pulse=500, max_pulse=2400)
servo15 = servo.Servo(pca.channels[15], min_pulse=500, max_pulse=2400)

time.sleep(2)

for i in [0, 1, 2]:
    print("pos 1")
    servo0.angle = 90
    servo15.angle = 0
    time.sleep(0.5)

    print("pos 2")
    servo0.angle = 0
    servo15.angle = 100
    time.sleep(0.5)

print("pos 3")
servo0.angle = 90
servo15.angle = 0
time.sleep(1)

# De-initialize to release resources (good practice, though script ends anyway)
pca.deinit()
