
# 用types与动态链接库交互

[ctypes](https://docs.python.org/2/library/ctypes.html)是原版python和pypy都支持的一种与动态链接库(就是.so或者.dll那个文件)交互的方式,因此它也是最方便的一种与c语言混合编程的方式.c还是那个c,python还是那个python,不用再学其他的了,这也是简单情况下最推荐的一种与c直接交互的方式.

ctypes 有以下优点：

+ Python内建，不需要单独安装
+ 可以直接调用二进制的动态链接库 
+ 对基本类型的相互映射有良好的支持

ctypes 有以下缺点：

+ 平台兼容性差
+ 不能够直接调用动态链接库中未经导出的函数或变量
+ 对C++的支持差


**事先申明:**本文写在mac osx平台,使用的编译工具是clang,其他平台都没试过,有兴趣的小朋友可以自己摸索下

> 例子:一个二维向量运算

### c代码:

v.c

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//向量结构体
typedef struct{
    float x,y;
    char repr[50];
}Vector;

Vector add(Vector a,Vector b){
    Vector c;
    c.x = a.x+b.x;
    c.y = a.y+b.y;
    char tempx[10];
    char tempy[10];
    //char x = itoa(c.x,&tempx,10);
    //char y = itoa(c.y,&tempy,10);
    int len = sprintf(c.repr, "<x:%f,y:%f>\n",c.x,c.y);
    //c.repr = "<x:" + x + "," + "y:" + y + ">";
    return c;
}

int main(void){
    Vector a,b,c;
    a.x = 10.0;
    a.y = 20.0;
    strcpy(a.repr,"<x:10.0,y:20.0>");

    b.x = 1.0;
    b.y = 2.0;
    strcpy(b.repr,"<x:10.0,y:20.0>");
    c = add(a,b);
    printf("x %f y %f\n",c.x,c.y);
    printf("%s\n",c.repr);
    return 0;
}
```

编译运行下:

```bash
gcc v.c -o vtest
./vtest
```

结果正常

### 修改成动态链接库(把那个显示结果的省了)

vector.h

```c
#ifndef VECTOR_HEAD_
#define VECTOR_HEAD_

//向量结构体
typedef struct{
    float x,y;
}Vector;

//向量加法
Vector add(Vector a,Vector b);

#endif
```

vector.c

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "vector.h"

//向量结构体
Vector add(Vector a,Vector b){
    Vector c;
    c.x = a.x+b.x;
    c.y = a.y+b.y;
    return c;
}
```
编译成动态链接库

```bash
gcc -shared -fPIC -o libvec.so vector.c
```

这样就生成一个v.so文件,我们先来用c语言试试看调用

vectorTest.c

```c
#include <stdio.h>
#include <string.h>

#include "vector.h"

int main(void){
    Vector a,b,c;
    a.x = 10.0;
    a.y = 20.0;

    b.x = 1.0;
    b.y = 2.0;
    c = add(a,b);
    printf("x %f y %f\n",c.x,c.y);
    return 0;
}
```

编译:

```bash
gcc vectorTest.c -o vectorTest -L ./ -lvec
./vectorTest
```

结果正常

### 用ctypes调用这个动态链接库

到正题了,我们用这个ctypes调用下动态库试试


```python
from ctypes import CDLL,c_float,c_char_p,Structure,POINTER,c_int,pointer
```


```python
class Vector(Structure):
    _fields_ = [("x",c_float),("y",c_float)]
    def __str__(self):
        return "Vector:<{this.x},{this.y}>".format(this=self)
    def __repr__(self):
        return self.__str__()
    def __add__(self,that):
        dll = CDLL("libvec.so")
        dll.add.argtypes = (Vector,Vector)
        dll.add.restype = Vector
        return dll.add(self,that)
```


```python
v1 = Vector(1,2)
```


```python
v1
```




    Vector:<1.0,2.0>




```python
v2 = Vector(10,20)
```


```python
v2
```




    Vector:<10.0,20.0>




```python
v3 = v1+v2
```


```python
v3
```




    Vector:<11.0,22.0>



可喜可贺~~

## ctypes内置数据类型映射:


ctypes type|c type|Python type
---|---|---
c_char|char	|1-character string
c_wchar	|wchar_t	|1-character unicode string
c_byte	|char	|int/long
c_ubyte	|unsigned char	|int/long
c_short	|short	|int/long
c_ushort	|unsigned short	|int/long
c_int	|int	|int/long
c_uint	|unsigned int	|int/long
c_long	|long	|int/long
c_ulong	|unsigned long	|int/long
c_longlong	|__int64 or long long	|int/long
c_ulonglong	|unsigned __int64 or unsigned long long	|int/long
c_float	|float	|float
c_double	|double	|float
c_char_p	|char * (NUL terminated)	|string or None
c_wchar_p	|wchar_t * (NUL terminated)	|unicode or None
c_void_p	|void *|int/long or None

需要注意的是:
+ 关于指定映射类型,如果指定c中的返回值类型,则是`dll.FUNCNAME.restype = TYPE`,如果函数的返回值是`void`那么你可以赋值为 `None`,如果不设定,则默认是`int`类型;
+ 如果是传入参数类型指定,则使用`dll.FUNCNAME.argtypes = (TYPE1, TYPE2...)`

## ctypes 和 指针

如何创建一个 ctypes 的指针呢？这里有三个跟指针有个的 ctypes 里的函数，

函数	|说明
---|---
byref(x [, offset])	|返回 x 的地址，x 必须为 ctypes 类型的一个实例。相当于 c 的 &x 。 offset 表示偏移量。
pointer(x)	|创建并返回一个指向 x 的指针实例， x 是一个实例对象。
POINTER(type)	|返回一个类型，这个类型是指向 type 类型的指针类型， type 是 ctypes 的一个类型。



byref 很好理解，传递参数的时候就用这个，用 pointer 创建一个指针变量也行，不过 byref 更快。

而 pointer 和 POINTER 的区别是，pointer 返回一个实例，POINTER 返回一个类型。甚至你可以用 POINTER 来做 pointer 的工作：


```python
a = c_int(6)         # 创建一个 c_int 实例
```


```python
a
```




    c_int(6)




```python
b = pointer(a)        # 创建指针
```


```python
b
```




    <__main__.LP_c_int at 0x103d618c0>




```python
c = POINTER(c_int)(a) # 创建指针
```


```python
c
```




    <__main__.LP_c_int at 0x103d70050>




```python
b.contents #输出 a 的值
```




    c_int(6)




```python
c.contents            # 输出 a 的值
```




    c_int(6)




```python
pointer(v3)
```




    <__main__.LP_Vector at 0x103d704d0>




```python
POINTER(Vector)(v3)
```




    <__main__.LP_Vector at 0x103d70560>




```python
POINTER(Vector)(v3).contents
```




    Vector:<11.0,22.0>




```python
POINTER(Vector)(v3).contents.x
```




    11.0


