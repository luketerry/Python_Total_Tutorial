#!/usr/bin/env python
#coding:utf-8
from __future__ import division, print_function
"""socket异常处理
"""
from socket import socket, traceback
from socket import AF_INET, SOCK_STREAM
from socket import SOL_SOCKET, SO_REUSEADDR
from socket import error, gaierror, herror, timeout

def main():
    host = ""
    port = 12345
    s = socket(AF_INET, SOCK_STREAM)#设定通信类型和
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
    s.bind((host,port))
    s.listen(1)
    
    while True:
        try:
            #块1
            clientsock,clientaddr = s.accept()
        except KeyboardInterrupt:
            raise
        except:
            traceback.print_exc()
            continue
        try:
            #块2
            print("链接来自:")
            print(clientsock.getpeername())
        except (KeyboardInterrupt,SystemExit):
            raise
        except:
            traceback.print_exc()
            
        try:
            #块3
            clientsock.close()
        except KeyboardInterrupt:
            raise
        except:
            traceback.print_exc()