import time
from operator import truediv

import hid
import vgamepad as vg
from numpy import interp


class GamepadButtons():
    def _init_(self):
        self.A_BUTTON = 0
        self.B_BUTTON = 0
        self.X_BUTTON = 0
        self.Y_BUTTON = 0
        self.RB_BUTTON = 0
        self.LB_BUTTON = 0
        self.RT_BUTTON = 0
        self.LT_BUTTON = 0
        self.LJS_X = 125
        self.LJS_Y = 125
        self.RJS_X = 125
        self.RJS_Y = 125

  

    def update_button_values(self, dec_val):
        bin_val = format(dec_val,"08b")

        print(f"={bin_val}")

        self.A_BUTTON = bin_val[0]
        self.B_BUTTON = bin_val[1]
        self.X_BUTTON = bin_val[2]
        self.Y_BUTTON = bin_val[3]
        self.RB_BUTTON = bin_val[4]
        self.LB_BUTTON = bin_val[5]

    def update_joystick_values(self, joystick_values):
        self.LJS_X =  int(interp(joystick_values[1],[0,255],[-32768,32767]))
        self.LJS_Y =  int(interp(joystick_values[3],[0,255],[-32768,32767]))
        self.RJS_X =  int(interp(joystick_values[5],[0,255],[-32768,32767]))
        self.RJS_Y =  int(interp(joystick_values[7],[0,255],[-32768,32767]))
      
      
        print(f"{joystick_values[1]=}")
        print(f"{self.LJS_X=}")



gamepad = vg.VX360Gamepad()

# press a button to wake the device up
gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
gamepad.update()
time.sleep(1)
gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
gamepad.update()
time.sleep(1)



# for device in hid.enumerate():
#   print(f"0x{device['vendor_id']:04x}:0x{device['product_id']:04x} {device['product_string']}")

logitech_f310 = hid.device()
logitech_f310.open(0x046d, 0xc21d)



gamepad_buttons = GamepadButtons()


# for device in hid.enumerate():
#    print(f"0x{device['vendor_id']:04x}:0x{device['product_id']:04x} {device['product_string']}")



while True:
    report = logitech_f310.read(64)
    if report:
#        print(report)
        gamepad_buttons.update_button_values(report[10])
        gamepad_buttons.update_joystick_values(report)



        gamepad.left_joystick(x_value=gamepad_buttons.LJS_X, y_value=gamepad_buttons.LJS_Y)  # values between -32768 and 32767
        gamepad.right_joystick(x_value=gamepad_buttons.RJS_X, y_value=gamepad_buttons.RJS_Y)  # values between -32768 and 32767

        gamepad.update()



