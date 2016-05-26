# --*--coding:utf-8 --*--
from __future__ import print_function
from multiprocessing import Process
import os

#子进程要执行的代码
def run_proc(name):
    for i in range(3):
        print(u'子进程 %s (%s)...' % (name, os.getpid()))
    print(u'子进程结束.')
    
if __name__=='__main__':
    print(u'父进程 %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print(u'子进程要开始啦.')
    p.start()
    for i in range(3):
        print(u'父进程{pid}进行中...'.format(pid = os.getpid()))
    p.join()
    print(u"父进程结束啦")
    