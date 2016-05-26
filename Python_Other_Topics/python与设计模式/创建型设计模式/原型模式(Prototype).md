
大家都知道连锁机构是现在灰常流行的商业模式，比如星巴克,kfc啥的，那么假如星巴克要在小南通新建立一个分店，所经营的产品和以前在其他的城市已经存在的店经营的产品差不多，那么面向对象开发的角度怎么解决这个问题呢？难道要重新的实例化一个咖啡之翼的店？？这显然不太好吧，星巴克里面经营的产品（假设是属性吧）都需要重新写，这就是在做大量的重复工作啊，这显然是不符合OO开发思想的。遇到这样的情况，并不是重新建立一个类来解决这样的问题，而是通过设计模式中的“原型模式”来解决这种问题。(js貌似就是这种理念的面向对象模型)

原型模式需要用到copy这个库做深层拷贝.

原型模式适用场合：

原型模式在几个方面比较有效：

1. 如果说我们的对象类型不是刚开始就可以确定，而是这个类型是在运行期确定的话，那么我们通过这个类型的对象克隆出一个新的类型更容易。

2. 有的时候我们可能在实际的项目中需要一个对象在某个状态下的副本

3. 当我们在处理一些对象比较简单，并且对象之间的区别很小，可能只是很固定的几个属性不同的时候，可能我们使用原型模式更合适。

注：东西不要学死，重要的是理解不是背诵，原型模式还有其他可用的场合，要理解原型模式的原理，这样才能真正地为我所用，这只是一种思想，可能在很多地方好用，只有真正地理解才能在以后的实践中提出新的看法。


```python
import copy


class Prototype:

    value = 'default'

    def clone(self, **attrs):
        """Clone a prototype and update inner attributes dictionary"""
        obj = copy.deepcopy(self)
        obj.__dict__.update(attrs)
        return obj


class PrototypeDispatcher:
    #记录原型和它的拷贝
    def __init__(self):
        self._objects = {}

    def get_objects(self):
        """Get all objects"""
        return self._objects

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]


def main():
    dispatcher = PrototypeDispatcher()
    prototype = Prototype()

    d = prototype.clone()
    a = prototype.clone(value='a-value', category='a')
    b = prototype.clone(value='b-value', is_checked=True)
    dispatcher.register_object('objecta', a)
    dispatcher.register_object('objectb', b)
    dispatcher.register_object('default', d)
    print([{n: p.value} for n, p in dispatcher.get_objects().items()])


main()
```

    [{'default': 'default'}, {'objecta': 'a-value'}, {'objectb': 'b-value'}]



```python

```
