#!/usr/bin/env python
#coding:utf-8

"""UDP昨日时间服务器,有log文档"""
from socket import socket,gethostbyaddr,getaddrinfo
from socket import AF_INET, SOCK_DGRAM
from socket import SOL_SOCKET, SO_REUSEADDR
import time
import struct
import traceback
import logging
logging.basicConfig(
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='udpserver.log',
                filemode='w', level=logging.INFO)

host = ""
port = 12345

# 步骤一
s = socket(AF_INET, SOCK_DGRAM)#设定通信类型和

# 步骤二
s.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)

# 步骤三
s.bind((host,port))
logging.info("等待连接")

def difhost(fromhost,addr):
    idfips = getaddrinfo(fromhost[0],None)
        #返回值为(family,socktype,proto,canonname,sockaddr)
    ips = [i[4][0] for i in idfips]
    if addr[0] in ips:
        return True
    else:
        return False

while True:
    try:
        msg,addr = s.recvfrom(8192)
        fromhost = gethostbyaddr(addr[0])
        logging.info("连接来自")
        if difhost(fromhost,addr):
            logging.info(fromhost[0]+str(addr))
        else:
            logging.info("unknow"+str(addr))
        #实现时间功能
        secs = int(time.time())
        secs -= 60*60*24
        secs += 2208988800
        reply = struct.pack("!I",secs)
        #实现时间功能结束
        logging.info("准备返回发送")
        s.sendto(reply,addr)
        logging.info("发送结束")
    except (KeyboardInterrupt,SystemExit):
        raise
    except:
        traceback.print_exc()