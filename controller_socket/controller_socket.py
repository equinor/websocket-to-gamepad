import json
from threading import Thread

import websocket


class ControllerSocket():
    def __init__(self) -> None:
        #websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp("ws://localhost:6259",
                              on_open=self.__on_open,
                              on_message=self.__on_message,
                              on_error=self.__on_error,
                              on_close=self.__on_close)

        self.thread = Thread(target = self.ws.run_forever)
        self.thread.daemon = True
        self.js_values  = [0,0,0,0]
        self.button_values = [0,0]
        self.battery_level = 100

    def __on_message(self, message):
        print("yay")
        print(message)
        message = json.loads(message)
        js_left_y = message["payload"]["joystick_01"]
        js_left_x = message["payload"]["joystick_02"]
        js_right_y = message["payload"]["joystick_03"]
        js_right_x = message["payload"]["joystick_04"]
        switch_02 = message["payload"]["switch_02"]
        switch_03 = message["payload"]["switch_03"]
        battery_level = message["payload"]["win_ru_battery"]
        self.js_values =  [js_left_x, js_left_y, js_right_x, js_right_y]
        self.button_values = [switch_02, switch_03]
        self.battery_level = battery_level

    def __on_error(self,error):
        print(error)

    def __on_close(self):
        print("### closed ###")

    def __on_open(self):
        print("Opened connection")

    def connect(self):
        self.connected = True
        self.thread.start()

