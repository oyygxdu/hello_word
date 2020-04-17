#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from functools import partial

import EthernetControl

import socket




def SwitchSelect(ui):
    ADDR = '192.168.6.133'
    PORT = 60000
    client = socket.socket()
    client.connect((ADDR, PORT))
    selectedKey = ui.buttonGroup.checkedButton()
    if selectedKey is  ui.btnOff:
        sendcmd = ':OUTP:SEL OFF'
        client.sendall(sendcmd.encode())
        revdata = client.recv(1024).decode()
        ui.textBrowser.append(revdata)
    elif selectedKey is ui.btnSw1:
        sendcmd = ':OUTP:SEL SW1'
        client.sendall(sendcmd.encode())
        revdata = client.recv(1024).decode()
        ui.textBrowser.append(revdata)
    elif selectedKey is ui.btnSw2:
        sendcmd = ':OUTP:SEL SW2'
        client.sendall(sendcmd.encode())
        revdata = client.recv(1024).decode()
        ui.textBrowser.append(revdata)
    elif selectedKey is ui.btnSw3:
        sendcmd = ':OUTP:SEL SW3'
        client.sendall(sendcmd.encode())
        revdata = client.recv(1024).decode()
        ui.textBrowser.append(revdata)
    elif selectedKey is ui.btnSw4:
        sendcmd = ':OUTP:SEL SW3'
        client.sendall(sendcmd.encode())
        revdata = client.recv(1024).decode()
        ui.textBrowser.append(revdata)
    elif selectedKey is ui.btnSw5:
        sendcmd = ':OUTP:SEL SW5'
        client.sendall(sendcmd.encode())
        revdata = client.recv(1024).decode()
        ui.textBrowser.append(revdata)
    elif selectedKey is ui.btnSw6:
        sendcmd = ':OUTP:SEL SW6'
        client.sendall(sendcmd.encode())
        revdata = client.recv(1024).decode()
        ui.textBrowser.append(revdata)
    else:
       print('error')

def ethConect(ui):
    ADDR = '192.168.6.133'
    PORT = 60000
    #global client
    client = socket.socket()
    client.connect((ADDR,PORT))
    sendcmd = ':OUTP:SEL OFF'
    client.sendall(sendcmd.encode())
    revdata = client.recv(1024).decode()
    ui.textBrowser.append(revdata)

if __name__ == "__main__":
    app =  QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = EthernetControl.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ####Add user Application here
    ui.buttonGroup.buttonClicked.connect(partial(SwitchSelect,ui))
    ui.btnConn.clicked.connect(partial(ethConect,ui))

    sys.exit(app.exec_())
