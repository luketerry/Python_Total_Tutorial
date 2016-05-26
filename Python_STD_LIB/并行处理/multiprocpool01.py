# --*--coding:utf-8 --*--
from __future__ import print_function
from multiprocessing import Pool
from time import sleep

def f(x):
    return x*x

if __name__ == '__main__':
    # start 4 worker processes
    pool = Pool(processes=4)
    print("map: ",pool.map(f, range(10)))
    print("imap:")
    for i in pool.imap_unordered(f, range(10)):
        print(i)

    # evaluate "f(10)" asynchronously
    res = pool.apply_async(f, [10])
    print("apply:",res.get(timeout=1))             # prints "100"

    # make worker sleep for 10 secs
    res = pool.apply_async(sleep, [10])
    print(res.get(timeout=1))             # raises multiprocessing.TimeoutError