from time import sleep
#from mylib_semaforo import set_semaforo, set_motor

c=0
m1=0
m2=0
while 1:

    c=c+1
    if c<=40:
        m1=m1+1.0
        m2=m2+1
    if m1<20:
        print("rojo")
    elif m1<40:
        print("amarillo")
    else:
        print("verde")

    if c==155:
        m1=0
        m2=0
    if c==160:
        m1=-30
        m2=-30
    print(c,m1,m2)
    #set_motor(1,m1)
    #set_motor(2,m2)

    sleep(0.1)
    if c>=200:
        break
