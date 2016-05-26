
# 元类(metaclass)

我们都知道Python中啥都是类,那元类有是啥呢?元类可以理解为定义类的类.不过按这个逻辑不就没完没了了么,还好Python只有一层元类,这样复杂度还算可控,像ruby啥的就没完没了了.

基本上Python中类型机制是这样:

元类(metaclass)==>类(class)==>实例(instance)

一般我们只用到类和实例就很够用了.

那为啥要有元类,他有啥用呢?先说说作用:

+ 自由的、动态的修改/增加/删除 类的或者实例中的方法或者属性
+ 批量的对某些方法使用decorator，而不需要每次都在方法的上面加入@decorator_func
+ 当引入第三方库的时候，如果该库某些类需要patch的时候可以用metaclass
+ 可以用于序列化(参见yaml这个库的实现，我没怎么仔细看）
+ 提供接口注册，接口格式检查等
+ 自动委托(auto delegate)
...

那为啥要有个元类呢?

这就和Python的类型系统有关了,我们定义类一般式这样吧:


```python
class A(object):
    a=0
```


```python
dir(A)
```




    ['__class__',
     '__delattr__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__le__',
     '__lt__',
     '__module__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__weakref__',
     'a']



我们呢继承了object作为基类,创建了一个叫A的类,好像是这样,然而其实呢真相是这样的


```python
B = type("B",(object,),{"b":1})
```


```python
dir(B)
```




    ['__class__',
     '__delattr__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__le__',
     '__lt__',
     '__module__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__weakref__',
     'b']



type(classname,tuple of parent class ,dict of attributs)这个方法可以生成一个type对象,然后把它赋值给一个变量,于是一个新的类就诞生了!

也就是说--类也是对象!没错了还真是. 这就是类真正的生成方式.

那回到原来的问题,元类又是啥?type()方法就是一个metaclass~~


```python
dir(type)
```




    ['__abstractmethods__',
     '__base__',
     '__bases__',
     '__basicsize__',
     '__call__',
     '__class__',
     '__delattr__',
     '__dict__',
     '__dictoffset__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__flags__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__instancecheck__',
     '__itemsize__',
     '__le__',
     '__lt__',
     '__module__',
     '__mro__',
     '__name__',
     '__ne__',
     '__new__',
     '__prepare__',
     '__qualname__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasscheck__',
     '__subclasses__',
     '__subclasshook__',
     '__text_signature__',
     '__weakrefoffset__',
     'mro']



看它其实也是个对象...还有个`__call__()`方法.我们就是用这个方法来创建自定义类的.这个过程其实和`int()`创建整形.`str()`创建字符串是一样一样的.那所谓的元类说白了就是这些个对象而已.我们可以自己写个类似的专门用来实现自己的类型

记得在之前的<基本类型扩展>一节里面讲过的自定义扩展类型不,其实这个差不多,只是我们继承的是type.

>动态的修改/增加/删除 类的或者实例中的方法或者属性


```python
def ma(cls):  
    print('method a')
def mb(cls):  
    print('method b')  
method_dict = {  
    'ma': ma,  
    'mb': mb,  
}  
```


```python
class DynamicMethod(type):  
    def __new__(cls, name, bases, dct):  
        if name[:3] == 'Abc':  
            dct.update(method_dict)  
        return type.__new__(cls, name, bases, dct)  
  
    def __init__(cls, name, bases, dct):  
        super(DynamicMethod, cls).__init__(name, bases, dct)  
  
```


```python
class AbcTest(object,metaclass=DynamicMethod):  
    def mc(self, x):  
        print(x * 3)
```


```python
class NotAbc(object,metaclass=DynamicMethod):  
    def md(self, x):  
        print(x * 3)  
```


```python
def main():  
    a = AbcTest()  
    a.mc(3)  
    a.ma()  
    print(dir(a)) 
  
    b = NotAbc()  
    print(dir(b)) 
```


```python
main()
```

    9
    method a
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'ma', 'mb', 'mc']
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'md']


