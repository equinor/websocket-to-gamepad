
from threading import Thread

from inputs import get_gamepad


class XGamePad(Thread):
    def __init__(self):			
        Thread.__init__(self, daemon=True)		# thread init class (don't forget this)
        self.A = 0			# all vars of gamepad, set init val to 0
        self.B = 0
        self.X = 0
        self.Y = 0
        self.LBumper = 0	
        self.RBumper = 0
        self.LThumb = 0	
        self.RThumb = 0
        self.LTrigger = 0	
        self.RTrigger = 0	
        self.Back = 0
        self.Start = 0
        self.LStickX = 0
        self.LStickY = 0
        self.RStickX = 0
        self.RStickY = 0
        self.DPadX = 0
        self.DPadY = 0
        self.message = ""

    def run(self):		# run is a default Thread function
        while True:	# loop for ever
            for event in get_gamepad():	# check events of gamepads, if not event, all is stop
                if event.ev_type == "Key":	# category of binary respond values
                    if event.code == "BTN_SOUTH":
                        self.A = event.state
                    elif event.code == "BTN_EAST":
                        self.B = event.state
                    elif event.code == "BTN_WEST":
                        self.X = event.state
                    elif event.code == "BTN_NORTH":
                        self.Y = event.state
                    elif event.code == "BTN_TL":
                        self.LBumper = event.state
                    elif event.code == "BTN_TR":
                        self.RBumper = event.state
                    elif event.code == "BTN_THUMBL":
                        self.LThumb = event.state
                    elif event.code == "BTN_THUMBR":
                        self.RThumb = event.state
                    elif event.code == "BTN_START":
                        self.Back = event.state
                    elif event.code == "BTN_SELECT":
                        self.Start = event.state
                
                elif event.ev_type == "Absolute":	# category of analog values
                                    # some values are from -32000 to 32000, or -256 to 256
                                    # here all values are mapped from -512 to 512 by bitshifting
                    if event.code[-1:] == "Z":
                        event.state = event.state<<1	# reduce range from 256 to 512
                    else:
                        event.state = event.state>>6	# reduce range from 32000 to 512
                    
                    if event.state < 40 and event.state > -40:  # dead zone of my joypad, check this one for yours
                        event.state = 0
                    
                    if event.code == "ABS_Z":
                        self.LTrigger = event.state
                    elif event.code == "ABS_RZ":
                        self.RTrigger = event.state
                    elif event.code == "ABS_X":
                        self.LStickX = event.state
                    elif event.code == "ABS_Y":
                        self.LStickY = event.state
                    elif event.code == "ABS_RX":
                        self.RStickX = event.state
                    elif event.code == "ABS_RY":
                        self.RStickY = event.state
                    elif event.code == "ABS_HAT0Y":
                        self.DPadX = event.state
                    elif event.code == "ABS_HAT0X":
                        self.DPadY = event.state
            self.encode_message()

    def encode_message(self):
        message = f'{{"payload": {{"joystick_01": {-self.LStickX}, "joystick_02": {-self.LStickY}, "joystick_03": {self.RStickX}, "joystick_04": {self.RStickY}, "switch_02": {self.A}, "switch_03": {self.B}, "win_ru_battery": 90}} }}'
        #print(message)
        self.message = message


