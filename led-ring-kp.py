
from time import sleep
from mylib_ledring import set_led, set_tail, clear
from mylib_gamepad import gamepad, KEY_C, KEY_D, KEY_G, KEY_F

c = 0
s = 1

color = (0, 100, 0)
clear()



while 1:

    c = c + 1
    pos = c % 12
    set_tail(pos, 5, color, direction=1)

    gamepad.get_events()
    if gamepad.check_event(KEY_C):
       s = s * 0.9

    if gamepad.check_event(KEY_D):
       s = s * 1.1

    if gamepad.check_event(KEY_G):
       break

    if gamepad.check_event(KEY_F):
       color = (color[1], color[2], color[0])


    sleep(s)


clear()

