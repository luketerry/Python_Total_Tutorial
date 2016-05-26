
[cython](http://docs.cython.org/src/tutorial/cython_tutorial.html#fibonacci-fun)的语法是python语言语法和c语言语法的混血,如果你有写python扩展模块的需求，那么Cython真的是一个很好的工具

> 例: helloworld


```python
%%writefile /Users/huangsizhe/workspace/Pythonspace/cython/fac.pyx

def fac(n):
    if n<2 :
        return 1
    return n*fac(n-1)
```

    Writing /Users/huangsizhe/workspace/Pythonspace/cython/fac.pyx



```python
%%writefile /Users/huangsizhe/workspace/Pythonspace/cython/setup.py
#coding:utf-8
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
 
setup(
  name = 'fac',
  ext_modules=cythonize("fac.pyx")
)
```

    Overwriting /Users/huangsizhe/workspace/Pythonspace/cython/setup.py


注意目录和文件名都不能有中文

    python setup.py build_ext --inplace

可以看到编译出来.so文件


```python
from fib import fib
fib(10)
```

    1 1 2 3 5 8



```python
from fac import fac
```


```python
fac(10)
```




    3628800




```python
%timeit fac(10)
```

    The slowest run took 7.80 times longer than the fastest. This could mean that an intermediate result is being cached 
    1000000 loops, best of 3: 764 ns per loop


用pypy编译后看看能有多快


```python
from fac import fac
```


```python
%timeit fac(10)
```

    10000 loops, best of 3: 53.9 µs per loop


所以看得出来,这个库不是给pypy使得...
