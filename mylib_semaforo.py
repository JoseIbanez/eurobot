import time
import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import motor



i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c, address=64)
pca.frequency = 1000


motor1 = motor.DCMotor(pca.channels[0], pca.channels[1])
# Set motor to active braking mode to improve performance
motor1.decay_mode = motor.SLOW_DECAY  

motor2 = motor.DCMotor(pca.channels[2], pca.channels[3])
# Set motor to active braking mode to improve performance
motor2.decay_mode = motor.SLOW_DECAY  



def set_semaforo(pos:int,color:str):

    base = 8
    if pos == 2:
        base = 12
    

    if color == "rojo" or color == "red":
        pca.channels[base+0].duty_cycle = 0xFFFF
        pca.channels[base+1].duty_cycle = 0x0
        pca.channels[base+2].duty_cycle = 0x0

    elif color == "amarillo" or color == "yellow":
        pca.channels[base+0].duty_cycle = 0x0
        pca.channels[base+1].duty_cycle = 0xFFFF
        pca.channels[base+2].duty_cycle = 0x0

    elif color == "verde" or color == "green":
        pca.channels[base+0].duty_cycle = 0x0
        pca.channels[base+1].duty_cycle = 0x0
        pca.channels[base+2].duty_cycle = 0xFFFF

    else:
        pca.channels[base+0].duty_cycle = 0x0
        pca.channels[base+1].duty_cycle = 0x0
        pca.channels[base+2].duty_cycle = 0x0



def set_motor(pos:int, throttle:int):
    global motor1
    global motor2

    t = throttle / 100

    if t > 1:
        t = 1

    elif t < -1:
        t = -1

    if pos == 1:
        motor1.throttle = t

    elif pos == 2:
        motor2.throttle = t

    

