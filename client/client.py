#!/usr/bin/env python

import socket
import sys
import os
import math
import LoginWindow
import threading
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, Qt, QThread, pyqtSignal
from LoginWindow import Ui_LoginWindow
from UIwindow import Client

SIZE = 8192


def initWindows():
    App = QApplication(sys.argv)
    client = Client()
    sys.exit(App.exec_())



def initSocket(host, port):
    try:
        clisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clisock.connect((host, port))
        while True:
            #   print(clisock.recv(size).decode())
            msg = clisock.recv(SIZE).decode()
            if not msg:
                break
            print(msg)
            command = input("command: ")
            parameter = input("parameter: ")
            if not data:
                break
            data = command+' '+parameter + '\r\n'
            clisock.send(data.encode())

        clisock.close()
    except:
        clisock.send('exit'.encode())
        print("cannot reach the server")

# def PORTmethod():
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.bind(('', 6785))
#     sock.listen(10)
#     while True:
#         print("Server Waiting for connection")
#         try:
#             Client, address = sock.accept()
#             while True:
#                 msg = Client.recv(SIZE).decode()
#                 print(msg)
#                 rpl = msg.upper().encode()
#                 Client.send(rpl)
#         finally:
#             Client.close()
#             break
#     sock.close()



def get_local_ip():
    local_ip = ''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
        print(local_ip)
    except:
        local_ip.close()
    return local_ip


if __name__ == "__main__":
    # initSocket('localhost', 21)
    client = Client()

