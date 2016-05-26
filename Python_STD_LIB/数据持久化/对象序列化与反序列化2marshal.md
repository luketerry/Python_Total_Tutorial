
# 对象序列化与反序列化2(marshal)

这个模块一样版本不兼容,而且往往不是推荐的序列化工具因为支持序列化的类型太少,它的存在意义主要是为`.pyc`文件服务



```python
from marshal import dump, load, dumps,loads
```

## 将对象写入文件(`dump(obj,file)`)


```python
exa_l=[1,2,3,4,5]
```


```python
with open("./marshal_test.txt","wb") as f:
    dump(exa_l,f)
```

## 将文件中的对象反序列化(`load(f)`)


```python
with open("./marshal_test.txt","rb") as f:
    view_exam = load(f)
```


```python
view_exam
```




    [1, 2, 3, 4, 5]



## 将数据序列化为二进制流(`dumps(obj)`)


```python
exa_b = dumps(exa_l)
```


```python
exa_b
```




    b'\xdb\x05\x00\x00\x00\xe9\x01\x00\x00\x00\xe9\x02\x00\x00\x00\xe9\x03\x00\x00\x00\xe9\x04\x00\x00\x00\xe9\x05\x00\x00\x00'



## 将二进制流转化为对象(loads(bytes))


```python
view_exa=loads(exa_b)
```


```python
view_exa
```




    [1, 2, 3, 4, 5]


