# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CommandWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1295, 861)
        font = QtGui.QFont()
        font.setFamily("Samyak Malayalam")
        Form.setFont(font)
        self.scrollArea_2 = QtWidgets.QScrollArea(Form)
        self.scrollArea_2.setGeometry(QtCore.QRect(550, 60, 591, 311))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 589, 309))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 591, 311))
        font = QtGui.QFont()
        font.setFamily("Samyak Malayalam")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(147)
        self.tableWidget.verticalHeader().setDefaultSectionSize(34)
        self.tableWidget.verticalHeader().setMinimumSectionSize(31)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(550, 450, 591, 321))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 589, 319))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 591, 321))
        font = QtGui.QFont()
        font.setFamily("Samyak Malayalam")
        font.setPointSize(12)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(147)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.downloadbutton = QtWidgets.QPushButton(Form)
        self.downloadbutton.setGeometry(QtCore.QRect(1150, 160, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Yrsa Medium")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.downloadbutton.setFont(font)
        self.downloadbutton.setObjectName("downloadbutton")
        self.uploadbutton = QtWidgets.QPushButton(Form)
        self.uploadbutton.setGeometry(QtCore.QRect(1150, 570, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Yrsa Medium")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.uploadbutton.setFont(font)
        self.uploadbutton.setObjectName("uploadbutton")
        self.DLlabel = QtWidgets.QLabel(Form)
        self.DLlabel.setGeometry(QtCore.QRect(560, 20, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Samyak Malayalam")
        font.setPointSize(16)
        self.DLlabel.setFont(font)
        self.DLlabel.setObjectName("DLlabel")
        self.ULlabel = QtWidgets.QLabel(Form)
        self.ULlabel.setGeometry(QtCore.QRect(560, 410, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Samyak Malayalam")
        font.setPointSize(16)
        self.ULlabel.setFont(font)
        self.ULlabel.setObjectName("ULlabel")
        self.conmandchoose = QtWidgets.QComboBox(Form)
        self.conmandchoose.setGeometry(QtCore.QRect(140, 30, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Samyak Malayalam")
        font.setPointSize(16)
        self.conmandchoose.setFont(font)
        self.conmandchoose.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.conmandchoose.setObjectName("conmandchoose")
        self.conmandchoose.addItem("")
        self.conmandchoose.addItem("")
        self.conmandchoose.addItem("")
        self.conmandchoose.addItem("")
        self.conmandchoose.addItem("")
        self.conmandchoose.addItem("")
        self.conmandchoose.addItem("")
        self.conmandchoose.addItem("")
        self.conmandchoose.addItem("")
        self.conmandchoose.addItem("")
        self.conmandchoose.addItem("")
        self.conmandchoose.addItem("")
        self.conmandchoose.addItem("")
        self.conmandchoose.addItem("")
        self.Cmlabel = QtWidgets.QLabel(Form)
        self.Cmlabel.setGeometry(QtCore.QRect(20, 40, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Samyak Malayalam")
        font.setPointSize(14)
        self.Cmlabel.setFont(font)
        self.Cmlabel.setObjectName("Cmlabel")
        self.parametertext = QtWidgets.QTextEdit(Form)
        self.parametertext.setGeometry(QtCore.QRect(140, 120, 351, 61))
        self.parametertext.setObjectName("parametertext")
        self.PRlabel = QtWidgets.QLabel(Form)
        self.PRlabel.setGeometry(QtCore.QRect(20, 120, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Samyak Malayalam")
        font.setPointSize(14)
        self.PRlabel.setFont(font)
        self.PRlabel.setObjectName("PRlabel")
        self.SRlabel = QtWidgets.QLabel(Form)
        self.SRlabel.setGeometry(QtCore.QRect(20, 220, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Samyak Malayalam")
        font.setPointSize(14)
        self.SRlabel.setFont(font)
        self.SRlabel.setObjectName("SRlabel")
        self.serverresponselist = QtWidgets.QListWidget(Form)
        self.serverresponselist.setGeometry(QtCore.QRect(80, 280, 381, 491))
        self.serverresponselist.setObjectName("serverresponselist")
        self.sendbutton = QtWidgets.QPushButton(Form)
        self.sendbutton.setGeometry(QtCore.QRect(380, 30, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Yrsa Medium")
        font.setPointSize(17)
        self.sendbutton.setFont(font)
        self.sendbutton.setObjectName("sendbutton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "FIlename"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Type"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Size"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Download time"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Filename"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Type"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Size"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Upload Time"))
        self.downloadbutton.setText(_translate("Form", "Download File"))
        self.uploadbutton.setText(_translate("Form", "Upload File"))
        self.DLlabel.setText(_translate("Form", "Downloaded"))
        self.ULlabel.setText(_translate("Form", "Uploaded"))
        self.conmandchoose.setItemText(0, _translate("Form", "PORT"))
        self.conmandchoose.setItemText(1, _translate("Form", "PASV"))
        self.conmandchoose.setItemText(2, _translate("Form", "RETR"))
        self.conmandchoose.setItemText(3, _translate("Form", "STOR"))
        self.conmandchoose.setItemText(4, _translate("Form", "MKD"))
        self.conmandchoose.setItemText(5, _translate("Form", "CWD"))
        self.conmandchoose.setItemText(6, _translate("Form", "PWD"))
        self.conmandchoose.setItemText(7, _translate("Form", "LIST"))
        self.conmandchoose.setItemText(8, _translate("Form", "RMD"))
        self.conmandchoose.setItemText(9, _translate("Form", "RNFR"))
        self.conmandchoose.setItemText(10, _translate("Form", "RNTO"))
        self.conmandchoose.setItemText(11, _translate("Form", "SYST"))
        self.conmandchoose.setItemText(12, _translate("Form", "TYPE"))
        self.conmandchoose.setItemText(13, _translate("Form", "QUIT"))
        self.Cmlabel.setText(_translate("Form", "Command:"))
        self.PRlabel.setText(_translate("Form", "Parameter:"))
        self.SRlabel.setText(_translate("Form", "Server Response:"))
        self.sendbutton.setText(_translate("Form", "Send"))
