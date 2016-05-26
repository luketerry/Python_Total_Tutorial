
# 通用表格格式(csv)

csv是通用的表格格式,Python中提供了专门的包来处理它


```python
import csv
```

## 读取(`reader(csvfile, dialect='excel', **fmtparams)`)

+ dialect 

编码风格，默认为excel方式，也就是逗号(,)分隔，另外csv模块也支持excel-tab风格，也就是制表符(tab)分隔。其它的方式需要自己定义，然后可以调用register_dialect方法来注册，以及list_dialects方法来查询已注册的所有编码风格列表。

+ fmtparam

格式化参数，用来覆盖之前dialect对象指定的编码风格。


```python
with open('source/iris.csv',"r") as csvfile:
    spamreader = csv.reader(csvfile)
    line10 = [next(spamreader) for i in range(10)]
```


```python
line10
```




    [['5.1', '3.5', '1.4', '0.2', 'Iris-setosa'],
     ['4.9', '3.0', '1.4', '0.2', 'Iris-setosa'],
     ['4.7', '3.2', '1.3', '0.2', 'Iris-setosa'],
     ['4.6', '3.1', '1.5', '0.2', 'Iris-setosa'],
     ['5.0', '3.6', '1.4', '0.2', 'Iris-setosa'],
     ['5.4', '3.9', '1.7', '0.4', 'Iris-setosa'],
     ['4.6', '3.4', '1.4', '0.3', 'Iris-setosa'],
     ['5.0', '3.4', '1.5', '0.2', 'Iris-setosa'],
     ['4.4', '2.9', '1.4', '0.2', 'Iris-setosa'],
     ['4.9', '3.1', '1.5', '0.1', 'Iris-setosa']]



## 写入(`writer(csvfile[, dialect='excel'][, fmtparam])`)

+ dialect 

编码风格，默认为excel方式，也就是逗号(,)分隔，另外csv模块也支持excel-tab风格，也就是制表符(tab)分隔。其它的方式需要自己定义，然后可以调用register_dialect方法来注册，以及list_dialects方法来查询已注册的所有编码风格列表。

+ fmtparam

格式化参数，用来覆盖之前dialect对象指定的编码风格。


```python

with open('source/iris10.csv',"w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(line10)
```

##  读入字典格式(`DictReader(csvfile, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)`)



```python
with open('source/iris.csv',"r") as csvfile:
    spamreader = csv.DictReader(csvfile,fieldnames = ["a","b","c","d","class"])
    dic10 = [next(spamreader) for i in range(10)]
```


```python
dic10
```




    [{'a': '5.1', 'b': '3.5', 'c': '1.4', 'class': 'Iris-setosa', 'd': '0.2'},
     {'a': '4.9', 'b': '3.0', 'c': '1.4', 'class': 'Iris-setosa', 'd': '0.2'},
     {'a': '4.7', 'b': '3.2', 'c': '1.3', 'class': 'Iris-setosa', 'd': '0.2'},
     {'a': '4.6', 'b': '3.1', 'c': '1.5', 'class': 'Iris-setosa', 'd': '0.2'},
     {'a': '5.0', 'b': '3.6', 'c': '1.4', 'class': 'Iris-setosa', 'd': '0.2'},
     {'a': '5.4', 'b': '3.9', 'c': '1.7', 'class': 'Iris-setosa', 'd': '0.4'},
     {'a': '4.6', 'b': '3.4', 'c': '1.4', 'class': 'Iris-setosa', 'd': '0.3'},
     {'a': '5.0', 'b': '3.4', 'c': '1.5', 'class': 'Iris-setosa', 'd': '0.2'},
     {'a': '4.4', 'b': '2.9', 'c': '1.4', 'class': 'Iris-setosa', 'd': '0.2'},
     {'a': '4.9', 'b': '3.1', 'c': '1.5', 'class': 'Iris-setosa', 'd': '0.1'}]



##  写入字典格式(`DictWriter(csvfile, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)`)


```python
with open('source/iris_dic10.csv',"w") as csvfile:
    fieldnames = ["a","b","c","d","class"]
    writer = csv.DictWriter(csvfile,fieldnames = ["a","b","c","d","class"])
    writer.writeheader()
    writer.writerows(dic10)
```
