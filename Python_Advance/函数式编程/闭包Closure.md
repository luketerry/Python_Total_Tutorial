
# 闭包(Closure)

所谓闭包是指一种组织代码的结构.函数的对象也是有作用域的,我们希望一个函数可以不依赖于外界的函数或者变量,自己就可以实现它的既定功能(也就是没有副作用),那么,有的时候我们就需要在函数的内部定义函数,这就是闭包了.


>例



```python
def expr1():
    a = 1
    b = 2
    c = 1
    def func(x):
        return a*x**2+b*x+c
    return func
```


```python
line = expr1()
```


```python
line.__closure__
```




    (<cell at 0x1026ddbe8: int object at 0x100e8c7e0>,
     <cell at 0x1026ddbb8: int object at 0x100e8c800>,
     <cell at 0x1026ddcd8: int object at 0x100e8c7e0>)



## 闭包的使用

闭包简单说就是可以把变量减少并固定化的一种技术.因为其无污染,所以很适合并行计算


```python
list(map(expr1(),range(10)))
```




    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



像这样使用闭包,可以看到隐藏了中间的`Enclosing function locals`层的变量,这层的变量相当安全,不会受到外界改变.

> 例: 看一个简单的计数器:


```python
def counter():
    d={"i":0}
    def count():
        d["i"]+= 1
        return d["i"]
    return count
```


```python
a = counter()
```


```python
a()
```




    1




```python
a()
```




    2



明明定义的一个函数,结果却向类一样,counter里返回的count可以返回counter中变量的的状态,这是闭包的优秀特性之一

# 闭包生成器

我们想输出一个包含不同参数方法的列表


```python
def closure1():
    return [lambda : i*i for i in range(1, 4)]
    
def main1():
    f1,f2,f3=closure1()
    print(f1())
    print(f2())
    print(f3())
```


```python
main1()
```

    9
    9
    9


看到结果都是9是不是觉得很诡异,其实这就是因为函数f要寻找变量i,在函数内部找不到i,那就会在外部嵌套函数中寻找,外部嵌套中i已经从1走到3了,也就是i=3了,那就都是为啥结果都是9了


```python
def closure2():
    return (lambda :i*i for i in range(1, 4))
    
def main2():
    for j in closure2():
        print(j())
```


```python
main2()
```

    1
    4
    9


这是为啥呢?其实是因为生成器是一步一步执行的,不进行next程序就没跑完,所以当我们跑main2的时候实际上i在每一步都不一样,是不是很有意思
