import logging
import time
from threading import Thread

from websocket import create_connection
from websocket_server import WebsocketServer
from xgamepad import XGamePad

from gamepad.emulated_gamepad import GamepadEmulator


class TestServer():
    def __init__(self):
        self.host = 'localhost'
        self.port = 6259

        self.server = WebsocketServer(host=self.host, port=self.port, loglevel=logging.DEBUG)
        self.server.set_fn_new_client(self.new_client)
        self.server.set_fn_message_received(self.message_recieved)
        self.server_thread = Thread(target=self.server.run_forever, daemon=True)
        self.gamepad = XGamePad()
        self.emulator = GamepadEmulator()
        self.emulator_thread = Thread(target=self.emulator.run, daemon=True)



    def new_client(self,client, server):
        print("new client")
        server.send_message_to_all("A new client joined")

    def message_recieved(self, client, server, message):
        server.send_message_to_all(message)


    def run(self):
            self.server_thread.start()
            self.gamepad.start()
            self.setup_test_socket()
            self.socket.send("Starting gamepad test socket")
            self.emulator_thread.start()
            while True:
                if self.gamepad.message:
                    print(self.gamepad.message)
                    self.socket.send(self.gamepad.message)
                time.sleep(0.1)


    def setup_test_socket(self):
            self.socket =  create_connection(f"ws://{self.host}:{self.port}")




