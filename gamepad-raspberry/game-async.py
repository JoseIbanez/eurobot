import asyncio
import evdev


speed_l = 0
speed_r = 0


async def scan(devpath):
    global speed_l, speed_r
    dev = evdev.InputDevice(devpath)
    print("  * device opened")
    try:
        async for event in dev.async_read_loop():
            print("  event: {}".format(event))

            if event.code == evdev.ecodes.KEY_C and event.value>0:
                print(f"Up Trigger: {event.value}")
                speed_l += 1
                speed_r += 1

    finally:
        dev.close()
        print("  * device closed")


async def soft_break():
     global speed_l, speed_r
     while True:
        await asyncio.sleep(1)
        print(f"b {speed_l} {speed_r}")
        if speed_l > 0:
            speed_l -= 1
            speed_r -= 1


async def amain():

    task1 = asyncio.create_task(scan("/dev/input/event2"))
    task2 = asyncio.create_task(soft_break())

    while True:
        await asyncio.sleep(10)
    
    task1.cancel()
    while not task.done():
       await asyncio.sleep(0.1)




asyncio.run(amain())


