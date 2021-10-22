#!/usr/bin/env python
import socket

size = 8192

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 6785))
sock.listen(10)
while True:
    print("Server Waiting for connection")
    try:
        Client, address = sock.accept()
        while True:
            msg = Client.recv(size).decode()
            print(msg)
            rpl = msg.upper().encode()
            Client.send(rpl)
    finally:
      Client.close()
      break
sock.close()