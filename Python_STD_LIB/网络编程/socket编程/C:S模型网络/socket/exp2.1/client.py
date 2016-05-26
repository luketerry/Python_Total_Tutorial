#!/usr/bin/env python
#coding:utf-8
from __future__ import division, print_function
"""一个简单的Gopher信息查找服务的客户端
"""
from socket import socket,AF_INET,SOCK_STREAM ,error
import sys

def main():
    port = 70
    host = sys.argv[1]
    filename = sys.argv[2]
    s = socket(AF_INET,SOCK_STREAM)
    try:
        s.connect((host,port))

    except error as e:
        print(e)
        sys.exit(1)
    s.sendall(filename + "\r\n")
    while True:
        buf = s.recv(2048)
        if not len(buf):
            break
        sys.stdout.write(buf)
        
if __name__=="__main__":
    main()