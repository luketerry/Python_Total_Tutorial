
# 自省(inspect)

Python的自省在快速入门中已经有介绍.标准库中有inspect模块可以帮助自省


```python
import inspect
```

> 检查对象类型

方法|说明
---|---
is{module/class/function/method/builtin}(obj) |检查对象是否为模块、类、函数、方法、内建函数或方法
isroutine(obj)|用于检查对象是否为函数、方法、内建函数或方法等等可调用类型。用这个方法会比多个is*()更方便，不过它的实现仍然是用了多个is*()



> 获取对象信息

方法|说明
---|---
getmembers(object[, predicate])|这个方法是dir()的扩展版，它会将dir()找到的名字对应的属性一并返回，形如[(name, value), ...]。另外，predicate是一个方法的引用，如果指定，则应当接受value作为参数并返回一个布尔值，如果为False，相应的属性将不会返回。使用is\*作为第二个参数可以过滤出指定类型的属性。
getmodule(object)|还在为第2节中的`__module__`属性只返回字符串而遗憾吗？这个方法一定可以满足你，它返回object的定义所在的模块对象。
get{file/sourcefile}(object)|获取object的定义所在的模块的文件名/源代码文件名（如果没有则返回None）。用于内建的对象（内建模块、类、函数、方法）上时会抛出TypeError异常。
get{source/sourcelines}(object)| 获取object的定义的源代码，以字符串/字符串列表返回。代码无法访问时会抛出IOError异常。只能用于module/class/function/method/code/frame/traceack对象。
getargspec(func)| 仅用于方法，获取方法声明的参数，返回元组，分别是(普通参数名的列表, \*参数名, \*\*参数名, 默认值元组)。如果没有值，将是空列表和3个None。如果是2.6以上版本，将返回一个命名元组(Named Tuple)，即除了索引外还可以使用属性名访问元组中的元素。  
getargvalues(frame)|仅用于栈帧，获取栈帧中保存的该次函数调用的参数值，返回元组，分别是(普通参数名的列表, \*参数名, \*\*参数名, 帧的locals())。如果是2.6以上版本，将返回一个命名元组(Named Tuple)，即除了索引外还可以使用属性名访问元组中的元素。 
getmro(cls)|返回一个类型元组，查找类属性时按照这个元组中的顺序。如果是新式类，与cls.__mro__结果一样。但旧式类没有__mro__这个属性，直接使用这个属性会报异常，所以这个方法还是有它的价值的。 
currentframe()|返回当前的栈帧对象。


```python

```
