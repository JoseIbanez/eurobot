import time
from adafruit_servokit import ServoKit 

pca = ServoKit(channels=16, address=0x41)


pca.servo[0].set_pulse_width_range(500, 2400)
pca.servo[15].set_pulse_width_range(500, 2400)
time.sleep(2)


for i in [0,1,2]:

   print("pos 1")
   pca.servo[0].angle =   90
   pca.servo[15].angle =  0
   time.sleep(0.5)

   print("pos 2")
   pca.servo[0].angle =   0
   pca.servo[15].angle = 100
   time.sleep(0.5)


print("pos 3")
pca.servo[0].angle =  90
pca.servo[15].angle =  0
time.sleep(1)

