
## 说明文档测试模块(doctest)

doctest 并不是测试文档用的测试,而是用文档测试代码,听上去蛮酷的~

doctest 模块会搜索那些看起来像交互式会话的 Python 代码片段，然后尝试执行并验证结果

doctest 的编写过程就仿佛你真的在一个交互式 shell（比如 idle）中导入了要测试的模块，然后开始一条条地测试模块里的函数一样。实际上有很多人也是这么做的，他们写好一个模块后，就在 shell 里挨个测试函数，最后把 shell 会话复制粘贴成 doctest 用例。 


> 一个简单的例子:


```python
%%writefile func_oper.py
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

def  summing(*args):
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
```

    Writing func_oper.py



```python
%run func_oper.py
```

    Trying:
        summing(multiply(2,3),multiply(2,3))
    Expecting:
        12
    ok
    Trying:
        multiply(2,3)
    Expecting:
        6
    ok
    Trying:
        multiply('baka~',3)
    Expecting:
        'baka~baka~baka~'
    ok
    Trying:
        summing(2,3)
    Expecting:
        5
    ok
    Trying:
        summing(2,3,4)
    Expecting:
        9
    ok
    3 items passed all tests:
       1 tests in __main__
       2 tests in __main__.multiply
       2 tests in __main__.summing
    5 tests in 3 items.
    5 passed and 0 failed.
    Test passed.


    if __name__ == '__main__':
        import doctest
        doctest.testmod(verbose=True)

这种方式很适合在写简单模块包的时候用,因为模块都是引用来用的.


```python
!python -m doctest -v func_oper.py
```

    Trying:
        summing(multiply(2,3),multiply(2,3))
    Expecting:
        12
    ok
    Trying:
        multiply(2,3)
    Expecting:
        6
    ok
    Trying:
        multiply('baka~',3)
    Expecting:
        'baka~baka~baka~'
    ok
    Trying:
        summing(2,3)
    Expecting:
        5
    ok
    Trying:
        summing(2,3,4)
    Expecting:
        9
    ok
    3 items passed all tests:
       1 tests in func_oper
       2 tests in func_oper.multiply
       2 tests in func_oper.summing
    5 tests in 3 items.
    5 passed and 0 failed.
    Test passed.


这种方式启动测试就不用在写

    if __name__ == '__main__':
        import doctest
        doctest.testmod(verbose=True)
        
这段了,效果也是一样

doctest也可以在文件外写测试,但这么搞就有点本末倒置了,因此这边就不写了
