
如果一个类在程序中只会并且只有一个实例,

主要优点：

1. 提供了对唯一实例的受控访问。
2. 由于在系统内存中只存在一个对象，因此可以节约系统资源，对于一些需要频繁创建和销毁的对象单例模式无疑可以提高系统的性能。
3. 允许可变数目的实例。
 
主要缺点：

1. 由于单利模式中没有抽象层，因此单例类的扩展有很大的困难。
2. 单例类的职责过重，在一定程度上违背了“单一职责原则”。
3. 滥用单例将带来一些负面问题，如为了节省资源将数据库连接池对象设计为的单例类，可能会导致共享连接池对象的程序过多而出现连接池溢出；如果实例化的对象长时间不被利用，系统会认为是垃圾而被回收，这将导致对象状态的丢失。


使用场景:

+ 只有一个资源且需要共享其状态信息的场景.


那么这就是单例模式了,具体的实现:



## Borg

Borg实际上并不是只有一个实例,而是所有实例共享属性,效果上来看一样啦,它的特点是实例化等于刷新,旧的属性会被替代

> 1.继承Borg类实现

其实就是共享一个变量,并固定`__dict__`,


```python
class Borg:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'Init'

    def __str__(self):
        return self.state


```


```python
class YourBorg(Borg):
    def __init__(self,a):
        Borg.__init__(self)
        self.a = a
```


```python
A = YourBorg(1)
A.a
```




    1




```python
B = YourBorg(2)
B.a
```




    2




```python
A.a
```




    2




```python
id(A) ==id(B)
```




    False



> 利用装饰器实现


```python
def borg(cls):
    cls._state = {}
    orig_init = cls.__init__
    def new_init(self, *args, **kwargs):
        self.__dict__ = cls._state
        orig_init(self, *args, **kwargs)
    cls.__init__ = new_init
    return cls
```


```python
@borg
class Myborg(object):
    def __init__(self,a):
        self.a = a
    
```


```python
C = Myborg(1)
```


```python
C.a
```




    1




```python
D = Myborg(2)
```


```python
D.a
```




    2




```python
C.a
```




    2




```python
id(C) ==id(D)
```




    False



## standalone

正经单例模式,这回事第一次实例化后就无法改变

> 使用Singleton元类


```python
class Singleton(type):  
    def __init__(cls, name, bases, dict):  
        super(Singleton, cls).__init__(name, bases, dict)  
        cls._instance = None  
    def __call__(cls, *args, **kw):  
        if cls._instance is None:  
            cls._instance = super(Singleton, cls).__call__(*args, **kw)  
        return cls._instance  
```

3中用法:


```python
class MySingleton(object,metaclass=Singleton ):  
    def __init__(self,a):
        self.a = a
        
```

2.7中用法:

```python
class MySingleton(object): 
    __metaclass__ = Singleton 
    def __init__(self,a):
        self.a = a
```


```python
class MySingleton(object): 
    __metaclass__ = Singleton 
    def __init__(self,a):
        self.a = a
```


```python
E = MySingleton(1)
```


```python
E.a
```




    1




```python
F = MySingleton(2)
```


```python
F.a
```




    1




```python
id(E) == id(F)
```




    True



> 利用装饰器


```python
def singleton(cls, *args, **kw):  
    instances = {}  
    def _singleton(*args, **kw):  
        if cls not in instances:  
            instances[cls] = cls(*args, **kw)  
        return instances[cls]  
    return _singleton  
```


```python
@singleton  
class MyClass4(object):  
    def __init__(self, a):  
        self.a = a  
```


```python
one = MyClass4(1)  
print one.a
two = MyClass4(2)  
print two.a
```

    1
    1



```python
two.a = 3  
print(one.a) 
```

    3



```python
print(id(one))
print(id(two)) 
```

    4361105488
    4361105488


> 单例模式类工厂


```python
class singletonFactory(object):
    instances = {}
    def __call__(self,clz,*args, **kw):
        if clz not in self.instances:  
            self.instances[clz] = clz(*args, **kw)  
        return self.instances[clz]  
```


```python
class MyClass4(object):  
    def __init__(self, a):  
        self.a = a  
```


```python
fac = singletonFactory()
a = fac(MyClass4,1)
```


```python
a.a
```




    1




```python
b = fac(MyClass4,2)
```


```python
b.a
```




    1



还可以监控有哪些单例


```python
fac.instances
```




    {__main__.你: <__main__.你 at 0x103f232d0>,
     __main__.MyClass4: <__main__.MyClass4 at 0x103f23ad0>,
     __main__.A: <__main__.A at 0x103f23150>}



配合type方法实现多个单例模式类的的定义和使用


```python
class base(object):
    def __init__(self,a):
        self.a =a
```


```python
clzname = ["你","我","它"]
```


```python
classes = [type(i,(base,),{}) for i in clzname]
```


```python
classes
```




    [__main__.你, __main__.我, __main__.它]




```python
c = fac(classes[0],1)
```


```python
c.a
```




    1




```python
d = fac(classes[0],2)
```


```python
d.a
```




    1




```python
id(c)==id(d)
```




    True



> 实例:汇率

假设我们有一个应用需要一直追踪美元兑rmb的汇率,这是一个典型的单例模式一般汇率只获取一次就好,不用每次调用都获取一遍,我们为了减少


```python
URL="http://download.finance.yahoo.com/d/quotes.csv?s=USDCNY=X&f=sl1d1t1ba&e=.csv"
```


```python
from requests import get
```


```python
a = get(URL)
```


```python
a.text
```


```python
from Creational import lazy, singleton
@singleton 
class ExchangeRateUSDtoCNY(object):  
    def __init__(self):  
        self.date = None
        self.time = None
        self.From = "USD"
        self.To="CNY"
        self.URL="http://download.finance.yahoo.com/d/quotes.csv?s={self.From}{self.To}=X&f=sl1d1t1ba&e=.csv".format(self=self)
    @lazy
    def current_value(self):
        class Value(object):
            def __str__(self):
                time = self.time.strftime('%m/%d/%Y%H:%M%p')
                return """\
                {time}:{self.value}
                """.format(time=time,self=self)
            def __init__(self,time,value):
                self.time = time
                self.value = value
        from requests import get
        from datetime import datetime
        resultstr = get(self.URL).text
        result = resultstr.split(",")[1]
        date = result[2]
        time = result[3].upper()
        return Value(datetime.strptime(date + time, '%m/%d/%Y%H:%M%p'),result)
        
    
```


```python
a = ExchangeRateUSDtoCNY()
```


```python
a.current_value
```


```python
from requests import get 
    
from datetime import datetime
URL = "http://download.finance.yahoo.com/d/quotes.csv?s=USDCNY=X&f=sl1d1t1ba&e=.csv"
resultstr = get(URL).text
result = resultstr.split(",")
date = result[2]
time = result[3].upper()
datetime.strptime(date.join(time), '"%m/%d/%Y""%H:%M%p"')
```


```python
datetime
```


```python
date.split('"')[1]
```


```python

```
