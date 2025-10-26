import evdev
from evdev.ecodes import EV_KEY, KEY_F, KEY_E, KEY_C, KEY_D

class Gamepad:

    def __init__(self):

        try:
            self.device = evdev.InputDevice('/dev/input/event2')
            self.eventList = []
            print(self.device)

        except Exception as e:
            print(f"Error initializing gamepad: {e}")
            raise e 


    def close(self):
        self.device.close()


    def get_events(self):

        self.eventList = []
        try:
            while True:
                event = self.device.read_one()
                if not event:
                    break


                if event.type != evdev.ecodes.EV_KEY:
                    continue
            
                if event.value <= 0:
                    continue
                
                if event.value > 1:
                    self.eventList.append(event.code)
                
                self.eventList.append(event.code)
                print(event)


        except KeyboardInterrupt as e:
            raise KeyboardInterrupt from e

        except Exception as e:
            print(f"Error: {e}")


    def check_event(self, event_code):

        count = 0
        for event in self.eventList:
            if event == event_code:
                count += 1
 
        return count

# Create object
gamepad = Gamepad()
