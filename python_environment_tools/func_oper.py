#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""\
这里可以写用到多个函数的

>>> summing(multiply(2,3),multiply(2,3))
12

"""
from functools import reduce
from operator import mul,add

def multiply(*args):
    """\
    这里可以写单元测试
    >>> multiply(2,3)
    6
    >>> multiply('baka~',3)
    'baka~baka~baka~'
    """
    return reduce(mul,args)

def summing(*args):
    """\
    这里可以写单元测试
    >>> summing(2,3)
    5
    >>> summing(2,3,4)
    9
    """
    return reduce(add,args)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)