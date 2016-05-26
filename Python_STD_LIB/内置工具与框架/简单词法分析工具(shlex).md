
# 简单shell词法分析工具(shlex)

词法分析是编译中的一个很重要的步骤,Python中提供了shlex模块用来做词法分析,用于分析shell中的输入语法,
shlex基本只提供一个分词的功能和识别引号的功能

> 例:解析一串字符串,以`,`分割,但引号内的`,`不用于分割


```python
import shlex
strin=shlex.shlex("ab,'cdsfd,sfsd',ewewq,5654",posix=True)
strin.whitespace=','
strin.whitesapce_split=True
b=list(strin)
print(b)
```

    ['ab', 'cdsfd,sfsd', 'ewewq', '5654']


> split方法可以在用多种空白的时候解析


```python
import shlex
strin2=shlex.split("ab 'cdsfd  sfsd'   ewewq 5654",posix=True)

b=list(strin)
print(b)
```

    ['ab', 'cdsfd  sfsd', 'ewewq', '5654']

