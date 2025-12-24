
from time import sleep
from mylib_ledring import set_led, set_tail, clear

c = 0
color = (0, 100, 0)
clear()

while 1:

    c = c + 1
    pos = c % 12
    set_tail(pos, 5, color, direction=1)

    sleep(.1)


