
#Bluethooth


```bash
bluetoothctl

scan on

pair XX:XX:XX:XX:XX:XX

trush XX:XX:XX:XX:XX:XX

connect XX:XX:XX:XX:XX:XX

```

example:

```bash
pi@rp3:~ $ bluetoothctl
Agent registered
[CHG] Controller B8:27:EB:B0:95:B2 Pairable: yes
[CHG] Device XX:XX:XX:XX:XX:XX Connected: no
[bluetooth]# pair XX:XX:XX:XX:XX:XX
[CHG] Device XX:XX:XX:XX:XX:XX Connected: yes
Authorize service
[agent] Authorize service 00001124-0000-1000-8000-00805f9b34fb (yes/no): yes
[8BitDo Micro gamepad]# trust XX:XX:XX:XX:XX:XX
[8BitDo Micro gamepad]# connect XX:XX:XX:XX:XX:XX
Attempting to connect to XX:XX:XX:XX:XX:XX
[CHG] Device XX:XX:XX:XX:XX:XX ServicesResolved: yes
Connection successful
[8BitDo Micro gamepad]# 
```


# Evtest

```bash

pi@rp3:~ $ sudo apt install evtest 
...
pi@rp3:~ $ ls -l /dev/input/
total 0
drwxr-xr-x 2 root root      60 Sep 30 08:22 by-path
crw-rw---- 1 root input 13, 64 Sep 30 08:22 event0
crw-rw---- 1 root input 13, 65 Sep 30 08:22 event1
crw-rw---- 1 root input 13, 66 Oct  2 17:33 event2
crw-rw---- 1 root input 13, 63 Sep 30 08:22 mice

```

```bash
pi@rp3:~ $ sudo evtest /dev/input/event2 
Testing ... (interrupt to exit)
Event: time 1759419817.879552, type 4 (EV_MSC), code 4 (MSC_SCAN), value 70008
Event: time 1759419817.879552, type 1 (EV_KEY), code 18 (KEY_E), value 1
Event: time 1759419817.879552, -------------- SYN_REPORT ------------
Event: time 1759419818.042009, type 4 (EV_MSC), code 4 (MSC_SCAN), value 70008
Event: time 1759419818.042009, type 1 (EV_KEY), code 18 (KEY_E), value 0
Event: time 1759419818.042009, -------------- SYN_REPORT ------------
Event: time 1759419819.409553, type 4 (EV_MSC), code 4 (MSC_SCAN), value 70008
Event: time 1759419819.409553, type 1 (EV_KEY), code 18 (KEY_E), value 1
Event: time 1759419819.409553, -------------- SYN_REPORT ------------
Event: time 1759419819.444523, type 4 (EV_MSC), code 4 (MSC_SCAN), value 70008
Event: time 1759419819.444523, type 1 (EV_KEY), code 18 (KEY_E), value 0
Event: time 1759419819.444523, -------------- SYN_REPORT ------------
Event: time 1759419820.407099, type 4 (EV_MSC), code 4 (MSC_SCAN), value 70009
Event: time 1759419820.407099, type 1 (EV_KEY), code 33 (KEY_F), value 1
Event: time 1759419820.407099, -------------- SYN_REPORT ------------
Event: time 1759419820.473282, type 4 (EV_MSC), code 4 (MSC_SCAN), value 70009
Event: time 1759419820.473282, type 1 (EV_KEY), code 33 (KEY_F), value 0
Event: time 1759419820.473282, -------------- SYN_REPORT ------------
^C
pi@rp3:~ $ sudo evtest /dev/input/event2 

```