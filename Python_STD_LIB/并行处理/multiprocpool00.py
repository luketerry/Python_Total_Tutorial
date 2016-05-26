# --*--coding:utf-8 --*--
from __future__ import print_function
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('运行任务 %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('任务 %s 执行了 %0.2f 秒.' % (name, (end - start)))

if __name__=='__main__':
    print('父进程 %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))#创建非阻塞子进程用这个
    print('等待所有子进程完成...')
    p.close()
    p.join()
    print('所有子进程完成了.')