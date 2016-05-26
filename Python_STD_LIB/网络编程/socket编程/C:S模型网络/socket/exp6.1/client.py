#!/usr/bin/env python
#coding:utf-8

"""UDP昨日时间客户端"""
from socket import socket,getservbyname
from socket import AF_INET, SOCK_DGRAM
from socket import SOL_SOCKET, SO_REUSEADDR
import time
import struct
import traceback
import sys

host = ""
textport = 12345

# 步骤一
s = socket(AF_INET, SOCK_DGRAM)#设定通信类型和

# 步骤二
try:
    port = int(textport)
except ValueError:
    port = getservbyname(textport,'udp')
s.connect((host,port))
#print("输入要发送的日期")

#data = sys.stdin.readline().strip()
data = raw_input("输入要发送的日期").strip()
s.sendall(data)
print("等待回复,按CTRL-C或者CTRl-BREAK结束")
buf = s.recvfrom(2048)[0]
if len(buf) != 4:
    print("错误的长度{a}:{b}".format(a = len(buf),b = buf))
    sys.exit(1)
print time.ctime(int(struct.unpack("!I",buf)[0]-2208988800))