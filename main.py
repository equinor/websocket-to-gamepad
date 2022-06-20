
from gamepad.emulated_gamepad import GamepadEmulator

emulator = GamepadEmulator()

while True:
  emulator.update_virtual_gamepad()
