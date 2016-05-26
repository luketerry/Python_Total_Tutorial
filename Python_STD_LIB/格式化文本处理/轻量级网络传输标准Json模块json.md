
# 轻量级网络传输标准Json模块(json)

Json是当今网络数据传递的标准格式之一,python的标准变量类型与js十分相像因此有天然的Json支持,也就是他的json模块了


```python
import json
```

## 将python数据序列化为json

### 将python数据转化json格式字符串


```python
d = dict(name='Bob', age=20, score=88)
json.dumps(d)
```




    '{"name": "Bob", "score": 88, "age": 20}'



dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object

### 将python数据保存为json格式文件


```python
cont = json.dump(d,open('source/new.json', 'w'))
```

### 将json格式的字符串转化为python数据


```python
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
```


```python
json.loads(json_str)
```




    {'age': 20, 'name': 'Bob', 'score': 88}



### 读取json格式的文件转化为python数据


```python
json.load(open('source/new.json', 'r'))
```




    {'age': 20, 'name': 'Bob', 'score': 88}


