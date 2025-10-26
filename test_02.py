from mylib_gamepad import gamepad, KEY_F, KEY_E, KEY_C, KEY_D
from time import sleep


while 1:

    gamepad.get_events()


    if gamepad.check_event(KEY_F):
         print("f")

    sleep(.1)   


