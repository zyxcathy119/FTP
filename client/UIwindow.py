
import sys
import socket
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt5.QtGui import *
import threading
import time

from LoginWindow import Ui_LoginWindow
from CentralWindow import Ui_MainWindow

SIZE = 8190


class Loginwin(QtWidgets.QMainWindow, Ui_LoginWindow):
    def __init__(self):
        super().__init__() #python3继承
        self.setupUi(self) #创建Ui_LoginWindow
        self.setFixedSize(self.width(), self.height())
 

class Centralwin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__() #python3继承
        self.setupUi(self) #创建Ui_LoginWindow
        self.setFixedSize(self.width(), self.height())


class Client():

    clientIP = "127.0.0.1"
    serverIP = "127.0.0.1"
    clientControlPort = 8000
    clientDataPort = 8001
    clientDatafd = -1
    serverControlPort = 21
    clisock = -1
    clientFilePath ='/home/cathy/FTPCLIENT/'
    ServerDataPort = 20
    isSignin = False
    isPass = False
    username = ''
    password = ''
    ChooseCMD ={}


    def __init__(self):
        super().__init__()
        # self.chooseCMD()
        # self.loginwin = Loginwin()
        # self.centralwin = Centralwin()
        # self.loginwin.show()
        # self.centralwin.show()
        # t0 = threading.Thread(target=self.connectToServer, args=())
        # t0.start()
        
        # # self.connectToServer()
        # # self.loginwin.SignInbutton.clicked.connect(self.connectToServer)
        # self.centralwin.sendbutton.clicked.connect(self.sendCommand)
        self.initSocket('localhost',21)

    def initSocket(self,host, port):
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
                # self.chooseCMD.get(command)
                if command == 'PORT':
                    self.cmd_PORT()
                if command == 'RETR':
                    print("intoif\n")
                    t2=threading.Thread(target = self.cmd_RETR)
                    t2.start()
                data = command+' '+parameter + '\r\n'
                print(data)
                clisock.send(data.encode())

            clisock.close()
        except Exception as e:
            clisock.send('exit\r\n'.encode())
            print(str(e))
