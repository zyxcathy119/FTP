# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(978, 445)
        font = QtGui.QFont()
        font.setPointSize(14)
        LoginWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Usernametext = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Usernametext.setGeometry(QtCore.QRect(630, 80, 321, 61))
        self.Usernametext.setObjectName("Usernametext")
        self.Passwordtext = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Passwordtext.setGeometry(QtCore.QRect(630, 190, 321, 61))
        self.Passwordtext.setObjectName("Passwordtext")
        self.SignInbutton = QtWidgets.QPushButton(self.centralwidget)
        self.SignInbutton.setGeometry(QtCore.QRect(450, 310, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Noto Serif CJK TC")
        font.setPointSize(14)
        self.SignInbutton.setFont(font)
        self.SignInbutton.setObjectName("SignInbutton")
        self.Username = QtWidgets.QLabel(self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(500, 90, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Username.setFont(font)
        self.Username.setObjectName("Username")
        self.Passwordlabel = QtWidgets.QLabel(self.centralwidget)
        self.Passwordlabel.setGeometry(QtCore.QRect(500, 200, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Passwordlabel.setFont(font)
        self.Passwordlabel.setObjectName("Passwordlabel")
        self.ServerPorttext = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ServerPorttext.setGeometry(QtCore.QRect(150, 190, 321, 61))
        self.ServerPorttext.setObjectName("ServerPorttext")
        self.ServerIPtext = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ServerIPtext.setGeometry(QtCore.QRect(150, 80, 321, 61))
        self.ServerIPtext.setObjectName("ServerIPtext")
        self.ServerPortlabel = QtWidgets.QLabel(self.centralwidget)
        self.ServerPortlabel.setGeometry(QtCore.QRect(20, 200, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ServerPortlabel.setFont(font)
        self.ServerPortlabel.setObjectName("ServerPortlabel")
        self.ServerIPlabel = QtWidgets.QLabel(self.centralwidget)
        self.ServerIPlabel.setGeometry(QtCore.QRect(30, 90, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ServerIPlabel.setFont(font)
        self.ServerIPlabel.setObjectName("ServerIPlabel")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 978, 28))
        self.menubar.setObjectName("menubar")
        self.menuLogin = QtWidgets.QMenu(self.menubar)
        self.menuLogin.setObjectName("menuLogin")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuLogin.menuAction())

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.SignInbutton.setText(_translate("LoginWindow", "Sign In"))
        self.Username.setText(_translate("LoginWindow", "Username"))
        self.Passwordlabel.setText(_translate("LoginWindow", "Password"))
        self.ServerPortlabel.setText(_translate("LoginWindow", "ServerPort"))
        self.ServerIPlabel.setText(_translate("LoginWindow", "ServerIP"))
        self.menuLogin.setTitle(_translate("LoginWindow", "Login"))
