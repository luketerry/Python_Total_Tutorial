
这个模式对我大天朝的人来说应该相当熟悉,代理嘛,没有他咱咋科学上网呢

它的原理简单说下,就是我们用一个代理作为中转,让代理替我们找我们需要的页面呀网站呀的,然后呢它把拿到的数据再传回来给我们

代理模式到底好处在哪里呢？？

　　那先要说一下代理模式中的三种角色了。

　　抽象角色：声明真实对象和代理对象的共同接口。
　　代理角色：代理对象角色内部含有对真实对象的引用，从而可以操作真实对象，同时代理对象提供与真实对象相同的接口以便在任何时刻都能代替真实对象。同时，代理对象　　　　　　　　可以在执行真实对象操作时，附加其他的操作，相当于对真实对象进行封装。
　　真实角色：代理角色所代表的真实对象，是我们最终要引用的对象。

　　代理模式的一个好处就是对外部提供统一的接口方法，而代理类在接口中实现对真实类的附加操作行为，从而可以在不影响外部调用情况下，进行系统扩展。也就是说，我要修改真实角色的操作的时候，尽量不要修改他，而是在外部在“包”一层进行附加行为，即代理类。例如：接口A有一个接口方法operator()，真实角色：RealA实现接口A，则必须实现接口方法operator()。客户端Client调用接口A的接方法operator()。现在新需求来了，需要修改RealA中的operator()的操作行为。怎么办呢？如果修改RealA就会影响原有系统的稳定性，还要重新测试。这是就需要代理类实现附加行为操作。创建代理ProxyA实现接口A，并将真实对象RealA注入进来。ProxyA实现接口方法operator()，另外还可以增加附加行为，然后调用真实对象的operator()。从而达到了“对修改关闭，对扩展开放”，保证了系统的稳定性。我们看客户端Client调用仍是接口A的接口方法operator()，只不过实例变为了ProxyA类了而已。也就是说代理模式实现了ocp原则。

当我们需要使用的对象很复杂或者需要很长时间去构造，这时就可以使用代理模式(Proxy)。例如：如果构建一个对象很耗费时间和计算机资源，代理模式(Proxy)允许我们控制这种情况，直到我们需要使用实际的对象。一个代理(Proxy)通常包含和将要使用的对象同样的方法，一旦开始使用这个对象，这些方法将通过代理(Proxy)传递给实际的对象。 一些可以使用代理模式(Proxy)的情况：

　　一个对象，比如一幅很大的图像，需要载入的时间很长。　　　　

　　一个需要很长时间才可以完成的计算结果，并且需要在它计算过程中显示中间结果

　　一个存在于远程计算机上的对象，需要通过网络载入这个远程对象则需要很长时间，特别是在网络传输高峰期。

　　一个对象只有有限的访问权限，代理模式(Proxy)可以验证用户的权限

　　代理模式(Proxy)也可以被用来区别一个对象实例的请求和实际的访问，例如：在程序初始化过程中可能建立多个对象，但并不都是马上使用，代理模式(Proxy)可以载入需要的真正的对象。这是一个需要载入和显示一幅很大的图像的程序，当程序启动时，就必须确定要显示的图像，但是实际的图像只能在完全载入后才可以显示！这时我们就可以使用代理模式(Proxy)。


```python
import time

#卖家
class SalesManager:
    def work(self):
        print("Sales Manager working...")

    def talk(self):
        print("Sales Manager ready to talk")

#代理
class Proxy:
    def __init__(self):
        self.busy = 'No'
        self.sales = None

    def work(self):
        print("Proxy checking for Sales Manager availability")
        if self.busy == 'No':
            self.sales = SalesManager()
            time.sleep(2)
            self.sales.talk()
        else:
            time.sleep(2)
            print("Sales Manager is busy")

#具体的代理
class NoTalkProxy(Proxy):
    def __init__(self):
        Proxy.__init__(self)

    def work(self):
        print("Proxy checking for Sales Manager availability")
        time.sleep(2)
        print("This Sales Manager will not talk to you whether he/she is busy or not")


def main():
    p = Proxy()
    p.work()
    p.busy = 'Yes'
    p.work()
    p = NoTalkProxy()
    p.work()
    p.busy = 'Yes'
    p.work()
main()
```

    Proxy checking for Sales Manager availability
    Sales Manager ready to talk
    Proxy checking for Sales Manager availability
    Sales Manager is busy
    Proxy checking for Sales Manager availability
    This Sales Manager will not talk to you whether he/she is busy or not
    Proxy checking for Sales Manager availability
    This Sales Manager will not talk to you whether he/she is busy or not



```python

```
