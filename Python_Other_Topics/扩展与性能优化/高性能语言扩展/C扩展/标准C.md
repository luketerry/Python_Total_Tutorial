
# C 扩展 

Python是C写的,许多时候他被作为浇水语言,与C联合使用,在一般的时候,Python的性能已经足够了,但有时候性能不够我们就需要C来扩展了.

我们来看看python写的原型:


```python
def fac(n):
    if n<2 :
        return 1
    return n*fac(n-1)
```


```python
fac(10)
```




    3628800




```python
%timeit fac(10)#pypy
```

    The slowest run took 98.61 times longer than the fastest. This could mean that an intermediate result is being cached.
    1000000 loops, best of 3: 414 ns per loop
    Compiler time: 549755.81 s



```python
%timeit fac(10)#python2
```

    The slowest run took 4.84 times longer than the fastest. This could mean that an intermediate result is being cached 
    100000 loops, best of 3: 1.87 µs per loop


##  官方给的标准写扩展的c程序


```python
%%writefile test.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFSIZE 10

int fac(int n) {
    if (n < 2)
        return 1;
    return n * fac(n - 1);
}

char *reverse(char *s) {
    register char t;
    char *p = s;
    char *q = (s + (strlen(s) - 1));
    while (p < q) {
        t = *p;
        *p++ = *q;
        *q-- = t;
    }
    return s;
}

int main() {
    char s[BUFSIZE];
    printf("4! == %d\n", fac(4));
    printf("8! == %d\n", fac(8));
    printf("12! == %d\n", fac(12));
    strcpy(s, "abcdef");
    printf("reversing 'abcdef', we get '%s'\n", reverse(s));
    strcpy(s, "madam");
    printf("reversing 'madam', we get '%s'\n", reverse(s));
    return 0;
}
```

    Writing test.c



```python
!gcc test.c -o test
```


```python
!./test
```

    4! == 24
    8! == 40320
    12! == 479001600
    reversing 'abcdef', we get 'fedcba'
    reversing 'madam', we get 'madam'


在python的include文件夹下的python2.X中找到python.h
放到文件夹下,并在上面的c代码中加入

    #include "Python.h"


```python
%%writefile Extest.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Python.h"
#define BUFSIZE 10

//原始函数
int fac(int n) {
    if (n < 2)
        return 1;
    return n * fac(n - 1);
}

char *reverse(char *s) {
    register char t;
    char *p = s;
    char *q = (s + (strlen(s) - 1));
    while (p < q) {
        t = *p;
        *p++ = *q;
        *q-- = t;
    }
    return s;
}

//包装函数,为每个模块的每一个函数增加一个型如PyObject* Module_func()的包装函数

static PyObject *
Extest_fac(PyObject *self, PyObject *args) {
    int res;
    int num;
    PyObject* retval;

    res = PyArg_ParseTuple(args, "i", &num);
    if (!res) {
        return NULL;
    }
    res = fac(num);
    retval = (PyObject *)Py_BuildValue("i", res);
    return retval;
}

static PyObject *
Extest_reverse(PyObject *self, PyObject *args) {
    char *orignal;
    if (!(PyArg_ParseTuple(args, "s", &orignal))) {
        return NULL;
    }
    return (PyObject *)Py_BuildValue("s", reverse(orignal));
}

//可以返回原始字符串和翻转字符串
static PyObject *
Extest_doppel(PyObject *self, PyObject *args) {
    char *orignal;
    char *resv;
    PyObject *retval;
    if (!(PyArg_ParseTuple(args, "s", &orignal))) {
        return NULL;
    }
    retval = (PyObject *)Py_BuildValue("ss", orignal, resv=reverse(strdup(orignal)));
    free(resv);
    return retval;
}

//注册方法
static PyMethodDef 
ExtestMethods[] = {
    {"fac", Extest_fac, METH_VARARGS},
    {"doppel", Extest_doppel, METH_VARARGS},
    {"reverse", Extest_reverse, METH_VARARGS},
    {NULL, NULL},
};

//初始化模块
void initExtest() {
    Py_InitModule("Extest", ExtestMethods);
}

//测试函数

int test() {
    char s[BUFSIZE];
    printf("4! == %d\n", fac(4));
    printf("8! == %d\n", fac(8));
    printf("12! == %d\n", fac(12));
    strcpy(s, "abcdef");
    printf("reversing 'abcdef', we get '%s'\n", reverse(s));
    strcpy(s, "madam");
    printf("reversing 'madam', we get '%s'\n", reverse(s));
    return 0;
}

static PyObject *
Extest_test(PyObject *self, PyObject *args) {
    test();
    //返回空的话，就使用下面这一句 
    return (PyObject *)Py_BuildValue("");
}

```

    Writing Extest.c


