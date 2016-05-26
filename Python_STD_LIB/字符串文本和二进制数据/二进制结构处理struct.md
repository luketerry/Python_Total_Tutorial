
# 二进制结构处理(struct)

有的时候需要用python处理二进制数据，比如，存取文件，socket操作时.这时候，可以使用python的struct模块来完成.可以用 struct来处理c语言中的结构体.

struct模块中最重要的三个函数是pack(), unpack(), calcsize():

+ pack(fmt, v1, v2, ...)     
按照给定的格式(fmt)，把数据封装成bytes(2.7中是str,实际上是类似于c结构体的字节流)
+ unpack(fmt, string)       
按照给定的格式(fmt)解析字节流bytes，返回解析出来的tuple
+ calcsize(fmt)                 
计算给定的格式(fmt)占用多少字节的内存

struct中支持的格式如下表：

Format|C Type|Python|字节数
---|---|---|---
x|pad byte|no value|---
c|char|string of length 1|1
b|signed char|integer|1
B|unsigned char|integer|1
?|\_Bool|bool|1
h|short|integer|2
H|unsigned short|nteger|2
i|int|integer|4
I|unsigned int|integer or long|4
l|long|integer|4
L|unsigned long|long|4
q|long long|long|8
Q|unsigned long long|long|8
n(3+)|ssize_t|integer|---
N(3+)|size_t|integer|---	 
f|float|float|4
d|double|float|8
s|char[]|bytes(2.7string)|---
p|char[]|bytes(2.7string)|---
P|void \*|	integer|---


注1.q和Q只在机器支持64位操作时有意思

注2.每个格式前可以有一个数字，表示个数

注3.s格式表示一定长度的字符串，4s表示长度为4的字符串，但是p表示的是pascal字符串

注4.P用来转换一个指针，其长度和机器字长相关

注5.最后一个可以用来表示指针类型的，占4个字节

为了同c中的结构体交换数据，还要考虑有的c或c++编译器使用了字节对齐，通常是以4个字节为单位的32位系统，故而struct根据本地机器字节顺序转换.可以用格式中的第一个字符来改变对齐方式.定义如下：

Character|	Byte order|	Size and alignment
---|---|---
@	|native	|native            凑够4个字节
=	|native	|standard        按原字节数
<	|little-endian	|standard        按原字节数
\>	|big-endian|standard       按原字节数
!	|network (= big-endian)|standard       按原字节数

使用方法是放在fmt的第一个位置，就像'@5s6sif'


```python
from struct import pack,unpack,calcsize
```

> `pack()`

pack把相应的数据类型变成bytes


```python
pack('f',12.34)
```




    '\xa4pEA'



如果是由多个数据构成的，可以这样：


```python
a='hello'

b='world!'

c=2

d=45.123

pack('5s6sif',a,b,c,d)
```




    'helloworld!\x00\x02\x00\x00\x00\xf4}4B'



>`unpack()`

unpack把bytes变成相应的数据类型：


```python
unpack("f",b'\xa4pEA')
```




    (12.34000015258789,)




```python
unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
```




    (4042322160, 32896)



>>例 一个bmp格式图片前30个字节

其格式为:

+ 一个4字节整数：表示位图大小；
+ 一个4字节整数：保留位，始终为0；
+ 一个4字节整数：实际图像的偏移量；
+ 一个4字节整数：Header的字节数；
+ 一个4字节整数：图像宽度；
+ 一个4字节整数：图像高度；
+ 一个2字节整数：始终为1；
+ 一个2字节整数：颜色数。


```python
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
```


```python
unpack('<ccIIIIIIHH', s)
```




    ('B', 'M', 691256, 0, 54, 40, 640, 360, 1, 24)


