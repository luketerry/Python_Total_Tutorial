
# 高阶函数( higher-order functions)

别被名字吓到啦,高阶函数不是啥多高级的特性啦.所谓高阶函数就是说:

函数有最高地位,它可以像一个值一样被付给变量,被传递,传递函数的函数就是所谓的高阶函数.

Python当然是支持高阶函数的啦.我们来看个例子:



```python
def add(x,y,f):
    return f(x)+f(y)
add(-3,4,abs)
```




    7




```python
def plus1(x):#传入实名函数
    return x+1

add(-3,4,plus1)
```




    3




```python
plu=plus1#传入赋值为函数的变量

add(-3,4,plu)
```




    3




```python
add(-3,4,lambda i: i**2)#传入匿名函数
```




    25



可见函数的传入参数只要是对象即可,因为传入的对象会被对应的赋值给形参

## Python内置的高阶函数

Python中内置了一些常用的高阶函数,可以方便的代替迭代,让代码更加简洁.其中有一些我们在快速入门部分也已经见过了,这些函数多是和可迭代对象组合使用,当可迭代对象是容器时他们会

> apply 触发器(2.7)

apply是用于触发函数的函数看个例子


```python
f = lambda x:x**2
```


```python
apply(f,(3,))
```




    9



看得出apply可以用来做工厂,这也算是2.7的福利之一


```python
fns={"+":lambda x,y:x+y,
    "-":lambda x,y:x-y}
```


```python
apply(fns.get("+"),(3,4))
```




    7




```python
apply(fns.get("-"),(3,4))
```




    -1



>filter过滤器

    filter(func,iterable)->Iterator
    
过滤器中传入一个返回布尔值的函数,该函数将作用于可迭代对象的每个子项.



```python
A =["小明","大黄","小白","小黑","乐乐"]
```

我们来过滤掉其中没有小字的


```python
list(filter(lambda x : "小" in x ,A ))
```




    ['小明', '小白', '小黑']



> map映射器

    map(func,iterable)->Iterator
  
map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

例 :我们把每个名字改成叠词(已经是叠词的不管)


```python
list(map(lambda x: x if x[-1]==x[-2] else x+x[-1],A))
```




    ['小明明', '大黄黄', '小白白', '小黑黑', '乐乐']



> reduce 化简器

    reduce(func,iterable)->value

reduce函数即为化简，它是这样一个过程：每次迭代，将上一次的迭代结果（第一次时为init的元素，如没有init则为seq的第一个元素）与下一个元素一同执行一个二元的func函数。在reduce函数中，init是可选的，如果使用，则作为第一次迭代的第一个元素使用。

现在版本reduce已经不是python的内置函数了,而是`functools`模块的一员

例:求阶乘


```python
from functools import reduce#2.7中不需要
reduce(lambda x,y:x*y,range(1,10))
```




    362880



> sorted 排序器

    sorted(iterable, key=func, reverse=False)

sorted比较特殊,如果是简单结构的序列,那么他会根据元素的类型来排序,比如数字就是按大小排,字符串就是按首字母顺序等.而key则是必须是一个可以让吗,每个元素执行的函数,其返回值也就是sorted排序时的输入值(权重)了.
当结构复杂时,sorted会默认以第一位作为排序时的输入值.



```python
sorted([36, 5, -12, 9, -21])
```




    [-21, -12, 5, 9, 36]




```python
sorted([36, 5, -12, 9, -21],reverse=True)
```




    [36, 9, 5, -12, -21]




```python
sorted([36, 5, -12, 9, -21],key = lambda x:x**2)
```




    [5, 9, -12, -21, 36]



但是如果是其他的复合类型呢,我们就该他指定一个比较的准则,

例:安成绩排序


```python
sorted([('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)])
```




    [('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]




```python
sorted([('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)],key = lambda t: t[1],reverse=True )
```




    [('Adam', 92), ('Lisa', 88), ('Bob', 75), ('Bart', 66)]



> all(iter)判断全真


```python
l=[1,2,3,4,5]
all(map(lambda x: True if x>3 else False,l))
```




    False



> any(iter)判断有真


```python
l=[1,2,3,4,5]
any(map(lambda x: True if x>3 else False,l))
```




    True


