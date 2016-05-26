
[numba](http://numba.pydata.org/numba-doc/dev/index.html)是利用llvm加速python的技术,虽然现在还在开发中,但已经基本可用了

numba有代码预热,如果迭代太少反而会减低效率


```python
from numba import jit,int32,int64,typeof
from numpy import arange
from datetime import datetime

# jit decorator tells Numba to compile this function.
# The argument types will be inferred by Numba when function is called.

@jit
def sum2d(arr):
    M, N = arr.shape
    result = 0.0
    for i in range(M):
        for j in range(N):
            result += arr[i,j]
    return result

a = arange(9999999).reshape(3333333,3)
start = datetime.now()
print(sum2d(a))
stop = datetime.now()
print(stop-start)
```

    4.9999985e+13
    0:00:00.129586



```python
def sum2d0(arr):
    M, N = arr.shape
    result = 0.0
    for i in range(M):
        for j in range(N):
            result += arr[i,j]
    return result

a = arange(9999999).reshape(3333333,3)
start = datetime.now()
print(sum2d0(a))
stop = datetime.now()
print(stop-start)
```

    4.9999985e+13
    0:00:03.998436



```python
@jit
def fac(n):
    if n<2 :
        return 1
    return n*fac(n-1)
```


```python
fac(10)
```




    3628800




```python
%timeit fac(10)
```

    100000 loops, best of 3: 2.94 µs per loop


看到确实可以有加速,但在迭代次数少的时候似乎并不太明显,而且最好不要用递归


## 高阶函数


```python
@jit
def compare(t1,t2):
    result = []
    for i in t1:
        for j in t2:
            if i[1] == j[1]:
                result.append(i[0])
                
    return result
```


```python
a = [[2,[1,2,3]],[4,[5,4,3]]]
b = [[3,[2,3,4]],[6,[5,9,3]]]
```


```python
typeof(a[0][1])
```




    reflected list(int64)




```python
compare(a[0][1],b[0][1])
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-48-4268315a0b89> in <module>()
    ----> 1 compare(a[0][1],b[0][1])
    

    /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/numba/dispatcher.pyc in typeof_pyval(self, val)
        246         # Not going through the resolve_argument_type() indirection
        247         # can shape a couple µs.
    --> 248         tp = typeof(val)
        249         if tp is None:
        250             tp = types.pyobject


    /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/numba/typing/typeof.pyc in typeof(val, purpose)
         27     # Note the behaviour for Purpose.argument must match _typeof.c.
         28     c = _TypeofContext(purpose)
    ---> 29     return typeof_impl(val, c)
         30 
         31 


    /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/singledispatch.pyc in wrapper(*args, **kw)
        208 
        209     def wrapper(*args, **kw):
    --> 210         return dispatch(args[0].__class__)(*args, **kw)
        211 
        212     registry[object] = func


    /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/numba/typing/typeof.pyc in _typeof_list(val, c)
        124 def _typeof_list(val, c):
        125     if len(val) == 0:
    --> 126         raise ValueError("Cannot type empty list")
        127     ty = typeof_impl(val[0], c)
        128     return types.List(ty, reflected=True)


    ValueError: Cannot type empty list



```python
typeof({1:10,2:20})
```


```python

```
