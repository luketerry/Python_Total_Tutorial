#!/usr/bin/env python
#coding:utf-8

"""基本的服务器"""
from socket import socket
from socket import AF_INET, SOCK_STREAM
from socket import SOL_SOCKET, SO_REUSEADDR

host = ""
port = 12345

# 步骤一
s = socket(AF_INET, SOCK_STREAM)#设定通信类型和

# 步骤二
s.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)

# 步骤三
s.bind((host,port))
print("等待连接")
# 步骤四
s.listen(5)
while True:
    clientsock,clientaddr = s.accept()
    print("连接来自")
    print(clientsock.getpeername())
    clientsock.close()