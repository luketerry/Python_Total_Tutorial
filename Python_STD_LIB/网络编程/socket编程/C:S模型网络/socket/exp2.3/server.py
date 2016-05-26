#!/usr/bin/env python
#coding:utf-8
from __future__ import division, print_function
"""一个简单的Server
"""
from socket import socket,AF_INET,SOCK_STREAM ,SOL_SOCKET ,SO_REUSEADDR
import sys

def main():
    port = 51423
    host = ""

    s = socket(AF_INET,SOCK_STREAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind((host,port))
    s.listen(True)#表示开始监听端口了
    print("Server is running on port {port}.press Ctrl-C to terminate.".format(port = port))
    while True:
        #主循环,从accept()方法开始
        clientsock,clientaddr = s.accept()
        clientfile = clientsock.makefile("rw",0)
        clientfile.write("Welcom, "+ str(clientaddr)+"\n")
        clientfile.write("Please enter a string: ")
        line = clientfile.readline().strip()
        clientfile.write("Please entered {nbr} chars: ".format(nbr=len(line)))
        clientfile.close()#注意要关闭
        clientsock.close()
if __name__=="__main__":
    main()