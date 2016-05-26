
# 数组容器(array)

Python有List这个混合类型序列,而array则是它的固定类型序列

它的操作和list没什么不一样,但只能存放固定类型

声明的时候必须定义类型,后面则可以跟一个序列用于初始化赋值

类型:

Type code|	C Type	|Python Type	|Minimum size in bytes
---|---|---|---
'c'	|char|	character|	1
'b'|	signed char	|int|	1
'B'	|unsigned char	|int|	1
'u'	|Py_UNICODE	|Unicode character|	2 (see note)
'h'	|signed short|	int|	2
'H'	|unsigned short	|int|	2
'i'	|signed int	|int	|2
'I'	|unsigned int	|long	|2
'l'	|signed long	|int	|4
'L'	|unsigned long	|long	|4
'f'	|float	|float|	4
'd'	|double	|float|	8


```python
from array import array as A
import array
```

> 声明


```python
arr_int = A("i")
```

> 赋值


```python
arr_int.append(1)#一个一个添加
```


```python
arr_int.extend([2,3,4,5,6])
```


```python
arr_char = A("c",["a","s","d","f","g"])#申明+赋值
```


```python
arr_int
```




    array('i', [1, 2, 3, 4, 5, 6])




```python
arr_char
```




    array('c', 'asdfg')



> 可用方法

方法|说明
---|---
array.typecode|类型代码
array.itemsize|每个元素的字节数
array.append(x)|添加元素
array.buffer_info()|返回(address_id, length)
array.byteswap()|---
array.count(x)|x的出现次数
array.extend(iterable)|将一个序列从后面存入数组
array.fromfile(f, n)|从f文件中读取n个元素并从后面保存入数组
array.fromlist(list)|相当于`for x in list: a.append(x)`
array.fromstring(s)|类似上一个
array.fromunicode(s)|类似上一个
array.index(x)|x出现的第一个位置
array.insert(i, x)|插入操作
array.pop([i])|出栈
array.read(f, n)|已被fromfile取代
array.remove(x)|删除元素
array.reverse()|倒转
array.tofile(f)|存入文件
array.tolist()|返回对应列表
array.tostring()|返回字符串
array.tounicode()|返回unicode
array.write(f)|被tofile()取代




```python
type(lambda: None)
```




    function




```python

```
