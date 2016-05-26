
生活中大家一定遇到过这样的情况：某一件事情的状态改变，会相应的引起其他相关的变化,比如天冷了人们就加衣服,天热了就脱衣服.

这里气温就是被观察者,它的状态改变会让观察者们改变状态

人们呢就是观察者了,人们通过观察气温的改变改变自己的状态

GoF对观察者模式定义：定义对象间的一种一对多的依赖关系，当一个对象的状态发生改变时，所有依赖于它的对象都得到通知并被自动更新。

实际上，观察者模式又被成为发布/订阅模式，在这种模式中，一个目标物件（被观察者）管理所有相依于它的相关物件（观察者），并且在目标物件的状态改变时主动发出通知。这通常透过使用各相关物件所提供的方法来实现，观察者模式模式通常被用来作事件处理系统。


使用观察者模式的场合和好处

　　以下情况使可以考虑使用观察者模式：

　　（1）当一个抽象模型有两个方面，其中一个方面依赖另一个方面，这时使用观察者模式可以将这两个者封装在独立的对象中使他们各自独立的改变和复用。

　　（2）当一个对象的改变要影响到其他对象，而且不知道有多少的对象需要改变。

　　（3）当一个对象必须通知其它对象，而它又不能假定其它对象是谁。换言之, 你不希望这些对象是紧密耦合的。

　　那么使用观察者模式有什么好处呢？主要是降低了系统中各个对象之间的耦合性，使得系统易于扩展。总的来说：

　　（1）使用面向对象的抽象，观察者模式使得我们可以独立地改变目标与观察者，从而使二者之间的依赖关系达到松耦合。

　　（2）目标发送通知时，无需指定观察者，通知（可以携带通知信息作为参数）会自动传播。观察者自己决定是否需要订阅通知。目标对象对此一无所知。

　　（3）在C#中的Event。委托充当了抽象的Observer接口，而提供事件的对象充当了目标对象，委托是比抽象Observer接口更为松耦合的设计。

下面的例子是一个典型的例子观察者是两个view,被观察者是data,被观测者会像观测者发送消息


```python
class Subject(object):

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


# Example usage
class Data(Subject):

    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


class HexViewer:

    def update(self, subject):
        print('HexViewer: Subject %s has data 0x%x' %
              (subject.name, subject.data))


class DecimalViewer:

    def update(self, subject):
        print('DecimalViewer: Subject %s has data %d' %
              (subject.name, subject.data))


# Example usage...
def main():
    data1 = Data('Data 1')
    data2 = Data('Data 2')
    view1 = DecimalViewer()
    view2 = HexViewer()
    data1.attach(view1)
    data1.attach(view2)
    data2.attach(view2)
    data2.attach(view1)

    print("Setting Data 1 = 10")
    data1.data = 10
    print("Setting Data 2 = 15")
    data2.data = 15
    print("Setting Data 1 = 3")
    data1.data = 3
    print("Setting Data 2 = 5")
    data2.data = 5
    print("Detach HexViewer from data1 and data2.")
    data1.detach(view2)
    data2.detach(view2)
    print("Setting Data 1 = 10")
    data1.data = 10
    print("Setting Data 2 = 15")
    data2.data = 15



main()
```

    Setting Data 1 = 10
    DecimalViewer: Subject Data 1 has data 10
    HexViewer: Subject Data 1 has data 0xa
    Setting Data 2 = 15
    HexViewer: Subject Data 2 has data 0xf
    DecimalViewer: Subject Data 2 has data 15
    Setting Data 1 = 3
    DecimalViewer: Subject Data 1 has data 3
    HexViewer: Subject Data 1 has data 0x3
    Setting Data 2 = 5
    HexViewer: Subject Data 2 has data 0x5
    DecimalViewer: Subject Data 2 has data 5
    Detach HexViewer from data1 and data2.
    Setting Data 1 = 10
    DecimalViewer: Subject Data 1 has data 10
    Setting Data 2 = 15
    DecimalViewer: Subject Data 2 has data 15

