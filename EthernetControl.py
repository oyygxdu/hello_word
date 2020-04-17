# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EthernetControl.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(528, 328)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(240, 20, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 220, 191, 31))
        self.label.setObjectName("label")
        self.btnOff = QtWidgets.QRadioButton(self.centralwidget)
        self.btnOff.setGeometry(QtCore.QRect(20, 150, 99, 21))
        self.btnOff.setObjectName("btnOff")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.btnOff)
        self.btnSw5 = QtWidgets.QRadioButton(self.centralwidget)
        self.btnSw5.setGeometry(QtCore.QRect(20, 110, 141, 21))
        self.btnSw5.setObjectName("btnSw5")
        self.buttonGroup.addButton(self.btnSw5)
        self.btnSw3 = QtWidgets.QRadioButton(self.centralwidget)
        self.btnSw3.setGeometry(QtCore.QRect(20, 70, 171, 21))
        self.btnSw3.setObjectName("btnSw3")
        self.buttonGroup.addButton(self.btnSw3)
        self.btnSw6 = QtWidgets.QRadioButton(self.centralwidget)
        self.btnSw6.setGeometry(QtCore.QRect(20, 130, 151, 21))
        self.btnSw6.setObjectName("btnSw6")
        self.buttonGroup.addButton(self.btnSw6)
        self.btnSw2 = QtWidgets.QRadioButton(self.centralwidget)
        self.btnSw2.setGeometry(QtCore.QRect(20, 50, 171, 21))
        self.btnSw2.setObjectName("btnSw2")
        self.buttonGroup.addButton(self.btnSw2)
        self.btnSw1 = QtWidgets.QRadioButton(self.centralwidget)
        self.btnSw1.setGeometry(QtCore.QRect(20, 30, 151, 21))
        self.btnSw1.setObjectName("btnSw1")
        self.buttonGroup.addButton(self.btnSw1)
        self.btnSw4 = QtWidgets.QRadioButton(self.centralwidget)
        self.btnSw4.setGeometry(QtCore.QRect(20, 90, 161, 21))
        self.btnSw4.setObjectName("btnSw4")
        self.buttonGroup.addButton(self.btnSw4)
        self.btnConn = QtWidgets.QPushButton(self.centralwidget)
        self.btnConn.setGeometry(QtCore.QRect(240, 230, 75, 23))
        self.btnConn.setObjectName("btnConn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 528, 23))
        self.menubar.setObjectName("menubar")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.menuExit.addAction(self.actionExit)
        self.menuExit.addAction(self.actionVersion)
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RF Channel Control"))
        self.label.setText(_translate("MainWindow", "ServerIP:192.168.1.100 : 60000"))
        self.btnOff.setText(_translate("MainWindow", "OFF"))
        self.btnSw5.setText(_translate("MainWindow", "SW5:18-26.5GHz"))
        self.btnSw3.setText(_translate("MainWindow", "SW3:2-6GHz"))
        self.btnSw6.setText(_translate("MainWindow", "SW6:26.5-40GHz"))
        self.btnSw2.setText(_translate("MainWindow", "SW2:0.02-2GHz Right"))
        self.btnSw1.setText(_translate("MainWindow", "SW1:0.02-2GHz Left"))
        self.btnSw4.setText(_translate("MainWindow", "SW4:6-18GHz"))
        self.btnConn.setText(_translate("MainWindow", "Connect"))
        self.menuExit.setTitle(_translate("MainWindow", "System"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionVersion.setText(_translate("MainWindow", "Version"))
