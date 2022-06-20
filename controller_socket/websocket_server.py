import hid
from simple_websocket_server import WebSocket, WebSocketServer

#for device in hid.enumerate():
 #   print(f"0x{device['vendor_id']:04x}:0x{device['product_id']:04x} {device['product_string']}")

gamepad = hid.device()
gamepad.open(0x045e, 0x02ff)
gamepad.set_nonblocking(True)
#while True:
#    report = gamepad.read(64)
#    print(report)
#    js_01 = report[0]
#    if report:

class SimpleEcho(WebSocket):
    def handle(self):
        # echo message back to client
        pass



    def connected(self):
        print(self.address, 'connected')


    def handle_close(self):
        print(self.address, 'closed')


server = WebSocketServer('localhost', 6259, SimpleEcho)
server.serve_forever()
