#!/usr/bin/env python
# --*-- coding:utf-8 --*--
from __future__ import print_function

class Counter(object):
    """一个计数器
    用法:
    >>> counter1 = Counter()
    >>> counter1()
    1
    >>> counter1()
    2
    >>> counter2 = Counter(lambda : 2,-3)
    >>> counter2()
    -1
    >>> counter2()
    1
    """
    def __str__(self):
        return "state:"+str(self.value)
    def __repr__(self):
        return self.__str__
    def __call__(self):
        def count():
            self.value += self.func()
            return self.value
        return count()
    
    def __init__(self,func=lambda : 1,start=0):
        self.value = start
        self.func = func 
test = Counter()
test()
test()
print(test)
if __name__=="__main__":
    counter1 = Counter()
    counter2 = Counter()
    for i in range(10):
        counter1()
    for i in range(8):
        counter2()
    if counter1.value == counter2.value:
        print("not success")
    else: 
        print("don't known")
        
    
    import doctest
    doctest.testmod(verbose=True)