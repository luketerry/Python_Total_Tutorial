
# 调用追踪(traceback)

调试的时候我们除了想知道哪条代码错了,也会想知道是谁调用了这条错误的代码,这个时候调用追踪模块就有用了

>一个简单的例子


```python
import traceback
def func():
    s =  traceback.extract_stack()
    print('%s Invoked me!'%s[-2][2])
    
def a():
    func()
b = lambda :func()
```


```python
a()
```

    a Invoked me!



```python
b()
```

    <lambda> Invoked me!


**注意:匿名函数即便赋值了还是匿名函数,所以无法追踪**
