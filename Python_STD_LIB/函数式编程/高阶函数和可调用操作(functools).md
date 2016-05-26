
# 高阶函数和可调用操作(functools)

该模块提供几个高阶函数和可调用操作

+ `cmp_to_key(func)`key值比较函数
+ `total_ordering(cls)[装饰器]`自动补完比较运算符
+ `reduce(function,iterable[,initializer])`归约
+ `partial(func, *args, **keywords)`偏函数
+ `update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)`函数属性交换
+ `wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)[装饰器]`函数属性交换


```python
from functools import *
from __future__ import print_function
```

## `cmp_to_key`

这个函数并不常用.3.0中`sorted`方法取消了cmp参数,这个函数是拿来过度用的


```python
def cmp_to_key(mycmp): #【从2.x到3.x移植程序时需要用到】
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K
```


```python
def reverse_numeric(x, y):
    return y - x
```


```python
sorted([5, 2, 4, 1, 3], key=cmp_to_key(reverse_numeric))
```




    [5, 4, 3, 2, 1]



## `total_ordering(cls)[装饰器]`自动补完比较运算符

这个装饰器只给类定义时用,只要在类中定义了一个比较用的运算符(`__lt__()`, `__le__()`, `__gt__()`, or `__ge__()`)那就可以把其他的自动补完.

> 例:官方例子


```python
@total_ordering
class Student(object):
    def __eq__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))
    def __lt__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))
    def __init__(self,lastname,firstname):
        self.lastname = lastname
        self.firstname = firstname
```


```python
a = Student("Jhon","Daffy")
b = Student("Anlly","Queen")
a>b
```




    True



## `reduce(function,iterable[,initializer])` 归约

"map reduce"中的reduce,也就是规约,从左到右地一个一个的操作,可以有一个初始值

>例子 求积


```python
reduce(lambda x,y:x*y,range(1,10))
```




    362880



## `partial(func, *args, **keywords)`偏函数

偏函数和柯里化是函数式编程中常见的技术,这俩有联系有区别

partial 通过包装手法，允许我们 "重新定义" 函数签名,用一些默认参数包装一个可调用对象,返回结果是可调用对象，并且可以像原始对象一样对待
冻结部分函数位置函数或关键字参数，简化函数,更少更灵活的函数参数调用

> 例 求加法


```python
def add(x,y,z):
    return x+y+z*2
    
```


```python
add(1,2,3)
```




    9




```python
partial(add,1)(2,3)
```




    9




```python
partial(add,1,2)(3)
```




    9




```python
partial(add,z=3)(1,2)
```




    9



这个可以理解成是柯里化的一个比较丑陋的实现方式,但标准库往往是最好用的.

## `update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)`

默认partial对象或者那些被装饰器包裹的可调用对象没有__name__和__doc__, 这种情况下，对于装饰器函数非常难以debug.使用update_wrapper(),从原始对象拷贝或加入现有对象



> 看一个计时器的例子


```python
from functools import update_wrapper

def timeit_(func):
    def wrapper():
        start = time.clock()
        func()
        end =time.clock()
        print('used:', end - start)
    return update_wrapper(wrapper,func)
@timeit_
def hello2():
    """test hello"""
    print('hello world2')


hello2()
print(hello2.__name__)
print(hello2.__doc__)

```

    hello world2
    used: 2.3000000000550358e-05
    hello2
    test hello


## `wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)[装饰器]`函数属性交换

调用函数装饰器partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)的简写


```python
import time
def timeit_withoutname(func):
    def wrapper():
        start = time.clock()
        func()
        end =time.clock()
        print('used:', end - start)
    return wrapper
def timeit(func):
    @wraps(func)
    def wrapper():
        start = time.clock()
        func()
        end =time.clock()
        print('used:', end - start)
    return wrapper
```


```python
@timeit
def foo():
    print('in foo()')
 
foo()
print(foo.__name__)

@timeit_withoutname
def bar():
    print('in bar()')
 
bar()
print(bar.__name__)
```

    in foo()
    used: 2.1000000000270802e-05
    foo
    in bar()
    used: 9.000000000369823e-06
    wrapper


可以看出`wraps`装饰器替换了原函数和wrapper的内置属性,或者说把他俩整个替换掉了.另外相信你也注意到了，这个装饰器竟然带有一个参数。实际上，他还有另外两个可选的参数，assigned中的属性名将使用赋值的方式替换，而updated中的属性名将使用update的方式合并，你可以通过查看functools的源代码获得它们的默认值。对于这个装饰器，相当于wrapper = functools.wraps(func)(wrapper)。
