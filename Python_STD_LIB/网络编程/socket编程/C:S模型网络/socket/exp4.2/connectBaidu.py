#!/usr/bin/env python
#coding:utf-8
from __future__ import division, print_function
"""连上百度服务器
"""
from socket import socket,AF_INET,SOCK_STREAM, getservbyname,error

def main():
    print("创建socket...")
    s = socket(AF_INET,SOCK_STREAM)
    print("创建成功!")
    print("获取端口号...")
    port = getservbyname("http","tcp")
    print("端口号为{port}".format(port = port))
    print("创建成功!")
    print("连接到百度...")
    try:
        s.connect(("www.baidu.com",80))
    except error as e:
        print("连接失败!")
        print(e)
    print("连接成功!")
if __name__=="__main__":
    main()