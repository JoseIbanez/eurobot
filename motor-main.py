import time
from adafruit_pca9685 import PCA9685
from board import SCL, SDA
from adafruit_motor import motor
import busio


i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c, address=64)
pca.frequency = 1000


motor1 = motor.DCMotor(pca.channels[0], pca.channels[1])
motor1.decay_mode = motor.SLOW_DECAY  # Set motor to active braking mode to improve performance



print("Forwards slow")
motor1.throttle = 0.5
print("throttle:", motor1.throttle)
time.sleep(1)

print("Forwards fast")
motor1.throttle = 1.0
print("throttle:", motor1.throttle)
time.sleep(1)

print("Forwards slow")
motor1.throttle = 0.2
print("throttle:", motor1.throttle)
time.sleep(1)


print("Stop")
motor1.throttle = 0.0
print("throttle:", motor1.throttle)
time.sleep(1)
