# websocket-to-gamepad
[![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Repository to map input from a websocket server to a virtual gamepad (USB HID-device).


### Install
For local development, please fork the repository. Then, clone and install in the repository root folder:

```
git clone https://github.com/equinor/websocket-to-gamepad
cd websocket-to-gamepad
pip install -e .
```

### Run websocket-to-gamepad emulator
Install the repo in your python environment and run

```
python main.py
```

### Settings
Configuration parameters can be set in with environment variables to match your setup

Websocket server:
```bash
WS_SERVER_HOST = 'localhost'
WS_SERVER_PORT = 8000
```

Minimum and maximum values of the joysticks on your input device and the emulated gamepad:

```bash
JS_INPUT_MIN = -1000
JS_INPUT_MAX = 1000
JS_OUTPUT_MIN = -32768
JS_OUTPUT_MAX = 32767
```

### Testing
To test functionality of your emulated gamepad run [gamepad_tester.py](https://github.com/equinor/websocket-to-gamepad/test/gamepad_tester.py) with a physical gamepad connected and check result on [gamepadviewer](https://gamepadviewer.com/). The left joystick should be inverted on the emulated gamepad for the test.
