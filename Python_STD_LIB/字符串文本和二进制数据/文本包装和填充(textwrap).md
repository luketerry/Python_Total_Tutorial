
# 文本包装和填充(textwrap)

TextWrap提供函数:

+ wrap()
+ fill()
+ 工具函数dedent()
+ TextWrapper类

通常包装或者填充一两个字符串使用wrap()和fill()。其他情况使用TextWrapper更高效。 


```python
from textwrap import wrap,fill,dedent,TextWrapper
```


```python
sample_text = '''\
    The textwrap module can beused to format text for output in
    situations wherepretty-printing is desired.  It offers
    programmatic functionalitysimilar to the paragraph wrapping
    or filling features found inmany text editors.
'''
```

> `wrap(text[,width])`

包装单个段落(text为输入，系字符串)，每行最长宽度width。返回输出行的列表，最后行无换行符。Width默认70。


```python
wrap(sample_text,20)
```




    ['    The textwrap',
     'module can beused to',
     'format text for',
     'output in',
     'situations',
     'wherepretty-printing',
     'is desired.  It',
     'offers',
     'programmatic',
     'functionalitysimilar',
     'to the paragraph',
     'wrapping     or',
     'filling features',
     'found inmany text',
     'editors.']



> `fill(text[,width])`

包装单段文字，并返回包含包裹段落的字符串。实际上是"\n".join(wrap(text,...))的缩写。


```python
fill(sample_text,50)
```




    '    The textwrap module can beused to format text\nfor output in     situations wherepretty-printing\nis desired.  It offers     programmatic\nfunctionalitysimilar to the paragraph wrapping\nor filling features found inmany text editors.'



> `dedent(text)`

反缩进去掉每行行首空白


```python
dedent(sample_text)
```




    'The textwrap module can beused to format text for output in\nsituations wherepretty-printing is desired.  It offers\nprogrammatic functionalitysimilar to the paragraph wrapping\nor filling features found inmany text editors.\n'



## 实用代码

> 段落填充


```python
print('Nodedent:\n')
print(fill(sample_text, width=50))
```

    Nodedent:
    
        The textwrap module can beused to format text
    for output in     situations wherepretty-printing
    is desired.  It offers     programmatic
    functionalitysimilar to the paragraph wrapping
    or filling features found inmany text editors.


结果为左对齐，第一行有缩进。行中的空格继续保留

> 移除缩进


```python
print('Nodedent:\n')
print(dedent(sample_text))
```

    Nodedent:
    
    The textwrap module can beused to format text for output in
    situations wherepretty-printing is desired.  It offers
    programmatic functionalitysimilar to the paragraph wrapping
    or filling features found inmany text editors.
    


第一行就不会缩进了

> 移除缩进+填充


```python
for width in [ 45,70 ]:
    print(width,' Columns:\n' )
    print(fill(dedent(sample_text),width=width))
```

    (45, ' Columns:\n')
    The textwrap module can beused to format text
    for output in situations wherepretty-printing
    is desired.  It offers programmatic
    functionalitysimilar to the paragraph
    wrapping or filling features found inmany
    text editors.
    (70, ' Columns:\n')
    The textwrap module can beused to format text for output in situations
    wherepretty-printing is desired.  It offers programmatic
    functionalitysimilar to the paragraph wrapping or filling features
    found inmany text editors.


> 悬挂缩进：悬挂缩进第一行的缩进小于其他行的缩进。


```python
dedented_text =dedent(sample_text).strip()

print(fill(dedented_text,
           initial_indent='',
           subsequent_indent=' ' * 4,
           width=50))
```

    The textwrap module can beused to format text for
        output in situations wherepretty-printing is
        desired.  It offers programmatic
        functionalitysimilar to the paragraph wrapping
        or filling features found inmany text editors.


其中的’’*4还可以使用其他字符代替。
