# --*--coding:utf-8 --*--
from __future__ import print_function
from multiprocessing import Pool
import time
def f(x):
    return x**2

if __name__=="__main__":
    pool = Pool(processes=4)
    result = pool.map_async(f,xrange(1,10000001), )
    pool.close()
    pool.join()
    print(sum(result.get()))