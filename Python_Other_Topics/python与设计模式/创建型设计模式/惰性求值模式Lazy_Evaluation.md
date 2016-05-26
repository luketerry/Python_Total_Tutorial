
惰性求值属性可以在对象被使用的时候才进行计算,这样可以减少一些资源消耗,提高程序效率

应用场景:

类中有属性需要大量计算才可以得到结果,但又不想在实例化的时候就计算的场景

实现:通过装饰器实现


```python
def lazy(fn):
    """Decorator that makes a property lazy-evaluated."""
    attr_name = '_lazy_' + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)
    return _lazy_property

```


```python
class Person(object):
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    @lazy
    def relatives(self):
        # Get all relatives, let's assume that it costs much time.
        relatives = "Many relatives."
        return relatives

```


```python
Jhon = Person('Jhon', 'Coder')
```


```python
print("Name: {0}    Occupation: {1}".format(Jhon.name, Jhon.occupation))
```

    Name: Jhon    Occupation: Coder



```python

```
