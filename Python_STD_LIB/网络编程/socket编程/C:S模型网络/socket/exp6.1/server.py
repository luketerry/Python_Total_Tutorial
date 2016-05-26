#!/usr/bin/env python
#coding:utf-8

"""UDP昨日时间服务器"""
from socket import socket
from socket import AF_INET, SOCK_DGRAM
from socket import SOL_SOCKET, SO_REUSEADDR
import time
import struct
import traceback


host = ""
port = 12345

# 步骤一
s = socket(AF_INET, SOCK_DGRAM)#设定通信类型和

# 步骤二
s.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)

# 步骤三
s.bind((host,port))
print("等待连接")

while True:
    try:
        msg,addr = s.recvfrom(8192)
        print("连接来自")
        print(addr)
        #实现时间功能
        secs = int(time.time())
        secs -= 60*60*24
        secs += 2208988800
        reply = struct.pack("!I",secs)
        #实现时间功能结束
        print("准备返回发送")
        s.sendto(reply,addr)
        print("发送结束")
    except (KeyboardInterrupt,SystemExit):
        raise
    except:
        traceback.print_exc()