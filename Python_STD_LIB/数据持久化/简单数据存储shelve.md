
# python基础应用--简单数据存储(shelve)

shelve是一个简单的数据存储方案，在shelve模块中，key必须为字符串，而值可以是python所支持的数据类型

它依赖两个库`dbm(anydbm)`和`pickel`

一般来说shelve会调用dbm(anydbm)来指定特定的微数据库做存储,可以是dbm.ndbm(dbm),dbm.gnu(gdbm),dbm.dumb(dumbdbm).具体指定谁,要看你的机器里具体有哪个,如果前两个都没有,才会用自带的dbm.dumb(dumbdbm).

而pickel则是用来将python对象序列化为字符串或二进制代码以用于存储的模块.

pickel到目前为止有5种序列化格式:

版本|说明|支持python版本
---|---|---
0| 人类可读的文本,用于最早期|全部版本
1| 老的二进制版本文本同样用于早期|全部版本
2| 出现于2.3版本,用以支持新类|2.3+
3|出现于3.0版本,用以支持bytes类型|3.0+ 
4| 出现于Python 3.4.用于扩充pickel的支持类型和大对象|3.4+ 

要向下支持的话,我们必须设定pickel的版本为2,即protocol=2


如果要存储类的实例除了要存储对象外,还要在调用对象前定义一个包含相同属性的类,方法可以不同.因为实际上 shelve只保存对象的状态,而不是保存它本身


```python
import shelve
try:
    import dbm.ndbm as dbm
except ImportError:
    import dbm
```


```python
def dbm_shelve(filename, flag="c",protocol=2): 
    return shelve.Shelf(dbm.open(filename, flag),protocol) 
```


```python
sh = dbm_shelve('newsh.data')#有点类似连接sqlite~
```


```python
sh["int"]=1
```


```python
sh["str"]="a"
```


```python
sh["list"]=[1,2,3]
```


```python
sh["dict"]={1:"q"}
```


```python
class A(object):
    
    def __init__(self):
        self.a = 10
        print("a="+str(self.a))
        
    def changea(self):
        self.a = self.a+10
```


```python
a = A()
```

    a=10



```python
sh["object"]=a
```


```python
sh["object"].a
```




    10




```python
b = A()
```

    a=10



```python
b.changea()
```


```python
b.a
```




    20




```python
sh["object2"]=b
```

当你下次再进入是只要再连接下就又可以获取到上次存储的值了.

之前我们用python3.5,现在换到python2.7看看是否可以读取之前的内容


```python
#2.7
import shelve
```


```python
sh = shelve.open('newsh.data', flag="c",protocol=2)#有点类似连接sqlite~
```


```python
sh["int"]
```




    1




```python
class A(object):
    b=10
    
    def __init__(self):
        self.a = 10
        print("a="+str(self.a))
        
    def changea(self):
        self.a = self.a+10
        
    def changb(self):
        self.b = self.b+5
```


```python
a = sh["object"]
```


```python
a.a
```




    10




```python
a.b
```




    10




```python
b = sh["object2"]
```


```python
b.a
    
```




    20




```python
b.b
```




    10


