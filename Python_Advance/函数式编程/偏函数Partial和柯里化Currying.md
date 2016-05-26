
# 偏函数(Partial)和柯里化(Currying)

偏函数就是将一个多参数函数分解为多个单参数或少量参数函数的过程,而柯里化是将多个单参数或者少量参数函数合并为多参数函数的方法.这个过程一般来说是等价的

Python中没有独立的柯里化模块,但可以用标准库中的`functools`和`inspect`模块写一个装饰器来实现(代码来自于第三方模块`fn`)


```python
%%writefile curried.py

#coding:utf-8

from functools import wraps
from inspect import getargspec


def curry_n(n, func=None):
    """curry_n(n, func) returns a new function which takes any arguments,
    returning callables that take any arguments until n argumentss 
    have been applied. Accumulates kwargs until func is evaluated.
    >>> curried_max = curry_n(4, max)
    >>> curried_max(2)(3, 5)(4)
    5
    >>> @curry_n(2)
    ... def add(x, y):
    ...     return x + y
    >>> add3 = add(3)
    >>> add3(4)
    7
    """
    def curry_func(func):
        def accum_curry(args, kwargs, accum_args=(), accum_kwargs={}):
            accum_args = accum_args + args
            accum_kwargs.update(kwargs)

            if not (args or kwargs) or len(accum_args) >= n:
                return func(*accum_args, **accum_kwargs)
            else:
                return wraps(func)(lambda *a, **kw: accum_curry(a, kw, accum_args, accum_kwargs))

        @wraps(func)
        def curried_func(*args, **kwargs):
            return accum_curry(args, kwargs)

        return curried_func
    return curry_func(func) if func else curry_func


def curried(func):
    """Curries a function over the number of arguments it requires
    (which do not specify defaults). Optional arguments can be 
    passed at any point in curried application as keywords.
    >>> @curried
    ... def add(x, y, z=0):
    ...     return x + y + z
    >>> add(4)(5)
    9
    >>> add(4, z=3)(5)
    12
    >>> @curried
    ... def add_all(*nums):
    ...     return reduce(lambda x,y: x+y, nums)
    >>> add_all(1)(2)(3)(4)()
    10
    """
    """Curried functions that accept a variable number of arguments 
    (i.e. `*args`) need to be terminated by an empty call
    """
    argspec = getargspec(func)
    num_defaults = len(argspec.defaults) if argspec.defaults else 0
    num_required = len(argspec.args) - num_defaults
    num_curried = float('inf') if argspec.varargs else num_required

    return curry_n(num_curried)(func)


if __name__=="__main__":
    import doctest
    doctest.testmod()
```

    Overwriting curried.py



```python
%run curried.py
```


```python
from curried import curried
@curried
def sum5(a, b, c, d, e):
    return a + b + c + d + e
```


```python
sum5(1)(2)(3)(4)(5)
```




    15




```python
a = sum5(1)(2)(3)(4)
```


```python
a(5)
```




    15




```python
b = sum5(2,3,4)
```


```python
b(5,6)
```




    20




```python
b(5)(6)
```




    20




```python
bb=b(5)
```


```python
bb(6)
```




    20




```python
c=sum5(1)(2)(3)(e=5)
```


```python
c(d=4)()
```




    15




```python
d=sum5(1,2,3,e=5)
```


```python
d(d=4)()
```




    15




```python
@curried
def add_all(*nums):
    return reduce(lambda x,y: x+y, nums)
```


```python
add_all(1)(2)(3)(4)()
```


```python
@curried
def add(x, y, z=0):
    return x + y + z
add(4)(5)
```




    9




```python
add(4, z=3)(5)
```




    12




```python
adq=add(4, z=3)
```


```python
adq(5)
```




    12



当然了大多数时候没必要这么麻烦,用`functools.partial`就可以实现偏函数了


```python
import functools
```


```python
def add(x,y,z):
    return x+y+z*2
```


```python
add(1,2,3)
```




    9




```python
functools.partial(add,1)(2,3)
```




    9


