from websocket import create_connection

ws = create_connection("ws://localhost:6259")
while True:
    message = "payload: joystick01: 0, joystick02: 0, joystick03: 0, joystick04: 0, switch_02: 0, switch_03: 0"
    ws.send(message)
    print("Sent")
    print("Receiving...")
    result =  ws.recv()
    print("Received '%s'" % result)
ws.close()
