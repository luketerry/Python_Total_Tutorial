
# HTML支持模块(html)

在2.7中html模块主要分为两个小模块:

模块名| 对应2.7中名字| 功能
---|---|---
html.parser|HTMLParser|html文本解析
html.entities| htmlentitydefs|html文本中实体的编码解码


```python
from __future__ import print_function
```

## html文本解析(html.parser) 

html.parser提供一个解析用的基类用来继承,通过定义handle来定义行为


```python
try: 
    from html.entities import entitydefs,name2codepoint,codepoint2name
except:
    from htmlentitydefs import entitydefs,name2codepoint,codepoint2name
```


```python
try: 
    from html.parser import HTMLParser
except:
    from HTMLParser import HTMLParser
```


```python
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('开始:',tag,"(属性:",attrs,")")

    def handle_endtag(self, tag):
        print('结束:', tag)

    def handle_startendtag(self, tag, attrs):
        print('独立标签:',tag,"(属性:",attrs,")")

    def handle_data(self, data):
        print("数据:",data)

    def handle_comment(self, data):
        print('注释', data)

    def handle_entityref(self, name):
        print('实体',chr(name2codepoint[name]))

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("字符编码:", c)
       
```


```python
parser = MyHTMLParser()
```


```python
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href="asf">html</a> HTML &nbsp;tutorial...<br>END</br></p>
</body></html>''')
```

    开始: html (属性: [] )
    数据: 
    
    开始: head (属性: [] )
    结束: head
    数据: 
    
    开始: body (属性: [] )
    数据: 
    
    注释  test html parser 
    数据: 
        
    开始: p (属性: [] )
    数据: Some 
    开始: a (属性: [('href', 'asf')] )
    数据: html
    结束: a
    数据:  HTML  tutorial...
    开始: br (属性: [] )
    数据: END
    结束: br
    结束: p
    数据: 
    
    结束: body
    结束: html


## html文本中实体的编码解码(html.entities)

> entitydefs 实体的常量字典


```python
list(map(lambda x:(x[0],x[1]),list(entitydefs.items())))[:5]# 名字->对应符号
```




    [('Ucirc', 'Û'), ('prop', '∝'), ('phi', 'φ'), ('radic', '√'), ('crarr', '↵')]




```python
list(map(lambda x:(x[0],x[1]),list(name2codepoint.items())))[:5]# 名字->对应编码
```




    [('Ucirc', 219), ('prop', 8733), ('rho', 961), ('hArr', 8660), ('radic', 8730)]




```python
list(map(lambda x:(x[0],x[1]),list(codepoint2name.items())))[:5]# 对应编码->名字
```




    [(8704, 'forall'),
     (8194, 'ensp'),
     (8707, 'exist'),
     (8709, 'empty'),
     (8711, 'nabla')]


