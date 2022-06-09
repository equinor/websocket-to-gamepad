from numpy import interp


class GamepadButtons():
    def __init__(self):
        self.A_BUTTON = 0
        self.B_BUTTON = 0
        self.LJS_X = 0
        self.LJS_Y = 0
        self.RJS_X = 0
        self.RJS_Y = 0
        self.BUTTON_CHANGED = 0

  

    def update_button_values(self, button_values):
        new_A_value = button_values[0]
        new_B_value = button_values[1]
        if self.A_BUTTON != new_A_value:
            self.BUTTON_CHANGED = 1
            self.A_BUTTON = new_A_value
        if self.B_BUTTON != new_B_value:
            self.BUTTON_CHANGED = 2
            self.B_BUTTON = new_B_value
            
    def update_joystick_values(self, joystick_values):
        self.LJS_X =  int(interp(joystick_values[1],[-1000,1000],[-32768,32767]))
        self.LJS_Y =  int(interp(joystick_values[0],[-1000,1000],[-32768,32767]))
        self.RJS_X =  int(interp(joystick_values[3],[-1000,1000],[-32768,32767]))
        self.RJS_Y =  int(interp(joystick_values[2],[-1000,1000],[-32768,32767]))
      






