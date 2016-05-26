
# 弱引用模块(weakref)

Python提供了一个弱引用模块.

所谓弱引用是指:

相对于通常的引用来说，如果一个对象有一个常规的引用，它是不会被垃圾收集器销毁的，但是如果一个对象只剩下一个弱引用，那么它可能被垃圾收集器收回。这个特性很适合用在缓存编程和映射上.

并非所有的对象都支持weakref，例如list和dict就不支持，但是文档中介绍了可以通过继承dict来支持weakref

查看一个对象的引用次数可以用`sys.getrefcount(obj)`

## weakref模块具有的方法

+ class weakref.ref(object[, callback]) 

   创建一个弱引用对象，object是被引用的对象，callback是回调函数（当被引用对象被删除时的，会调用改函数）。

+ weakref.proxy(object[, callback]) 

   创建一个用弱引用实现的代理对象，参数同上。

+ weakref.getweakrefcount(object) 

   获取对象object关联的弱引用对象数

+ weakref.getweakrefs(object)

   获取object关联的弱引用对象列表

+ class weakref.WeakKeyDictionary([dict]) 

   创建key为弱引用对象的字典

+ class weakref.WeakValueDictionary([dict]) 

   创建value为弱引用对象的字典

+ class weakref.WeakSet([elements]) 

   创建成员为弱引用对象的集合对象

## weakref模块具有的属性

+ weakref.ReferenceType  -------- 被引用对象的类型

+ weakref.ProxyType        --------- 被代理对象（不能被调用）的类型

+ weakref.CallableProxyType -- 被代理对象（能被调用）的类型

+ weakref.ProxyTypes      ---------- 所有被代理对象的类型序列

+ exception weakref.ReferenceError  


## 例子:



```python
import sys 
import weakref
from __future__ import print_function
```


```python
class Class1(object):  
    def Foo(self):  
        print("Foo")  
```


```python
o=Class1()
```


```python
sys.getrefcount(o)
```




    2




```python
r = weakref.ref(o,lambda self:print("weakref disappear")) # 创建一个弱引用  
sys.getrefcount(o) # 引用计数并没有改变  
```




    2




```python
r
```




    <weakref at 0x103e3d1b0; to 'Class1' at 0x103e2e690>




```python
o2 = r()
```


```python
o2 is o
```




    True




```python
sys.getrefcount(o)  
```




    3




```python
o = None
```


```python
o2 = None
```

    weakref disappear



```python
r
```




    <weakref at 0x103e3d1b0; dead>



## 使用代理


```python
x=Class1()
x
```




    <__main__.Class1 at 0x103e2ee10>




```python
y = weakref.proxy(x,lambda self:print("weakref proxy disappear") ) 
y.Foo()
```

    Foo



```python
x2 = y
```


```python
x2.Foo()
```

    Foo



```python
x.Foo()
```

    Foo



```python
x2 is x
```




    False




```python
x = None
```
