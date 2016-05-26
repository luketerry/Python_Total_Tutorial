#!/usr/bin/env python
#coding:utf-8
from __future__ import division, print_function
"""socket异常处理
"""
from socket import socket, getservbyname
from socket import AF_INET, SOCK_STREAM
from socket import error, gaierror, herror, timeout
import sys
import time

def create():
    try:
        s = socket(AF_INET,SOCK_STREAM)
    except error as e:
        print("创建错误")
        print(e)
    return s

def find_port(textport):
    try:
        port = int(textport)
    except ValueError :
        try:
            port = getservbyname(textport,"tcp")
        except error as e:
            print("找不到端口: ",e)
            sys.exit(1)
    return port

def connect(s,host,port):
    try:
        s.connect((host,port))
    except gaierror as e:
        print("地址错误: ",e)
        sys.exit(1)
    except error as e:
        print("连接错误: ",e)
        sys.exit(1)
    return s
   
def sleep(t):
    print("sleeping...")
    time.sleep(t)
    print("continue...")
def send(s,filename):
    try:
        s.sendall("GET {filename} HTTP/1.0\r\n\r\n".format(filename = filename))
    except error as e:
        print("发送错误: ",e)
        sys.exit(1)
    return s

def shutdown(s):
    try:
        s.shutdown(1)
    except error as e:
        print("关闭错误",e)
        sys.exit(1)
    return s


def recive(s):
    try:
        buf = s.recv(2048)
    except error as e:
        print("接收错误: ",e)
        sys.exit(1)
    return buf


def main():
    host = sys.argv[1]
    textport = sys.argv[2]
    filename = sys.argv[3]
    s = create()
    port = find_port(textport)
    s = connect(s,host,port)
    sleep(10)
    s = send(s,filename)    

    while True:
        buf = recive(s)
        if not len(buf):
            break
        sys.stdout.write(buf)
    
if __name__=="__main__":
    main()