注意,这是python3中的写法,在python2中这样写


    class AbcTest(object):  
        __metaclass__=DynamicMethod
        def mc(self, x):  
            print(x * 3)

这个例子中我们利用元类和方法的动态绑定,根据类的名字判断了它需不需要绑定特定的方法,同理,可以通过第四个参数dct中的值来判断是否需要给一些方法绑定装饰器.很酷吧


> 实现方法自动绑定计数器


```python
def counter(func):
    count = 0
    def wrapper(*args,**kws):
        nonlocal count
        print("调用过",count,"次")
        count +=1
        return func(*args,**kws)
    return wrapper
```


```python
class CounterDecorator(type):  
    def __new__(cls, name, bases, dct):  
        for name, value in dct.items():  
            from types import FunctionType  
            if name not in ('__metaclass__', '__init__', '__module__') and type(value) == FunctionType:  
                value = counter(value)  
  
            dct[name] = value  
        return type.__new__(cls, name, bases, dct)  
    
    
class Operation(object,metaclass = CounterDecorator):  
  
    def sum_(self, *args):  
        print(sum(args)) 
        
    def mul_(self,*args):
        from functools import reduce
        print(reduce(lambda x,y:x*y,args,1))
```


```python
op = Operation() 
```


```python
op.sum_(1,2,3,4,5)
```

    调用过 0 次
    15



```python
op.sum_(1,2,3)
```

    调用过 1 次
    6



```python
op.mul_(1,2,3)
```

    调用过 0 次
    6



```python
op.mul_(2,3)
```

    调用过 1 次
    6


这种形式好处就是不用每个方法给打个装饰器了

> 打monkey-path


```python
#!/usr/bin/python
#coding :utf-8

def monkey_patch(name, bases, dct):
    assert len(bases) == 1
    base = bases[0]
    for name, value in dct.items():
        if name not in ('__module__', '__metaclass__'):
            setattr(base, name, value)
    return base

class A(object):
    def a(self):
        print('i am A object')


class PatchA(A,metaclass = monkey_patch):

    def patcha_method(self):
        print('this is a method patched for class A')

def main():
    pa = PatchA()
    pa.patcha_method()
    pa.a()
    print(dir(pa))
    print(dir(PatchA))


main()

```

    this is a method patched for class A
    i am A object
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'a', 'patcha_method']
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'a', 'patcha_method']


 通过继承原来的类来实现打补丁

> 利用委托模式实现不可变list和不可变dict


```python
class DelegateMetaClass(type):  
    def __new__(cls, name, bases, attrs):  
        methods = attrs.pop('delegated_methods', ())   
        for m in methods:  
            def make_func(m):  
                def func(self, *args, **kwargs):  
                    return getattr(self.delegate, m)(*args, **kwargs)  
                return func  
  
            attrs[m] = make_func(m)  
        return super(DelegateMetaClass, cls).__new__(cls, name, bases, attrs)  

    
    
class Delegate(object,metaclass=DelegateMetaClass):   
  
    def __init__(self, delegate):  
        self.delegate = delegate  
```

以上给出了对需要委托的方法进行的处理


```python
class ImmutableList(Delegate):  
    delegated_methods = ( '__contains__', '__eq__', '__getitem__', '__getslice__',   
                         '__str__', '__len__', 'index', 'count')  
```


```python
class ImmutableDict(Delegate):  
    delegated_methods = ('__contains__', '__getitem__', '__eq__', '__len__', '__str__',   
            'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'values')  
```


```python
il = ImmutableList([1,2,3,4])
for i in il:
    print(i)
```

    1
    2
    3
    4



```python
il.append(5)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-61-e8d7b6349c1b> in <module>()
    ----> 1 il.append(5)
    

    AttributeError: 'ImmutableList' object has no attribute 'append'

