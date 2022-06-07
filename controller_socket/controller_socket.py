import websocket
from threading import Thread
import json

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
        self.switch_02 = 0

    def __on_message(self,ws, message):
        message = json.loads(message)
        js01 = message["payload"]["joystick_01"]
        js02 = message["payload"]["joystick_02"]
        js03 = message["payload"]["joystick_03"]
        js04 = message["payload"]["joystick_04"]
        switch_02 = message["payload"]["switch_02"]
        self.js_values =  [js01, js02, js03, js04]
        self.switch_02 = switch_02

    def __on_error(self,ws, error):
        print(error)

    def __on_close(self,ws, close_status_code, close_msg):
        print("### closed ###")

    def __on_open(self,ws):
        print("Opened connection")

    def connect(self):
        self.connected = True
        self.thread.start()

