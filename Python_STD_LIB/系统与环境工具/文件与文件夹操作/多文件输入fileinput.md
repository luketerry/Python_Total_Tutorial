
# 多文件输入(fileinput)

根据官方的说法,这个模块是用来做多文件输入的,对一个文件的话最好还是用`open()`


```python
import fileinput
```

> 输入(input)

    fileinput.input (files=None, inplace=False, backup='', bufsize=0, mode='r', openhook=None)
    
参数|说明
---|---
files| 文件的路径列表，默认是stdin方式，多文件('1.txt','2.txt',...}
inplace| 是否将标准输出的结果写回文件，默认不取代
backup| 备份文件的扩展名，只指定扩展名，如.bak。如果该文件的备份文件已存在，则会自动覆盖。
bufsize| 缓冲区大小，默认为0，如果文件很大，可以修改此参数，一般默认即可
mode| 读写模式，默认为只读
openhook| 该钩子用于控制打开的所有文件，比如说编码方式等;

常用方法:

方法|说明
---|---
fileinput.input()  |返回一个包含文件内容的生成器
fileinput.filename()|返回当前文件的名称
fileinput.lineno()  |返回当前已经读取的行的数量（或者序号）
fileinput.filelineno()|返回当前读取的行的行号
fileinput.isfirstline()|检查当前行是否是文件的第一行
fileinput.isstdin() |判断最后一行是否从stdin中读取
fileinput.close()   |关闭队列


```python
!find source
```

    source
    source/f1.txt
    source/f2.txt



```python
!cat source/f1.txt
```

    line1
    line2
    line3



```python
!cat source/f2.txt
```

    1line
    2line
    3line


> 多文件操作

先备份每个文件,之后每行后面加上一个`#`号


```python
def process(line):
    return line.rstrip() + '#'
 
with fileinput.input(('source/f1.txt','source/f2.txt'),inplace=True,backup = ".bak") as fs:
    for x in fs:
        print(process(x))
```


```python
!cat source/f1.txt
```

    line1##
    line2##
    line3##



```python
!cat source/f2.txt
```

    1line##
    2line##
    3line##



```python
!find source
```

    source
    source/f1.txt
    source/f1.txt.bak
    source/f2.txt
    source/f2.txt.bak

