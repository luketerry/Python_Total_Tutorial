
# 生成器(generator)和生成器表达式

## 生成器

Python的生成器是许多特性和功能的基础,比如惰性求值,比如协程,让我们看看这是咋回事吧~



```python
def fib0(N):
    assert type(N)==int
    assert N>0
    n,a,b = 0,0,1
    while n < N:
        yield b
        a,b = b,a+b
        n += 1
```


```python
list(fib0(5))
```




    [1, 1, 2, 3, 5]




```python
for i in fib0(10):
    print(i)
```

    1
    1
    2
    3
    5
    8
    13
    21
    34
    55


>练习 画个杨辉三角


```python
def pas_triangles(N):
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]
        if len(a)==N:
            break

```


```python
list(pas_triangles(11))
```




    [[1],
     [1, 1],
     [1, 2, 1],
     [1, 3, 3, 1],
     [1, 4, 6, 4, 1],
     [1, 5, 10, 10, 5, 1],
     [1, 6, 15, 20, 15, 6, 1],
     [1, 7, 21, 35, 35, 21, 7, 1],
     [1, 8, 28, 56, 70, 56, 28, 8, 1],
     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]




```python
for i in pas_triangles(11):
    print(i)
```

    [1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    [1, 4, 6, 4, 1]
    [1, 5, 10, 10, 5, 1]
    [1, 6, 15, 20, 15, 6, 1]
    [1, 7, 21, 35, 35, 21, 7, 1]
    [1, 8, 28, 56, 70, 56, 28, 8, 1]
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]


## 生成器的结构方法


生成器的定义方法总结起来大约是这样:

    def g(args):
        code
        n = (yield y)
        
总结起来使用生成器的注意点有:

+ 不用return而是用yield来返回一个数
+ 一个生成器要被调用一般使用Python的内置函数`next()`来调用,每次调用后状态改变,生成器挂起等待下次调用或者结束时抛出异常终止异常
+ yield是个表达式,他可以有返回值,这个返回值可以用Python的内置函数`send()`来定义,通过这种方式来改变生成器内部的状态(调用send传入非None值前，生成器必须处于挂起状态，否则将抛出异常。不过，未启动的生成器仍可以使用None作为参数调用send.)
+ 可以使用`close()`方法直接关闭生成器
+ throw(type, value=None, traceback=None):这个方法用于在生成器内部（生成器的当前挂起处，或未启动时在定义处）抛出一个异常。

例子:


```python
def echo(value=None):
    print("Execution starts when 'next()' is called for the first time.")
    try:
        while True:
            try:
                value = (yield value)
            except Exception as e:
                value = e
    finally:
        print("Don't forget to clean up when 'close()' is called.")

```


```python
generator = echo(1)
next(generator)
```

    Execution starts when 'next()' is called for the first time.





    1




```python
generator.send("q")
```




    'q'




```python
generator.throw(TypeError, "spam")
```




    TypeError('spam')




```python
generator.close()
```

    Don't forget to clean up when 'close()' is called.


## 生成器的特性

python中的生成器在许多函数式语言中又叫流(stream)因为它是被动的产生输出结果,同时每次只产生一个局部的结果,在面对大量资源消耗时是非常高效的一种手段.

我们看看它的特性

> 惰性

生成器内部保存着运算的逻辑而不是运算的结果,只有当调用的时候才会计算,如何调用呢,在Python3中我们使用内置函数next()来获取下一个结果(另外3和2.7还可以分别使用`.next()`或者`.__next_()`方法)



```python
fib3 = fib0(3)
next(fib3)
```




    1




```python
next(fib3)
```




    1




```python
next(fib3)
```




    2




```python
next(fib3)
```


    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    <ipython-input-15-11a7f48c84ea> in <module>()
    ----> 1 next(fib3)
    

    StopIteration: 


可以看到如果不调用生成器,那生成器就不会计算下一个结果

> 记忆状态

看我们的斐波那契数列就知道了,它总能记下前一次的结果

> 单次可用

生成器一旦关闭了就无法打开,运行过程中除了用`send()`方法外也没有别的改变内部的方法,这样确保其封闭性安全性

## 生成器表达式

在解析的部分咱是不是漏了啥?对了,元组呢?

其实元组的解析进化了,它叫生成器表达式,大约是这样


```python
g = (x*y for x in range(1,11) if x%2==0 for y in range(1,11) if y%3 ==0 )
g
```




    <generator object <genexpr> at 0x10cdeefc0>



元组的解析会返回一个生成器对象,它就是个生成器
