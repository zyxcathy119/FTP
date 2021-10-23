
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

    clisock = -1
    clientIP = ""
    clientControlPort = 8000
    clientDataPort = 8001
    clientDatafd = -1
    dataConnectfd = -1
    clientControlfd = -1
    clientFilePath ='/home/cathy/FTPCLIENT/'    

    serverControlIP = 'localhost' #服务器ip
    serverControlPort = 21    #服务器controlport
    serverDataIP = ''
    serverDataPort = 20

    isSignin = False
    isPass = False
    isStop = False
    dataMode = 0 # PORT = 1,PASV = 2
    isPasvrecieved = False #server是否发过来了Ip和port
    username = ''
    password = ''
    command = ''
    parameter = ''
    resvmsg = ''
    code = ''
    text = ''
    filepath = ''
    threadcount = 0
    threads = []


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
        self.initSocket(self.serverControlIP,self.serverControlPort)

    def initSocket(self,host, port):
        try:
            self.clientControlfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.clientControlfd.connect((host, port))
            # 收
            t=threading.Thread(target = self.receiveResponse)
            self.threads.append(t)
            self.threadcount = self.threadcount+1
            t.start()
            while True:
                #   print(clisock.recv(size).decode())
                # if not self.isStop:
                    # self.resvmsg = clisock.recv(SIZE).decode()
                    # if not self.resvmsg:
                    #     break
                    # self.dealToRecv()
                    # print(self.resvmsg)

                    self.command = input("command: ")
                    self.parameter = input("parameter: ")
                    # self.chooseCMD.get(command)
                    if self.command is "PORT":
                        self.parameter = "183,173,67,177,100,6"
                    data = self.command+' '+self.parameter + '\r\n'
                    print("send:",data)
                    self.clientControlfd.send(data.encode())
                    self.dealToCommand()

            clisock.close()
        except Exception as e:
            self.clientControlfd.send('exit\r\n'.encode())
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

    def dealToRecv(self):
        rsv = self.resvmsg.split()
        self.code = rsv[0]
        self.text = rsv[1]

    def dealToCommand(self):
        if self.command == 'PORT':
            self.cmd_PORT()
            return
        
        if self.command == 'PASV':
            self.cmd_PASV()
            return
        
        if self.command == 'RETR':
            self.filepath = self.parameter
            self.cmd_RETR()
            # self.threads.append(t)
            # self.threadcount = self.threadcount+1
            # t.start()
            return
        
        if self.command == 'STOR':
            self.filepath = self.parameter
            self.cmd_STOR()       
            return

        if self.command == 'CWD':
            # self.cmd_PORT()
            return

    def cmd_PORT(self):
        try:
            self.clientIP = self.get_local_ip()
            self.clientDataPort = 25606
            self.parameter = self.clientIP.replace('.',',')+',100,6' #把客户端ip发给服务器
            self.clientDatafd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.clientDatafd.bind(('', self.clientDataPort)) #0.0.0.0接收所有
            self.clientDatafd.listen(10)
            print("cmd_PORT ends\n")
            self.dataMode = 1
        except Exception as e:
            print(str(e))

        return

    def cmd_PASV(self):
        while True:
            if self.code == "227":
                print("接受到PASV端口信息\n")
                try:
                    self.text.replace('\n', '').replace('\r', '').replace('=', '')
                    li = self.text.split(',')
                    self.serverDataIP = li[0]+'.'+li[1]+'.'+li[2]+'.'+li[3]
                    self.serverDataPort = int(li[4])*256 + int(li[5])
                    print("ip:", self.serverDataIP,"port:",self.serverDataPort)
                    self.dataMode = 2
                    break
                except Exception as e:
                    print(str(e))
                    break 
    
    def cmd_RETR(self):
        print("cmd_RETR begin\n")
        try:
            if self.dataMode is 1:
               # 接受一个新连接:
                self.dataConnectfd, addr = self.clientDatafd.accept()
            elif self.dataMode is 2:
                print("in to mode 2\n")
                self.dataConnectfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.dataConnectfd.connect(('localhost', self.serverDataPort))###
                print("connected\n")
            else:
                return
            print("accepted\n")
            self.downloadFile()
            self.dataConnectfd.close()
        except Exception as e:
            print(str(e))

    def cmd_STOR(self):
        # 接受一个新连接:
        try:
            if self.dataMode is 1:
               # 接受一个新连接:
                self.dataConnectfd, addr = self.clientDatafd.accept()
            elif self.dataMode is 2:
                self.dataConnectfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.dataConnectfd.connect(('localhost', self.serverDataPort))
            else:
                return
            print("accepted\n")
            self.uploadFile()
            print("cmd_STOR end\n")
            self.dataConnectfd.close()
        except Exception as e:
            print(str(e))

    def downloadFile(self):
        print('download begin\n')
        # filename = os.path.split(self.parameter)[1]
        filename = self.clientFilePath+self.filepath
        print(filename)

        f = open(filename, 'wb+') 
        f.seek(0)
        while True:
            data = self.dataConnectfd.recv(SIZE)
            if not data:
                print("没接到")
                break
            # time.sleep(0.05)
            f.write(data)
            print("接收文件廖\n")
            if len(data) < SIZE:
                break
        f.close()


    def uploadFile(self):
        print('upload begin\n')
        filename = self.clientFilePath+self.filepath
        print(filename)
        try:
            f = open(filename, 'rb+') 
        except:
            print("搜索文件失败\n")
            return
        print("搜索文件成功\n")
        f.seek(0)
        fsize = os.path.getsize(filename)
        print("seek文件成功\n")
        while True:
            data = f.read(SIZE)
            if not data:
                break
            self.dataConnectfd.send(data)
            print("发送文件廖\n")
            time.sleep(0.002)
        f.close()
        print("文件读取结束，已经关闭\n")

    # def connectToServer(self):
    #     print("connectToserver begin\n")
    #     host = 'localhost'
    #     port = 21
    #     self.username = 'anonymous'
    #     self.password = 'cathy@com'
    #     try:
    #         # host = self.loginwin.ServerIPtext.toPlainText()
    #         # port = int(self.loginwin.ServerPorttext.toPlainText())
    #         # self.username = self.loginwin.Usernametext.toPlainText()
    #         # self.password = self.loginwin.Passwordtext.toPlainText()
    #         self.checkConnectInput()
    #     except Exception as e:
    #         print("exception\n")
    #         QMessageBox.information(self.loginwin, 'Error', str(e), QMessageBox.Ok)
    #         return

    #     print(host,port,self.username, self.password)
    #     try:
    #         self.clientControlfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #         print("socket success\n")
    #         self.clientControlfd.connect((host, port))
    #         self.loginwin.close()   
    #         print("connect success\n")
    #         self.login()
              
    #         while True:
    #             self.receiveResponse()

    #     except:
    #         print("connnect error\n")
    #         QMessageBox.information(self.loginwin, 'Error', "Connection failed", QMessageBox.Ok)

    # def closeEvent(self):
    #     self.clientControlfd.close()

    # def login(self):
    #     self.receiveResponse()
    #     senddata =  "USER" + ' ' + self.username + '\r\n'
    #     self.clientControlfd.send(senddata.encode())
    #     self.receiveResponse()
    #     senddata =  "PASS" + ' ' + self.password + '\r\n'
    #     self.clientControlfd.send(senddata.encode()) 
    #     self.receiveResponse()      

    # def checkConnectInput(self):
    #     if self.username != "anonymous":
    #         QMessageBox.information(self.loginwin, 'Error', "Username should be 'anonymous'!", QMessageBox.Ok)
    #     if '@' not in self.password :
    #         QMessageBox.information(self.loginwin, 'Error', "Password should be e-mail address!", QMessageBox.Ok)

    def receiveResponse(self):
        while True:
            self.resvmsg = self.clientControlfd.recv(SIZE).decode()
            self.dealToRecv()
            if not self.resvmsg:
                break
            print(self.resvmsg)
        # self.centralwin.serverresponselist.addItem(msg)

    # def sendCommand(self):
    #     self.command = self.centralwin.conmandchoose.currentText()
    #     self.parameter = self.centralwin.parametertext.toPlainText()
    #     self.ChooseCMD.get(self.command)
    #     senddata = self.command + ' ' + self.parameter + '\r\n'
    #     self.clientControlfd.send(senddata.encode())
    
    def cmd_USER(self):

        return
    
    def cmd_PASS(self):
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




