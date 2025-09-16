import time
from adafruit_servokit import ServoKit 

pca = ServoKit(channels=16,fre)


pca.servo[0].set_pulse_width_range(500, 2400)
pca.servo[15].set_pulse_width_range(500, 2400)
time.sleep(2)

pca.servo[0].angle = 180
pca.servo[15].angle = 90
time.sleep(1)


pca.servo[0].angle = 90
pca.servo[15].angle = 0
time.sleep(1)


pca.servo[0].angle = 0
pca.servo[15].angle = 0
time.sleep(1)

