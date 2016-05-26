
# 装饰器(decorator)

Python中有一个很有特色的语法糖叫装饰器,它可以用来"装饰"一个类或者函数

它其实就是这么回事儿:

    func(args) = decorator(func(args))
    cls(args) = decorator(cls(args))
    
基本上装饰器可以分成函数装饰器和类装饰器两种,他们原理上是一样的,就是用一个函数包裹住其下面的函数或者类,只是作用对象不同.

+ 函数装饰器 在函数定义的时候进行名称重绑定,提供一个逻辑层来管理函数和方法 或随后对它们的调用。
+ 类装饰器 在类定义的时候进行名称重绑定,提供一个逻辑层来管理类,或管理随后 调用它们所创建的示例。

## 函数装饰器

一个最简单的例子


```python
def 开头结尾(func):
    print(func.__name__+"开始运行")
    func()
    print(func.__name__+"运行好了")
```


```python
@开头结尾
def a():
    print("a运行了")
```

    a开始运行
    a运行了
    a运行好了


另一种写法是这样:


```python
class 开头结尾2:
    def __init__(self,func):
        self.func = func
        
    def __call__(self,*args):
        print(self.func.__name__+"开始运行")
        result = self.func(*args)
        print(self.func.__name__+"运行好了")
        return result
```


```python
@开头结尾2
def a(*args):
    print("a运行了")
    return sum(args)
```


```python
a(10,20)
```

    a开始运行
    a运行了
    a运行好了





    30



当然更加通用的写法是这样(闭包):


```python
def 开头结尾3(func):
    print(func.__name__+"载入了")
    def wrapper(*args):
        print(func.__name__+"开始运行")
        result = func(*args)
        print(func.__name__+"运行结束")
        return result
    
    return wrapper
```


```python
@开头结尾3
def a(*args):
    print("a运行了")
    return sum(args)
```

    a载入了



```python
a(1,2,3)
```

    a开始运行
    a运行了
    a运行结束





    6



写个有实际作用的装饰器吧,

例:编写一个可以记录函数调用次数的函数装饰器


```python
def 调用计数君(func):
    count = 0
    def wrapper(*args,**kws):
        nonlocal count
        print("调用过",count,"次")
        count +=1
        return func(*args,**kws)
    return wrapper
```


```python
@调用计数君
def mul(*args):
    from operator import mul
    from functools import reduce
    return reduce(mul, range(1, 10))
```


```python
a = mul(1,2,3)
```

    调用过 0 次



```python
b = mul(4,7,8)
```

    调用过 1 次


>例:写一个装饰器,计算函数的执行时间


```python
def 计时君1(func,label = "==>"):
    print("计时君准备好啦~")
    def wrapper(*args,**kws):
        nonlocal label
        totaltime = []
        print("开始计时")
        for i in range(1000):
            import datetime
            start = datetime.datetime.now()
            result = func(*args,**kws)
            end = datetime.datetime.now()
            time = end - start
            totaltime.append(time.microseconds)
        mean = sum(totaltime)/1000
        print("计时结束")
        print("共计用时",label,mean,"ms")
        return result
    return wrapper
```


```python
@计时君1
def f_o_r(n):
    return sum(range(n))
    
```

    计时君准备好啦~



```python
f_o_r(40000)
```

    开始计时
    计时结束
    共计用时 ==> 1924.359 ms





    799980000



## 类装饰器

我们来定义一个单例类型装饰器:


```python
def 单例类型(cls):
    实例 = None
    def wrapper(*args):
        nonlocal 实例
        if 实例 ==None:
            实例 = cls(*args)
        return 实例
    return wrapper
```


```python
@单例类型
class People:
    def __init__(self,name):
        self.name = name
    def play(self):
        print(self.name,"playing")
    
```


```python
tom = People("tom")
```


```python
JoJo=People("JoJo")#可以创建,但不会改变实例内容
```


```python
tom.name
```




    'tom'




