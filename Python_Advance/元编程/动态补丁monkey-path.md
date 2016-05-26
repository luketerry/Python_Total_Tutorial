
# 动态补丁(monkey-path)

动态补丁是一种利用命名空间机制动态重载类,方法等对象的技术,它主要就是利用了Python没有命名空间这一特点.我们看个最简单的例子来理解动态重载


```python
class A(object):
    def a(self):
        print("old_a")
```


```python
AA = A()
```


```python
AA.a()
```

    old_a



```python
def a(self):
    print("new_a")
```


```python
A.a=a
```


```python
AA.a()
```

    new_a


monkey-path主要用在重载模块上,利用这个可以在runtime中替换模块中的一些行为,这在测试中会有用.
