
# 调试工具模块(pdb)

pdb是python自带的调试模块,它可以在交互环境中使用,也可以在terminal中作为python的一个模式使用

> 要调试的脚本:


```python
%%writefile counter.py
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

```

> 命令行调试

    python -m pdb counter.py
    
在jupyter中无法演示,请自己试试

> 在交互shell中调试

    import pdb
    import counter
    pdb.run('counter.test()')

> 常用的调试命令

可以用help命令来查看

> 在ipython中调用pdb

ipython内置了魔法命令`%pdb`可以在程序出错的时候自动跳入debug


```python
%pdb
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
assert test.value == 1 
```

    Automatic pdb calling has been turned ON
    state:2



    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-4-16cc623a427d> in <module>()
         33 test()
         34 print(test)
    ---> 35 assert test.value == 1
    

    AssertionError: 


    > [0;32m<ipython-input-4-16cc623a427d>[0m(35)[0;36m<module>[0;34m()[0m
    [0;32m     33 [0;31m[0mtest[0m[0;34m([0m[0;34m)[0m[0;34m[0m[0m
    [0m[0;32m     34 [0;31m[0mprint[0m[0;34m([0m[0mtest[0m[0;34m)[0m[0;34m[0m[0m
    [0m[0;32m---> 35 [0;31m[0;32massert[0m [0mtest[0m[0;34m.[0m[0mvalue[0m [0;34m==[0m [0;36m1[0m[0;34m[0m[0m
    [0m
    --KeyboardInterrupt--
    ipdb> h
    
    Documented commands (type help <topic>):
    ========================================
    EOF    c          d        h         next    pp       retval  u          whatis
    a      cl         debug    help      p       psource  run     unalias    where 
    alias  clear      disable  ignore    pdef    q        rv      undisplay
    args   commands   display  interact  pdoc    quit     s       unt      
    b      condition  down     j         pfile   r        source  until    
    break  cont       enable   jump      pinfo   restart  step    up       
    bt     continue   exit     n         pinfo2  return   tbreak  w        
    
    Miscellaneous help topics:
    ==========================
    exec  pdb
    
    Undocumented commands:
    ======================
    l  list  ll  longlist
    
    ipdb> EOF
    

