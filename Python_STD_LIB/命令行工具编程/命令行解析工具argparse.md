
# 命令行解析工具(argparse)

计算机最基础的应用就是命令行工具了,用python写命令行工具可以使用argparse.它可以解析命令行参数,可以生成次级菜单等


```python
import argparse
```

## 基本命令

argparse模块的命令可以归结为就3条

+ `parser = argparse.ArgumentParser()`  创建命令行解析对象

+ `parser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])` 增加命令行参数

选项|说明
---|---
name or flags|命令行参数名或者选项，如上面的address或者-p,--port.其中命令行参数如果没给定，且没有设置defualt，则出错。但是如果是选项的话，则设置为None
nargs|命令行参数的个数，一般使用通配符表示，其中，'?'表示只用一个，'*'表示0到多个，'+'表示至少一个
default|默认值
type|参数的类型，默认是字符串string类型，还有float、int等类型
help|和ArgumentParser方法中的参数作用相似，出现的场合也一致


+ `parser.parse_args()` 解析命令行参数



## 一个简单的例子

我们来写一个可以实现两位整型数相加的命令行工具,它有`--help(-h)`和`--version(-v)`两个参数信息

代码如下:


```python
%%writefile sum.py
# !/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import print_function
import argparse

__version__=0.1

def sumarg(args):
    if args.sum:
        print(sum([int(i) for i in args.sum]))

def version(args):
    if args.version :
        print("version:"+str(__version__))

def argp():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sum", type=int,nargs='+', help="add the args ")
    parser.add_argument("-v","--version", help=u"get app's version",action="store_true")

    args = parser.parse_args()
    
    sumarg(args)
    version(args)

if __name__ == '__main__':
    argp()
```

    Overwriting sum.py



```python
!python sum.py -h
```

    usage: sum.py [-h] [--sum SUM [SUM ...]] [-v]
    
    optional arguments:
      -h, --help           show this help message and exit
      --sum SUM [SUM ...]  add the args
      -v, --version        get app's version



```python
!python sum.py -v
```

    version:0.1



```python
!python sum.py --sum 1 2 4
```

    7


**说明**:

1. type参数只是类型检验,传入的参数还是字符串

2. 不需要写usage

3. 有nargs参数的话获取的对应是一个list

4. 参数传入实际上是被存入了一个namespace的空间中这个空间有俩参数,其中一个是方法名命名的一个list,要调用使用即可:
    
        args.方法名
5. 如果参数中有只能接受一个的情况,可以加入判断

        if args.methodname1 == args.methodname1:  
            print 'usage: ' + __file__ + ' --help'  
            sys.exit(2)  
  

    来判断两个参数,要么都存在， 要么都不存在， 即可满足要求  




> 练习:写一个`rename`的命令行工具


```python

```
