import evdev
#import numpy as np


device = evdev.InputDevice('/dev/input/event2')
print(device)



try:
    for event in device.read_loop():

        if event.type == evdev.ecodes.EV_KEY:

            # Right Trigger
            if event.code == evdev.ecodes.KEY_F:
                print(f"Right Trigger: {event.value}")

            # Left Trigger
            elif event.code == evdev.ecodes.KEY_E:
                print(f"Left Trigger: {event.value}")


            # Up Trigger
            elif event.code == evdev.ecodes.KEY_C:
                print(f"Up Trigger: {event.value}")

            # Down Trigger
            elif event.code == evdev.ecodes.KEY_D:
                print(f"Down Trigger: {event.value}")

            else:
                print(f"Key Event - Code: {event.code}, Value: {event.value}")


except KeyboardInterrupt:
    pass
finally:
    device.close()

print("Exiting...")
