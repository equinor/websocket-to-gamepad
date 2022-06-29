
from numpy import interp
from vgamepad import XUSB_BUTTON, VX360Gamepad

from controller_socket.controller_socket import ControllerSocket

JS_INPUT_MIN = -1000
JS_INPUT_MAX = 1000
JS_OUTPUT_MIN = -32768
JS_OUTPUT_MAX = 32767

class GamepadEmulator():
    def __init__(self) -> None:
        self.virtual_gamepad = VX360Gamepad()
        self.controller_socket = ControllerSocket()
        self.controller_socket.connect()
        self.BUTTONS: dict(str, int) = {"A": 0, "B": 0}
        self.button_address:dict (str, XUSB_BUTTON) = {"A": XUSB_BUTTON.XUSB_GAMEPAD_A,
        "B": XUSB_BUTTON.XUSB_GAMEPAD_B}

        self.JOYSTICKS: dict(str, int) = {"LEFT_X": 0, "LEFT_Y": 0, "RIGHT_X": 0, "RIGHT_Y": 0}

    def update_joystick_values(self):
        for count,(joystick, previous_value) in enumerate(self.JOYSTICKS.items()):
            self.JOYSTICKS[joystick] = self.interpolate_joystick_value(value = self.controller_socket.js_values[count])

        self.virtual_gamepad.left_joystick(x_value=self.JOYSTICKS["LEFT_X"], y_value=self.JOYSTICKS["LEFT_Y"])
        self.virtual_gamepad.right_joystick(x_value=self.JOYSTICKS["RIGHT_X"], y_value=self.JOYSTICKS["RIGHT_Y"])
    
    def interpolate_joystick_value(self,value):
        return int(interp(value,[JS_INPUT_MIN, JS_INPUT_MAX], [JS_OUTPUT_MIN,JS_OUTPUT_MAX]))
  
    def update_button_values(self):
        for count,(button, previous_value) in enumerate(self.BUTTONS.items()):
            self.BUTTONS[button] = self.controller_socket.button_values[count]
            if self.BUTTONS[button] != previous_value:
                self.actuate_virtual_button(button=button)


    def actuate_virtual_button(self,button):
        if self.BUTTONS[button]:
            self.virtual_gamepad.press_button(button=self.button_address[button])
        else:
            self.virtual_gamepad.release_button(button=self.button_address[button])


    def update_virtual_gamepad(self):
       # print(self.controller_socket.js_values)
        if self.controller_socket.battery_level <= 10:
            print(f"Low battery: {self.controller_socket.battery_level}%")

        self.update_joystick_values()
        self.update_button_values()
        self.virtual_gamepad.update()

    def run(self):
        while True:
            self.update_virtual_gamepad()
