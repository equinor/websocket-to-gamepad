import json
from threading import Thread

import websocket


class ControllerSocket():
    def __init__(self, host, port) -> None:
        #websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(f"ws://{host}:{port}",
                              on_open=self._on_open,
                              on_error=self._on_error,
                              on_message=self._on_message)
        self.thread = Thread(target = self.ws.run_forever)
        self.thread.daemon = True
        self.js_values  = [0,0,0,0]
        self.button_values = [0,0]
        self.battery_level = 100
    
    def _on_message(self, ws_app, message):
        try:
            message = json.loads(message)
        except:
            print("Message is not json")
            return

        js_left_y = message["payload"]["joystick_01"]
        js_left_x = message["payload"]["joystick_02"]
        js_right_y = message["payload"]["joystick_03"]
        js_right_x = message["payload"]["joystick_04"]
        switch_02 = message["payload"]["switch_02"]
        switch_03 = message["payload"]["switch_03"]
        battery_level = message["payload"]["win_ru_battery"]
        self.js_values =  [js_left_y, js_left_x, js_right_y, js_right_x]
        self.button_values = [switch_02, switch_03]
        self.battery_level = battery_level




    def _on_open(self, other):
        print("Opened connection")
        self.ws.send("ControllerSocket connected")

    def _on_error(self, e, other):
        print(e)

    def connect(self):
        self.connected = True
        self.thread.start()