#------------------------------------------------------------------------------------------------------
    # def chooseCMD(self):
    #     self.ChooseCMD = {
    #         'USER':self.cmd_USER,
    #         'PASS':self.cmd_PASS,
    #         'PORT':self.cmd_PORT,
    #         'PASV':self.cmd_PASV,
    #         'RETR':self.cmd_RETR,
    #         'STOR':self.cmd_STOR,
    #         'QUIT':self.cmd_QUIT,
    #         'SYST':self.cmd_SYST,
    #         'TYPE':self.cmd_TYPE,
    #         'MKD':self.cmd_MKD,
    #         'CWD':self.cmd_CWD,
    #         'PWD':self.cmd_PWD,
    #         'LIST':self.cmd_LIST,
    #         'RMD':self.cmd_RMD,
    #         'RNFR':self.cmd_RNFR,
    #         'RNTO':self.cmd_RNTO,
    #     }

    
    def connectToServer(self):
        print("connectToserver begin\n")
        host = 'localhost'
        port = 21
        self.username = 'anonymous'
        self.password = 'cathy@com'
        try:
            # host = self.loginwin.ServerIPtext.toPlainText()
            # port = int(self.loginwin.ServerPorttext.toPlainText())
            # self.username = self.loginwin.Usernametext.toPlainText()
            # self.password = self.loginwin.Passwordtext.toPlainText()
            self.checkConnectInput()
        except Exception as e:
            print("exception\n")
            QMessageBox.information(self.loginwin, 'Error', str(e), QMessageBox.Ok)
            return

        print(host,port,self.username, self.password)
        try:
            self.clisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("socket success\n")
            self.clisock.connect((host, port))
            self.loginwin.close()   
            print("connect success\n")
            self.login()
              
            while True:
                self.receiveResponse()

        except:
            print("connnect error\n")
            QMessageBox.information(self.loginwin, 'Error', "Connection failed", QMessageBox.Ok)

    def closeEvent(self):
        self.clisock.close()

    def login(self):
        self.receiveResponse()
        senddata =  "USER" + ' ' + self.username + '\r\n'
        self.clisock.send(senddata.encode())
        self.receiveResponse()
        senddata =  "PASS" + ' ' + self.password + '\r\n'
        self.clisock.send(senddata.encode()) 
        self.receiveResponse()      

    def checkConnectInput(self):
        if self.username != "anonymous":
            QMessageBox.information(self.loginwin, 'Error', "Username should be 'anonymous'!", QMessageBox.Ok)
        if '@' not in self.password :
            QMessageBox.information(self.loginwin, 'Error', "Password should be e-mail address!", QMessageBox.Ok)

    def receiveResponse(self):
        msg = self.clisock.recv(SIZE).decode()
        print(msg)
        self.centralwin.serverresponselist.addItem(msg)

    def sendCommand(self):
        self.command = self.centralwin.conmandchoose.currentText()
        self.parameter = self.centralwin.parametertext.toPlainText()
        self.ChooseCMD.get(self.command)
        senddata = self.command + ' ' + self.parameter + '\r\n'
        self.clisock.send(senddata.encode())
    
    def cmd_USER(self):
        print("cmd_USER begin")
        return
    
    def cmd_PASS(self):
        return

    def cmd_PORT(self):
        self.clientIP = self.get_local_ip()
        self.clientDataPort = 25608
        self.parameter = self.clientIP.replace('.',',')+',100,8'
        self.clientDatafd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientDatafd.bind(('', self.clientDataPort))
        self.clientDatafd.listen(10)
        print("cmd_PORT ends\n")
        return
    
    def cmd_RETR(self):
        print("cmd_RETR begin\n")
        while True:
            # 接受一个新连接:
            self.sock, addr = self.clientDatafd.accept()
            print("accepted\n")
            #创建新线程来处理TCP连接:
            t = threading.Thread(target=self.downloadFile)
            t.start()

    def downloadFile(self):
        print('download begin\n')
        # filename = os.path.split(self.parameter)[1]
        filename = self.clientFilePath+'courses2.cpp'
        print(filename)
        f = open(filename, 'ab') 
        if not f:
            print("建立文件失败\n")
        position = 0
        print("建立文件成功\n")
        f.seek(0)
        print("seek文件成功\n")
        while True:
            data = self.sock.recv(SIZE)
            if not data:
                print("没接到")
                break
            print("接收文件廖\n")
            # time.sleep(0.05)
            f.write(data)
        f.close()
        self.sock.send('Goodbye!'.encode())

    def cmd_PASV(self):
        return
        #  file = open(absolute_path, mode='wb')
        # if not file:
        #     error_msg = "file open or create failure"
        #     self.response_signal.emit(error_msg)
        # if self.file_breakpoint > 0:
        #     file.seek(self.file_breakpoint, 0)
        # self.file_breakpoint = 0
        # while 1:
        #     if self.blocked:
        #         return
        #     file_buf = connect_socket.recv(FILE_SIZE)
        #     if len(file_buf) <= 0:
        #         self.file_breakpoint = 0
        #         self.transfer_file = ''
        #         self.retr_file_signal.emit(100)
        #         break
        #     self.file_breakpoint += len(file_buf)
        #     if len(file_buf) > 0:
        #         self.retr_file_signal.emit(self.file_breakpoint)
        #     file.write(file_buf)
    

        
    
    def cmd_STOR(self):
        return
    
    def cmd_QUIT(self):
        return
    
    def cmd_SYST(self):
        return
    
    def cmd_TYPE(self):
        return
    
    def cmd_MKD(self):
        return
    
    def cmd_CWD(self):
        return
    
    def cmd_PWD(self):
        return

    def cmd_LIST(self):
        return
    
    def cmd_RMD(self):
        return

    def cmd_RNFR(self):
        return

    def cmd_RNTO(self):
        return

    # def changeWindow(self):
    #     print("changeWindow begin\n")
    #     try:
    #         self.centralwin.show()
    #     except Exception as e:
    #         print("exception\n")
    #         QMessageBox.information(self.loginwin, 'Error', str(e), QMessageBox.Ok)

    def get_local_ip(self):
        local_ip = ''
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('8.8.8.8', 80))
            local_ip = s.getsockname()[0]
        except:
            local_ip.close()
        return local_ip




