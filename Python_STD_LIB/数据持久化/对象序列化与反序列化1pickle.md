
# Python对象持久化(pickle)

python的pickle模块实现了基本的数据序列和反序列化。通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储；通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。

需要注意,pickel的文件并不是默认跨版本支持的,可以对照这张表设定需要的参数

pickel到目前为止有5种序列化格式:

版本|说明|支持python版本
---|---|---
0| 人类可读的文本,用于最早期|全部版本
1| 老的二进制版本文本同样用于早期|全部版本
2| 出现于2.3版本,用以支持新类|2.3+
3|出现于3.0版本,用以支持bytes类型|3.0+ 
4| 出现于Python 3.4.用于扩充pickel的支持类型和大对象|3.4+ 

要向下支持的话,我们必须设定pickel的版本为2,即protocol=2


```python
from pickle import dump, load, dumps,loads
```

## dump(obj, file, [,protocol])  

将对象obj保存到文件file中去。


```python
exa_l=[1,2,3,4,5]
```


```python
with open("./pickle_test.txt","wb") as f:
    dump(exa_l,f,protocol=2)
```

## load(file)

从file中读取一个字符串，并将它重构为原来的python对象。


```python
with open("./pickle_test.txt","rb") as f:
    view_exam = load(f)
view_exam
```




    [1, 2, 3, 4, 5]



## dumps(obj,[,protocol])  
序列化为bytes


```python
exa_b = dumps(exa_l)
```


```python
exa_b
```




    b'\x80\x03]q\x00(K\x01K\x02K\x03K\x04K\x05e.'



## loads(b)  
反序列化为对象


```python
loads(exa_b)
```




    [1, 2, 3, 4, 5]



## 命令行工具 `pickletools`[3+]

在python3中提供了一个命令行工具来管理pickle文件


```python
!python3 -m pickle pickle_test.txt
```

    [1, 2, 3, 4, 5]



```python
!python3 -m pickletools pickle_test.txt
```

        0: \x80 PROTO      2
        2: ]    EMPTY_LIST
        3: q    BINPUT     0
        5: (    MARK
        6: K        BININT1    1
        8: K        BININT1    2
       10: K        BININT1    3
       12: K        BININT1    4
       14: K        BININT1    5
       16: e        APPENDS    (MARK at 5)
       17: .    STOP
    highest protocol among opcodes = 2


可用的参数:


+ -a, --annotate

Annotate each line with a short opcode description.

+ -o, --output=<file>

Name of a file where the output should be written.

+ -l, --indentlevel=<num>

The number of blanks by which to indent a new MARK level.

+ -m, --memo

When multiple objects are disassembled, preserve memo between disassemblies.

+ -p, --preamble=<preamble>

When more than one pickle file are specified, print given preamble before each disassem

## 不可 pickle 的对象

一些对象类型是不可 pickle 的。例如，Python 不能 pickle 文件对象（或者任何带有对文件对象引用的对象），因为 Python 在 unpickle 时不能保证它可以重建该文件的状态（另一个示例比较难懂，在这类文章中不值得提出来）。

## pickle 类实例

与 pickle 简单对象类型相比，pickle 类实例要多加留意。这主要由于 Python 会 pickle 实例数据（通常是 _dict_ 属性）和类的名称，而不会 pickle 类的代码。当 Python unpickle 类的实例时，它会试图使用在 pickle 该实例时的确切的类名称和模块名称（包括任何包的路径前缀）导入包含该类定义的模块。另外要注意，类定义必须出现在模块的最顶层，这意味着它们不能是嵌套的类（在其它类或函数中定义的类）。

当 unpickle 类的实例时，通常不会再调用它们的 _init_() 方法。相反，Python 创建一个通用类实例，并应用已进行过 pickle 的实例属性，同时设置该实例的 _class_ 属性，使其指向原来的类。

我们可以用`copyreg`这个模块注册需要的实例


```python
import copyreg
```


```python
class C(object):
    def __init__(self,a):
        self.a = a
def pickle_c(c):
    return C,(c.a,)
```


```python
copyreg.pickle(C,pickle_c)
```


```python
c = C(1)
```


```python
c
```




    <__main__.C at 0x108ab4b00>




```python
p = dumps(c)
```


```python
p
```




    b'\x80\x03c__main__\nC\nq\x00K\x01\x85q\x01Rq\x02.'




```python
cc = loads(p)
```


```python
cc
```




    <__main__.C at 0x108a999e8>




```python
cc.a
```




    1