```python
JoJo.name
```




    'tom'



> 例:写一个可以追踪类中元素被调用情况的装饰器


```python
def 追踪君(cls):
    class Wrapper:
        def __init__(self,*args,**kws):
            self.fetches = 0
            self.wrapped = cls(*args,**kws)
        def __getattr__(self,attrname):
            print("追踪君:",attrname)
            self.fetches += 1
            return getattr(self.wrapped,attrname)
    return Wrapper
```


```python
@追踪君
class A:
    def display(self): 
        print('欧拉!' * 8)
```


```python
@追踪君
class Person:
    def __init__(self,name):
        self.name = name
    def play(self):
        print(self.name,"playing")
```


```python
a =A()
```


```python
a.display()
```

    追踪君: display
    欧拉!欧拉!欧拉!欧拉!欧拉!欧拉!欧拉!欧拉!



```python
a.fetches
```




    1




```python
JoJo = Person("JoJo")
```


```python
Dio = Person("Dio")
```


```python
JoJo.name
```

    追踪君: name





    'JoJo'




```python
JoJo.play()
```

    追踪君: play
    JoJo playing



```python
JoJo.fetches
```




    2




```python
Dio.play()
```

    追踪君: play
    Dio playing



```python
Dio.fetches
```




    1



## 带参数的装饰器

装饰器是可以带参数的


```python
def deco(*dargs):# 装饰器的参数
    def getfunc(func):#被装饰的函数
        def swap(*args):#函数的参数
            return func(*args)+sum(dargs)
        return swap
   
    return getfunc
```


```python
@deco(1,2,3)
def add(x,y,z):
    return x+y+z
```


```python
add(4,5,6)
```




    21



就像大多数语言功能一样,装饰器也有优点和缺点。例如,从负面的角度讲,类装饰器 有两个潜在的缺陷:

+ 类型修改

    正如我们所见到的,当插入包装器的时候,一个装饰器函数或类不会保持其最初的 类型——其名称重新绑定到一个包装器对象,在使用对象名称或测试对象类型的程 序中,这可能会很重要。在单体的例子中,装饰器和管理函数的方法都为实例保持 了最初的类类型;在跟踪器的代码中,没有一种方法这么做,因为需要有包装器。

+ 额外调用

    通过装饰添加一个包装层,在每次调用装饰对象的时候,会引发一次额外调用所需 的额外性能成本——调用是相对耗费时间的操作,因此,装饰包装器可能会使程序 变慢。在跟踪器代码中,两种方法都需要每个属性通过一个包装器层来指向;单体 的示例通过保持最初的类类型而避免了额外调用。
    
装饰器有3个主要优点。与前面小节的管理器 (即辅助)函数解决方案相比,装饰器提供:

+ 明确的语法

    装饰器使得扩展明确而显然。它们的@比可能在源文件中任何地方出现的特殊代码 要容易识别,例如,在单体和跟踪器实例中,装饰器行似乎比额外代码更容易被注 意到。此外,装饰器允许函数和实例创建调用使用所有P y t h o n程序员所熟悉的常规语法。

+ 代码可维护性

    装饰器避免了在每个函数或类调用中重复扩展的代码。由于它们只出现一次,在类 或者函数自身的定义中,它们排除了冗余性并简化了未来的代码维护。对于我们的 单体和跟踪器示例,要使用管理器函数的方法,我们需要在每次调用的时候使用特 殊的代码——最初以及未来必须做出的任何修改都需要额外的工作。

+ 一致性

    装饰器使得程序员忘记使用必需的包装逻辑的可能性大大减少。这主要得益于两个 优点——由于装饰是显式的并且只出现一次,出现在装饰的对象自身中,与必须包 含在每次调用中的特殊代码相比较,装饰器促进了更加一致和统一的A P I使用。例 如,在单体示例中,可能更容易忘了通过特殊代码来执行所有类创建调用,而这将 会破坏单体的一致性管理。
