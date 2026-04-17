from time import sleep
from mylib_semaforo import set_semaforo, set_motor, set_servo
from mylib_gamepad import gamepad, KEY_C, KEY_D, KEY_G, KEY_F, KEY_E, KEY_M, KEY_K 

MAX = 100
c = 0
set_semaforo(1,"red")
sleep(1)

V1 = 50
V2 = 70

m1 = 0
m2 = 0
cs =0

while 1:


    gamepad.get_events()
    if gamepad.check_event(KEY_C):
       m1 = V1
       m2 = V1
       cs = 5

    if gamepad.check_event(KEY_D):
       m1 = -V1
       m2 = -V1
       cs = 5

    if gamepad.check_event(KEY_E):
       m1 = V2
       m2 = -V2
       cs = 5

    if gamepad.check_event(KEY_F):
       m1 = -V2
       m2 = V2
       cs = 5

    if ( not gamepad.check_event(KEY_C) and
         not gamepad.check_event(KEY_D) and
         not gamepad.check_event(KEY_E) and
         not gamepad.check_event(KEY_F) ):
       
       cs = cs - 1 
       if cs <= 0:
           m1 = 0
           m2 = 0

    if gamepad.check_event(KEY_G):
       m1 = 0
       m2 = 0

    if gamepad.check_event(KEY_M):
       set_servo(1,0)
       set_servo(2,0)

    if gamepad.check_event(KEY_K):
       set_servo(1,110)
       set_servo(2,110)

           


    if m2 > MAX:
       m2 = MAX

    if m2 < -MAX:
       m2 = -MAX

    if m1 > MAX:
       m1 = MAX

    if m1 < -MAX:
       m1 = -MAX



    print(c, m1, m2)

    if abs(m1) > 20 or abs(m2) > 20:
        set_semaforo(1,"green")
    else:
        set_semaforo(1,"yellow")


    set_motor(1,m1)
    set_motor(2,m2)

    sleep(.01)




set_semaforo(1,"red")
set_motor(1,0)
set_motor(2,0)


