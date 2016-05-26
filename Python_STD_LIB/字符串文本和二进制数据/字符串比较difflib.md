
# 字符串比较(difflib)

difflib是python提供的比较序列(string list)差异的模块

主要实现了3个类:

+ SequenceMatcher 序列比较
+ Differ 字符串比较
+ HtmlDiff 将比较结果输出为html格式

## SequenceMatcher序列比较


```python
from difflib import SequenceMatcher
```


```python
a,b = 'hello world', 'HeLLO,wOrlD!'
```


```python
s = SequenceMatcher(None,a,b)
s.get_matching_blocks()
```




    [Match(a=1, b=1, size=1),
     Match(a=6, b=6, size=1),
     Match(a=8, b=8, size=2),
     Match(a=11, b=12, size=0)]




```python
s.get_opcodes()
```




    [('replace', 0, 1, 0, 1),
     ('equal', 1, 2, 1, 2),
     ('replace', 2, 6, 2, 6),
     ('equal', 6, 7, 6, 7),
     ('replace', 7, 8, 7, 8),
     ('equal', 8, 10, 8, 10),
     ('replace', 10, 11, 10, 12)]



## Differ 字符串比较


```python
from difflib import Differ
```


```python
diff = Differ().compare(a,b)
```


```python
list(diff)
```




    ['- h',
     '+ H',
     '  e',
     '- l',
     '- l',
     '- o',
     '-  ',
     '+ L',
     '+ L',
     '+ O',
     '+ ,',
     '  w',
     '- o',
     '+ O',
     '  r',
     '  l',
     '- d',
     '+ D',
     '+ !']



## HtmlDiff 将比较结果输出为html格式


```python
from difflib import HtmlDiff
```


```python
result = HtmlDiff.make_file(HtmlDiff(),a,b)
```


```python
with open("./hellostring.html","w") as f:
    f.write(result)
```


```python
f.close()
```