Python与c中对应类型转换参数表:

format code| python type |c type
--|--|--
s|str|char\*
z|str/None|char\*/NULL
i|int|int
l|long|long
c|str|char
d|float|double
D|complex|Py_Complex\*
O|(any)|PyObject\*
S|str|PyStringObject

Py_BuildValue的用法表:


用法|结果
---|---
Py_BuildValue("")                       | None
Py_BuildValue("i", 123)                  |123
Py_BuildValue("iii", 123, 456, 789)     | (123, 456, 789)
Py_BuildValue("s", "hello")             | 'hello'
Py_BuildValue("y", "hello")              |b'hello'
Py_BuildValue("ss", "hello", "world")   | ('hello', 'world')
Py_BuildValue("s#", "hello", 4)        |  'hell'
Py_BuildValue("y#", "hello", 4)         | b'hell'
Py_BuildValue("()")                     | ()
Py_BuildValue("(i)", 123)               | (123,)
Py_BuildValue("(ii)", 123, 456)          |(123, 456)
Py_BuildValue("(i,i)", 123, 456)         |(123, 456)
Py_BuildValue("[i,i]", 123, 456)         |[123, 456]
Py_BuildValue("{s:i,s:i}","abc", 123, "def", 456)    |{'abc': 123, 'def': 456}
Py_BuildValue("((ii)(ii)) (ii)",1, 2, 3, 4, 5, 6)          |(((1, 2), (3, 4)), (5, 6))

>编译与测试
>>创建setup.py


```python
%%writefile setup.py
#!/usr/bin/env python
from distutils.core import setup, Extension
MOD = 'Extest'
setup(name=MOD, ext_modules=[Extension(MOD, sources=['Extest.c'])])
```

    Overwriting setup.py


>> 生成.so文件


```python
!python setup.py build
```

    running build
    running build_ext
    building 'Extest' extension
    creating build
    creating build/temp.macosx-10.5-x86_64-2.7
    gcc -fno-strict-aliasing -I/Users/huangsizhe/Lib/conda/anaconda/include -arch x86_64 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/huangsizhe/Lib/conda/anaconda/include/python2.7 -c Extest.c -o build/temp.macosx-10.5-x86_64-2.7/Extest.o
    [1mExtest.c:95:1: [0m[0;1;35mwarning: [0m[1munused function 'Extest_test' [-Wunused-function][0m
    Extest_test(PyObject *self, PyObject *args) {
    [0;1;32m^
    [0m1 warning generated.
    creating build/lib.macosx-10.5-x86_64-2.7
    gcc -bundle -undefined dynamic_lookup -L/Users/huangsizhe/Lib/conda/anaconda/lib -arch x86_64 -arch x86_64 build/temp.macosx-10.5-x86_64-2.7/Extest.o -L/Users/huangsizhe/Lib/conda/anaconda/lib -o build/lib.macosx-10.5-x86_64-2.7/Extest.so


生成的文件在build文件夹下


```python
!find build
```

    build
    build/lib.macosx-10.5-x86_64-2.7
    build/lib.macosx-10.5-x86_64-2.7/Extest.so
    build/temp.macosx-10.5-x86_64-2.7
    build/temp.macosx-10.5-x86_64-2.7/Extest.o


>> 安装模块到第三方库


```python
!python setup.py install
```

    running install
    running build
    running build_ext
    running install_lib
    copying build/lib.macosx-10.5-x86_64-2.7/Extest.so -> /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages
    running install_egg_info
    Removing /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/Extest-0.0.0-py2.7.egg-info
    Writing /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/Extest-0.0.0-py2.7.egg-info


>> 测试使用


```python
import Extest
```


```python
Extest.doppel("ahl")
```




    ('ahl', 'lha')




```python
%timeit Extest.fac(10)
```

    The slowest run took 12.47 times longer than the fastest. This could mean that an intermediate result is being cached 
    1000000 loops, best of 3: 249 ns per loop


这个速度已经相当可观了,大约是pypy的3倍快

速度测试结果:

平台|方法|速度
---|---|---
pthon2|fac10|1.87 µs
pypy|fac10|414 ns
python2扩展|fac10|249ns
