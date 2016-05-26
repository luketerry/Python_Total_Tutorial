
看个例子:

车有牌子,有两厢有三厢车作为区分

那么可以看成这样的结构:

                     车
                     |
               |------------|
              大众          宝马
               |            |
            |=====|      |=====|
          两厢    三厢   两厢    三厢
          
          
这种结构可以看做是继承的一种

如果这样实现将会有很多的重复代码,怎么改呢?

我们将车分解为品牌和车型两个部分

         品牌-----------------车型
          |                    |
     |---------|           |--------|            
    大众      宝马         两厢      三厢
    
而每个车都是这两个属性的组合
            
桥接模式（Bridge）：将抽象部分与实现部分分离，使它们都可以独立的变化。什么叫抽象部分和实现部分分离？我们分析一下上面两种结构图，可以发现一个是用继承完成的，一种是用组合/聚合的方式完成的，而采用组合/聚合的方式就是所谓的抽象与实现分离。实际上在设计类时，我们应该首先考虑的是组合/聚合的方式，而不是考虑继承的方式，因为继承是一种强耦合关系，使用继承使得子类过多的依靠父类，这并不是很好。


那么什么时候使用桥接模式呢？当系统可以从多个角度分类，每一种分类都有可能变化，那么就把这种多角度分类分离出来让他们独立变化，这样就可以减少他们之间的耦合。


```python
class Mark(object):
    def __init__(self,mark):
        self.mark=mark
        

class Style(object):
    def __init__(self,style):
        self.style=style
        
class Car(object):
    def __init__(self,mark,style):
        self.mark = mark.mark
        self.style = style.style

```


```python
car1 = Car(Mark(u"大众"),Style(u"两厢"))
```


```python
print car1.mark
```

    大众


桥接模式在python中其实并不太需要,因为完全可以用多继承来实现...


```python
class Car2(Mark,Style):
    def __init__(self,mark,style):
        Mark.__init__(self,mark)
        Style.__init__(self,style)

```


```python
car2 = Car2(u"大众",u"两厢")
```


```python
print car2.mark
```

    大众

