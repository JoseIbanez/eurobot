from time import sleep
from mylib_semaforo import set_semaforo, set_motor



c = 0
set_semaforo(1,"red")
sleep(1)

m1 = 0
m2 = 0

while 1:

    c = c + 1

    if c <= 80:
        m1 = m1 + 1
        m2 = m2 + 1

    if c == 170:
        m1 = 0
        m2 = 0

    if c == 180:
        m1 = -30
        m2 = -30


    print(c, m1, m2)

    if m1 > 40 or m2 > 40:
        set_semaforo(1,"green")
    else:
        set_semaforo(1,"yellow")

    set_motor(1,m1)
    set_motor(2,m2)

    sleep(.1)

    if c >= 200:
        break

set_semaforo(1,"red")
set_motor(1,0)
set_motor(2,0)


