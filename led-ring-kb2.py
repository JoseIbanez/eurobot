
from time import sleep
from mylib_ledring import set_led, set_tail, clear
from mylib_gamepad import gamepad, KEY_C, KEY_D, KEY_G, KEY_F

c = 0
s = 0
dir = 1
pos = 0

color = (100, 0, 0)
clear()



while 1:

    c = c + abs(s)
    if c > 100 and s>0:
        dir = 1
        c = 0
        pos = pos + dir
    elif c > 100 and s<0:
        dir = -1
        c = 0
        pos = pos + dir

    if s == 0:
        dir = 0

    set_led(pos, color)
    set_led((pos+1)%12, (0,0,0))
    set_led((pos-1)%12, (0,0,0))
    #set_tail(pos, 5, color, direction=dir)

    gamepad.get_events()
    if gamepad.check_event(KEY_C):
       s = s + 1

    if gamepad.check_event(KEY_D):
       s = s - 1

    if gamepad.check_event(KEY_G):
       s = 0

    if gamepad.check_event(KEY_F):
       color = (color[1], color[2], color[0])


    sleep(0.01)


clear()

