# --*--coding:utf-8 --*--
from __future__ import print_function
from multiprocessing import Process,Queue,Manager
import time
def f(q,k):
    q.put(sum(map(lambda x:x**2,k)))

if __name__=="__main__":
    value = range(1,10000001)
    proc = 4
    step = len(value)/proc
    slic= [value[:step+1],value[step+1:2*step+1],value[step+1:3*step+1],value[3*step+1:]]
    q = Queue()
    jobs = [ Process(target=f, args=(q, i))
             for i in slic
             ]
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    val = 0    
    while True:
        if not q.empty():
            val = val+q.get(True)
        else:
            break