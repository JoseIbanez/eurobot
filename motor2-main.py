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

throttle = 0.1
print("Acelera")
while throttle < 0.8:
    throttle += 0.01
    motor1.throttle = throttle
    time.sleep(.05)

time.sleep(2)

print("Frena")
while throttle > 0: 
    throttle -= .01
    if throttle < 0.1:
        throttle = 0

    motor1.throttle = throttle
    time.sleep(.01)



print("Stop")
motor1.throttle = 0.0
print("throttle:", motor1.throttle)
time.sleep(1)
