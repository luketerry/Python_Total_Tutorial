
线程安全是多线程编程中最不容易的事儿,线程间同步,互斥数据共享一直是要考虑的问题,而最常见的就是用队列实现管理线程了

该模块在2和3中并不相同,2中叫Queue,3中叫queue


```python
from __future__ import print_function,unicode_literals,division
try: 
    import Queue
except:
    import queue as Queue
import threading
import random
```


```python
class Producer(threading.Thread):
    """生产者"""
    def __init__(self,q,con,name):
        super(Producer,self).__init__()
        self.q = q
        self.name = name
        self.con = con
        print("生产者{self.name}产生了".format(self=self))
        
    def run(self):
        while True:
            #global writelock
            self.con.acquire()
            if self.q.full():

                print("队列满了,生产者等待")
                self.con.wait()
            else:
                value = random.randint(0,10)

                print("{self.name}把值{self.name}:{value}放入了队列".format(self=self,
                                                                         value=value))
            self.q.put("{self.name}:{value}".format(self=self,value=value))
            self.con.notify()
        self.con.release()
            
```


```python
class Consumer(threading.Thread):
    """消费者"""
    def __init__(self,q,con,name):
        super(Consumer,self).__init__()
        self.q = q
        self.name = name
        self.con = con
        print("消费者{self.name}产生了".format(self=self))
        
    def run(self):
        while True:
            #global writelock
            self.con.acquire()
            if self.q.empty():

                print("队列空了,消费者等待")
                self.con.wait()
            else:
                value = self.q.get()

                print("{self.name}从队列中获取了{self.name}:{value}".format(self=self,
                                                                         value=value))
                self.con.notify()
            self.con.release()    
```


```python
q = Queue.Queue(10)
con = threading.Condition()
p1 = Producer(q,con,"P1")
p1.start()
p2 = Producer(q,con,"P2")
p2.start()
c1 = Consumer(q,con,"C1")
c1.start()
```

    生产者P1产生了
    P1把值P1:10放入了队列
    P1把值P1:10放入了队列
    P1把值P1:0放入了队列
    P1把值P1:7放入了队列
    P1把值P1:7放入了队列
    P1把值P1:2放入了队列
    P1把值P1:7放入了队列
    P1把值P1:0放入了队列
    P1把值P1:7放入了队列
    P1把值P1:4放入了队列
    队列满了,生产者等待
    生产者P2产生了
    队列满了,生产者等待
    消费者C1产生了
    C1从队列中获取了C1:P1:10
    C1从队列中获取了C1:P1:10
    C1从队列中获取了C1:P1:0
    C1从队列中获取了C1:P1:7
    C1从队列中获取了C1:P1:7
    C1从队列中获取了C1:P1:2
    C1从队列中获取了C1:P1:7
    C1从队列中获取了C1:P1:0
    C1从队列中获取了C1:P1:7
    C1从队列中获取了C1:P1:4
    队列空了,生产者等待


> Queue模块说明

方法|说明
---|---
**队列类型**|---
Queue.Queue(maxsize)|先进先出队列,maxsize是队列长度,其值为非正数时是无限循环队列
Queue.LifoQueue(maxsize)|后进先出队列,也就是栈
Queue.PriorityQueue(maxsize)|优先级队列
**支持方法**|---
qsize()|返回近似队列大小,,用近似二字因为当该值大于0时不能保证并发执行的时候get(),put()方法不被阻塞
empty()|判断是否为空,空返回True否则返回False
full()|当设定了队列大小的时候,如果队列满了则返回True,否则False
put(item[,block[,timeout]])|向队列添加元素,<br>当block设置为False时队列满则抛出异常<br>当block为True,timeout为None时则会等待直到有空位<br>当block为True,timeout不为None时则根据设定的时间判断是否等待,超时了就抛出错误
put_nowait(item)|相当于put(item,False)
get([,block[,timeout])|从队列中取出元素,<br>当block设置为False时队列空则抛出异常<br>当block为True,timeout为None时则会等待直到有元素<br>当block为True,timeout不为None时则根据设定的时间判断是否等待,超时了就抛出错误
get_nowait()|等价于get(False)
task_done()|发送信号表明入列任务已经完成,常在消费者线程里使用
join()|阻塞直到队列中所有元素处理完


Queue是线程安全的,而且支持in操作,因此用它的时候不用考虑锁的问题
