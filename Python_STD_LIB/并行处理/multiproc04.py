# --*--coding:utf-8 --*--
from __future__ import print_function
from multiprocessing import Process, Pipe
import os, time, random

# 写数据进程执行的代码:
def write(conn):
    value = ["h1 reader~"]
    print('Put %s to pip...' % value)
    conn.send(value)
    time.sleep(1)
    
# 读数据进程执行的代码:
def read(conn):
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    value = conn.recv()
    print('Get %s from pip.' % value)
    conn.send("hi writer~~")
    

if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    parent_conn, child_conn = Pipe()
    pw = Process(target=write, args=(parent_conn,))#起点
    pr = Process(target=read, args=(child_conn,))#终点
    # 启动子进程pw，写入:
    pw.start()    
    # 等待pw结束:
    pw.join()
    # 启动子进程pr，读取:
    pr.start()
    pr.join()
    print(parent_conn.recv())
    print('\n所有数据都写入并且读完')
