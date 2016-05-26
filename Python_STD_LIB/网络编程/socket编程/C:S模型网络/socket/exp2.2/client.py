#!/usr/bin/env python
#coding:utf-8
from __future__ import division, print_function
"""一个简单的Gopher信息查找服务的客户端,但用文件操作
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
    fd = s.makefile("rw",0)
    fd.write(filename+"\人\n")
    for line in fd.readlines():
        sys.stdout.write(line)
        
if __name__=="__main__":
    main()