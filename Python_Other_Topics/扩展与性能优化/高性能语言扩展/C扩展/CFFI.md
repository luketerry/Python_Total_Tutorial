
# pypy的官方C扩展(CFFI)

[CFFI](http://cffi.readthedocs.org/en/latest/)是pypy支持的一种c扩展写法,它当然也支持python2,python3,它的特点是c语言嵌入py文件,安装的时候直接编译,不用先预编译成.o文件

cffi有两种模式:

+ ABI The ABI mode accesses libraries at the binary level,

二进制码方式,这种方式是不安全的,主要原因也是C的编译器太多太杂又很多不兼容导致的.因为你不知道你的编译器究竟会编译出啥样来:它又分为两种使用形式:

        + in-line 即时编译使用
        + out-line 离线编译后调用



+ API mode accesses them with a C compiler 

通过api处理让c编译器编译,之后在形成python模块

> 在线的ABI模式


```python
from cffi import FFI
ffi = FFI()
#cdef用来定义结构体,变量,或者方法的声明
ffi.cdef("""
    int printf(const char *format, ...);   // copy-pasted from the man page
    """)
#dlopen是ABI模式的的基本读取方式
C = ffi.dlopen(None)                     # loads the entire C namespace
arg = ffi.new("char[]", "world")         # equivalent to C code: char arg[] = "world";
C.printf("hi there, %s.\n", arg)   
```




    17



> 在线API方式


```python
from cffi import FFI
ffi = FFI()
ffi.cdef("""
    int AIadd(int a, int b);   // copy-pasted from the man page
""")
#verify是在线api模式的基本方法它里面直接写C代码即可
lib = ffi.verify("""
    int AIadd(int a,int b){
        return a+b;
    }
""")
lib.AIadd(1,2)
```




    3



> 离线ABI方式


```python
%%writefile BO_example_build.py
#coding:utf-8
from cffi import FFI

ffi = FFI()
#set_source方法是离线方式的基本方法,它会生成一个第一位字符串为名字的.so文件用于python调用
ffi.set_source("BO_example", """

    int BOfac(int n) {
        if (n < 2)
            return 1;
        return n * BOfac(n - 1);
    }

""",source_extension='.c')
ffi.cdef("""
    int BOfac(int n);
""")

if __name__ == "__main__":
    #compile是离线方式的专用方法,它的作用是让编译器编译出可调用的.so文件
    ffi.compile()
```

    Overwriting BO_example_build.py



```python
!python BO_example_build.py
```


```python
from BO_example import ffi
lib = ffi.dlopen("BO_example.so")
lib.BOfac(10)
```




    3628800




```python
%timeit lib.BOfac(10)
```

    The slowest run took 28.71 times longer than the fastest. This could mean that an intermediate result is being cached 
    1000000 loops, best of 3: 208 ns per loop


> 离线API模式

离线API模式和ABI模式不同之处只在于API模式不再使用dlopen方法


```python
from BO_example import lib as libp
```


```python
libp.BOfac(10)
```




    3628800




```python
%timeit libp.BOfac(10)
```

    The slowest run took 31.80 times longer than the fastest. This could mean that an intermediate result is being cached 
    1000000 loops, best of 3: 195 ns per loop


看起来API模式基本和ABI模式效率差不多

我们看看pypy下的表现


```python
!pypy BO_example_build.py
```


```python
from BO_example import lib as libp
```


```python
libp.BOfac(10)
```




    3628800




```python
%timeit libp.BOfac(10)
```

    The slowest run took 172.96 times longer than the fastest. This could mean that an intermediate result is being cached.
    10000000 loops, best of 3: 61.9 ns per loop


爆炸啦!比c下快了3倍有余!

## 写setup


```python
%%writefile setup.py
from setuptools import setup

setup(
    name = "cffi_exa",
    setup_requires=["cffi>=1.0.0"],
    cffi_modules=["BO_example_build.py:ffi"],
    install_requires=["cffi>=1.0.0"],
)
```

    Overwriting setup.py



```python
!pypy setup.py install
```

    running install
    Checking .pth file support in /usr/local/Cellar/pypy/4.0.1/libexec/site-packages/
    /usr/local/bin/pypy -E -c pass
    TEST PASSED: /usr/local/Cellar/pypy/4.0.1/libexec/site-packages/ appears to support .pth files
    running bdist_egg
    running egg_info
    creating cffi_exa.egg-info
    writing cffi_exa.egg-info/PKG-INFO
    writing dependency_links to cffi_exa.egg-info/dependency_links.txt
    writing requirements to cffi_exa.egg-info/requires.txt
    writing top-level names to cffi_exa.egg-info/top_level.txt
    writing manifest file 'cffi_exa.egg-info/SOURCES.txt'
    reading manifest file 'cffi_exa.egg-info/SOURCES.txt'
    writing manifest file 'cffi_exa.egg-info/SOURCES.txt'
    installing library code to build/bdist.macosx-10.11-x86_64/egg
    running install_lib
    running build_ext
    generating cffi module 'build/temp.macosx-10.11-x86_64-2.7/BO_example.c'
    creating build
    creating build/temp.macosx-10.11-x86_64-2.7
    building 'BO_example' extension
    creating build/temp.macosx-10.11-x86_64-2.7/build
    creating build/temp.macosx-10.11-x86_64-2.7/build/temp.macosx-10.11-x86_64-2.7
    cc -arch x86_64 -O2 -fPIC -Wimplicit -I/usr/local/Cellar/pypy/4.0.1/libexec/include -c build/temp.macosx-10.11-x86_64-2.7/BO_example.c -o build/temp.macosx-10.11-x86_64-2.7/build/temp.macosx-10.11-x86_64-2.7/BO_example.o
    creating build/lib.macosx-10.11-x86_64-2.7
    cc -shared -undefined dynamic_lookup -arch x86_64 build/temp.macosx-10.11-x86_64-2.7/build/temp.macosx-10.11-x86_64-2.7/BO_example.o -o build/lib.macosx-10.11-x86_64-2.7/BO_example.pypy-26.so
    creating build/bdist.macosx-10.11-x86_64
    creating build/bdist.macosx-10.11-x86_64/egg
    copying build/lib.macosx-10.11-x86_64-2.7/BO_example.pypy-26.so -> build/bdist.macosx-10.11-x86_64/egg
    creating stub loader for BO_example.pypy-26.so
    byte-compiling build/bdist.macosx-10.11-x86_64/egg/BO_example.py to BO_example.pyc
    creating build/bdist.macosx-10.11-x86_64/egg/EGG-INFO
    copying cffi_exa.egg-info/PKG-INFO -> build/bdist.macosx-10.11-x86_64/egg/EGG-INFO
    copying cffi_exa.egg-info/SOURCES.txt -> build/bdist.macosx-10.11-x86_64/egg/EGG-INFO
    copying cffi_exa.egg-info/dependency_links.txt -> build/bdist.macosx-10.11-x86_64/egg/EGG-INFO
    copying cffi_exa.egg-info/requires.txt -> build/bdist.macosx-10.11-x86_64/egg/EGG-INFO
    copying cffi_exa.egg-info/top_level.txt -> build/bdist.macosx-10.11-x86_64/egg/EGG-INFO
    writing build/bdist.macosx-10.11-x86_64/egg/EGG-INFO/native_libs.txt
    zip_safe flag not set; analyzing archive contents...
    creating dist
    creating 'dist/cffi_exa-0.0.0-py2.7-macosx-10.11-x86_64.egg' and adding 'build/bdist.macosx-10.11-x86_64/egg' to it
    removing 'build/bdist.macosx-10.11-x86_64/egg' (and everything under it)
    Processing cffi_exa-0.0.0-py2.7-macosx-10.11-x86_64.egg
    Copying cffi_exa-0.0.0-py2.7-macosx-10.11-x86_64.egg to /usr/local/Cellar/pypy/4.0.1/libexec/site-packages
    Adding cffi-exa 0.0.0 to easy-install.pth file
    
    Installed /usr/local/Cellar/pypy/4.0.1/libexec/site-packages/cffi_exa-0.0.0-py2.7-macosx-10.11-x86_64.egg
    Processing dependencies for cffi-exa==0.0.0
    Searching for cffi==1.3.1
    Best match: cffi 1.3.1
    cffi 1.3.1 is already the active version in easy-install.pth
    
    Using /usr/local/Cellar/pypy/4.0.1/libexec/lib_pypy
    Finished processing dependencies for cffi-exa==0.0.0



```python
from BO_example import lib as libp
```


```python
libp.BOfac(10)
```




    3628800




```python

```
