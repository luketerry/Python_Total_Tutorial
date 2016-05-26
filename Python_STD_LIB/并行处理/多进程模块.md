
# 多进程模块( multiprocessing,subprocess)



## 进程(Process)

进程（Process）是计算机中的程序关于某数据集合上的一次运行活动，是系统进行资源分配和调度的基本单位，是操作系统结构的基础。在早期面向进程设计的计算机结构中，进程是程序的基本执行实体；在当代面向线程设计的计算机结构中，进程是线程的容器。程序是指令、数据及其组织形式的描述，进程是程序的实体。--by 百度百科

Unix/Linux操作系统提供了一个fork()系统调用.普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。

子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。

在"系统与环境工具"中我们介绍了`os`模块,它封装了`fork()`

*ps:这个只能unix-like系统使用*


```python
import os
```


```python
print('Process (%s) 开始...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('子进程: (%s) 它的父进程是: (%s.)' % (os.getpid(), os.getppid()))
else:
    print('父进程 (%s) 产生了子进程 (%s).' % (os.getpid(), pid))
```

    Process (13098) 开始...
    父进程 (13098) 产生了子进程 (13103).


## 多进程（multiprocessing）

进入正题了
Python是跨平台的，提供了一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。

multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：


```python
%%writefile multiproc00.py
# --*--coding:utf-8 --*--
from __future__ import print_function
from multiprocessing import Process
import os

#子进程要执行的代码
def run_proc(name):
    for i in range(3):
        print(u'子进程 %s (%s)...' % (name, os.getpid()))
    print(u'子进程结束.')
    
if __name__=='__main__':
    print(u'父进程 %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print(u'子进程要开始啦.')
    p.start()
    for i in range(3):
        print(u'父进程{pid}进行中...'.format(pid = os.getpid()))
    p.join()
    print(u"父进程结束啦")
    
```

    Overwriting multiproc00.py
    子进程: (13103) 它的父进程是: (13098.)



```python
!python multiproc00.py
```

    父进程 13105.
    子进程要开始啦.
    父进程13105进行中...
    父进程13105进行中...
    父进程13105进行中...
    子进程 test (13107)...
    子进程 test (13107)...
    子进程 test (13107)...
    子进程结束.
    父进程结束啦


创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。

join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

可以看到我们的父进程进行完了子进程才进行.其实当执行start方法的时候我们就已经把进程创建好并给他任务了.
虽然进程启动了,但我们并不能知道它啥时候运算完成.这时候用join方法来确认是否执行完了(通过阻塞主进程),也就是起个等待结果的作用.

## 进程间通信

如何让进程间通信呢,其实原理上来讲就是构造一个独立的数据结构来存放结果来参与通信

有两种方式,最常用的一种是用队列
>先进先出队列Queue


```python
%%writefile multiproc01.py
# --*--coding:utf-8 --*--
from __future__ import print_function
from multiprocessing import Process, Queue

def f(q):
    q.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())    # prints "[42, None, 'hello']"
    p.join()
```

    Overwriting multiproc01.py



```python
!python multiproc01.py
```

    [42, None, 'hello']


看一个稍微复杂一点的:


```python
%%writefile multiproc02.py
# --*--coding:utf-8 --*--
from __future__ import print_function
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())
# 读数据进程执行的代码:
def read(q):
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    while True:
        if not q.empty():
            value = q.get(True)
            print('Get %s from queue.' % value)
            time.sleep(random.random())
        else:
            q.put("Done!")
            break
if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()    
    # 等待pw结束:
    pw.join()
    # 启动子进程pr，读取:
    pr.start()
    pr.join()
    print(q.get())
    print('\n所有数据都写入并且读完')

```

    Overwriting multiproc02.py



```python
!python multiproc02.py
```

    Put A to queue...
    Put B to queue...
    Put C to queue...
    Get A from queue.
    Get B from queue.
    Get C from queue.
    Done!
    
    所有数据都写入并且读完


看到两个进程间的交互么,父进程创建一个队列给各个子进程,子进程接收父进程的队列作为参数运行.
运行过程中将结果存入队列最后运行完后将"done!"存入队列,由父进程接收.

再来是用管道

> 管道Pipes

既然是管道,那就肯定有两端,有方向,分成单向管道和双向管道了.

看一个最简单的双向管道


```python
%%writefile multiproc03.py
# --*--coding:utf-8 --*--

from multiprocessing import Process, Pipe

def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    p.join()
```

    Overwriting multiproc03.py



```python
!python multiproc03.py
```

    [42, None, 'hello']



```python
%%writefile multiproc04.py
# --*--coding:utf-8 --*--
from __future__ import print_function
from multiprocessing import Process, Pipe
import os, time, random

# 写数据进程执行的代码:
def write(conn):
    value = ["h1 reader~"]
    print('Put %s to pip...' % value)
    conn.send(value)
    time.sleep(1)
    
# 读数据进程执行的代码:
def read(conn):
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    value = conn.recv()
    print('Get %s from pip.' % value)
    conn.send("hi writer~~")
    

if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    parent_conn, child_conn = Pipe()
    pw = Process(target=write, args=(parent_conn,))#起点
    pr = Process(target=read, args=(child_conn,))#终点
    # 启动子进程pw，写入:
    pw.start()    
    # 等待pw结束:
    pw.join()
    # 启动子进程pr，读取:
    pr.start()
    pr.join()
    print(parent_conn.recv())
    print('\n所有数据都写入并且读完')


```

    Overwriting multiproc04.py



```python
!python multiproc04.py
```

    Put ['h1 reader~'] to pip...
    Get ['h1 reader~'] from pip.
    hi writer~~
    
    所有数据都写入并且读完


可以看出管道的限制相对多些,必须要建立连接才能交换数据,一出一进这样子,这也是为啥队列用的比较多.

## 静态数据共享

python里面的全局变量也只管到他自己的进程,如果要让一个静态的数据在每个子进程中都可以调用.那么需要用到模块中的几个方法:


```python
%%writefile multiproc05.py
# --*--coding:utf-8 --*--
from __future__ import print_function

from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
```

    Overwriting multiproc05.py



```python
!python multiproc05.py
```

    3.1415927
    [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]


## 高级共享multiprocessing.Manager

之前介绍了queue,pipe,array和value,这些都太具体太细节了,有没有什么方法可以简单地处理数据共享的问题呢?multiprocess提供一个manager模块.

Manager()返回的manager对象控制了一个server进程，此进程包含的python对象可以被其他的进程通过proxies来访问。从而达到多进程间数据通信且安全。

Manager支持的类型有list,dict,Namespace,Lock,RLock,Semaphore,BoundedSemaphore,Condition,Event,Queue,Value和Array。 

> 数据结构的使用:


```python
%%writefile multiproc06.py
# --*--coding:utf-8 --*--
from __future__ import print_function

import multiprocessing
import time

def worker(d, key, value):
    d[key] = value

if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    d = mgr.dict()
    jobs = [ multiprocessing.Process(target=worker, args=(d, i, i*2))
             for i in range(10) 
             ]
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print ('Results:' )
    for key, value in enumerate(dict(d)):
        print("%s=%s" % (key, value))
```

    Overwriting multiproc06.py



```python
!python multiproc06.py
```

    Results:
    0=0
    1=1
    2=2
    3=3
    4=4
    5=5
    6=6
    7=7
    8=8
    9=9


> namespace对象没有公共的方法，但是有可写的属性


```python
import multiprocessing
```


```python
manager = multiprocessing.Manager()
```


```python
Global = manager.Namespace()
```


```python
Global.x = 10
```


```python
Global.y = 'hello'
```


```python
print(Global)
```

    Namespace(x=10, y='hello')


## 进程池(pool)

如果要启动大量的子进程，可以用进程池的方式批量创建子进程：


```python
%%writefile multiprocpool00.py
# --*--coding:utf-8 --*--
from __future__ import print_function
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('运行任务 %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('任务 %s 执行了 %0.2f 秒.' % (name, (end - start)))

if __name__=='__main__':
    print('父进程 %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))#创建非阻塞子进程用这个
    print('等待所有子进程完成...')
    p.close()
    p.join()
    print('所有子进程完成了.')
```

    Overwriting multiprocpool00.py



```python
!python multiprocpool00.py
```

    父进程 13135.
    等待所有子进程完成...
    运行任务 0 (13136)...
    运行任务 1 (13137)...
    运行任务 2 (13138)...
    运行任务 3 (13139)...
    任务 1 执行了 0.36 秒.
    运行任务 4 (13137)...
    任务 3 执行了 0.45 秒.
    任务 0 执行了 1.36 秒.
    任务 2 执行了 1.55 秒.
    任务 4 执行了 2.61 秒.
    所有子进程完成了.


对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。

请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。如果改成：

    p = Pool(5)

就可以同时跑5个进程。

由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。

除了使用`apply_async`方法外,还有apply，map和map_async可以用于线程池的计算

命令|说明
---|---
apply|单一任务布置
apply_async|非阻塞单一任务布置
map()|同系统的map方法
map_async|非阻塞的map




```python
%%writefile multiprocpool01.py
# --*--coding:utf-8 --*--
from __future__ import print_function
from multiprocessing import Pool
from time import sleep

def f(x):
    return x*x

if __name__ == '__main__':
    # start 4 worker processes
    pool = Pool(processes=4)
    print("map: ",pool.map(f, range(10)))
    print("imap:")
    for i in pool.imap_unordered(f, range(10)):
        print(i)

    # evaluate "f(10)" asynchronously
    res = pool.apply_async(f, [10])
    print("apply:",res.get(timeout=1))             # prints "100"

    # make worker sleep for 10 secs
    res = pool.apply_async(sleep, [10])
    print(res.get(timeout=1))             # raises multiprocessing.TimeoutError

```

    Overwriting multiprocpool01.py



```python
!python multiprocpool01.py
```

    map:  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    imap:
    0
    1
    4
    9
    16
    25
    36
    49
    64
    81
    apply: 100
    Traceback (most recent call last):
      File "multiprocpool01.py", line 23, in <module>
        print(res.get(timeout=1))             # raises multiprocessing.TimeoutError
      File "/Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/multiprocessing/pool.py", line 563, in get
        raise TimeoutError
    multiprocessing.TimeoutError


> 获取进程池中的运算结果


```python
%%writefile multiprocpool02.py
# --*--coding:utf-8 --*--
from __future__ import print_function
import multiprocessing
import time

def func(msg):
    print("msg:", msg)
    time.sleep(1)
    print("end")
    return "done " + msg

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=4)
    result = []
    for i in xrange(3):
        msg = "hello %d" %(i)
        result.append(pool.apply_async(func, (msg, )))
    pool.close()
    pool.join()
    for res in result:
        print(":::", res.get())
    print("Sub-process(es) done.")
```

    Writing multiprocpool02.py



```python
!python multiprocpool02.py
```

    msg: hello 0
    msg: hello 1
    msg: hello 2
    end
    end
    end
    ::: done hello 0
    ::: done hello 1
    ::: done hello 2
    Sub-process(es) done.


## 子进程(subprocess)

很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。

subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。

下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的：


```python
import subprocess
r = subprocess.Popen('nslookup www.python.org', shell=True,stdout=subprocess.PIPE)
print(r.communicate()[0].decode("utf-8"))
print('Exit code:', r.returncode)
```

    Server:		192.168.2.1
    Address:	192.168.2.1#53
    
    Non-authoritative answer:
    www.python.org	canonical name = python.map.fastly.net.
    Name:	python.map.fastly.net
    Address: 103.245.222.223
    
    
    Exit code: 0


> # 并行性能测试

我们来比较下一个性能吧~来求1到1000万的平方和吧

**首先是原装的cpython**


```python
%%writefile multiprocTest.py
# --*--coding:utf-8 --*--
from __future__ import print_function

if __name__=="__main__":
    print(sum(map(lambda x: x**2,xrange(1,10000001))))
```

    Overwriting multiprocTest.py



```python
%timeit !python multiprocTest.py
```

    333333383333335000000
    333333383333335000000
    333333383333335000000
    333333383333335000000
    1 loops, best of 3: 4.34 s per loop


**接着是pypy以性能著称的pypy**


```python
%timeit !pypy multiprocTest.py
```

    333333383333335000000
    333333383333335000000
    333333383333335000000
    333333383333335000000
    1 loops, best of 3: 589 ms per loop


**然后是多进程并行**


```python
%%writefile multiTest.py
# --*--coding:utf-8 --*--
from __future__ import print_function
from multiprocessing import Pool
import time
def f(x):
    return x**2

if __name__=="__main__":
    pool = Pool(processes=4)
    result = pool.map_async(f,xrange(1,10000001), )
    pool.close()
    pool.join()
    print(sum(result.get()))
```

    Overwriting multiTest.py



```python
%timeit !python multiTest.py
```

    333333383333335000000
    333333383333335000000
    333333383333335000000
    333333383333335000000
    1 loops, best of 3: 9 s per loop



```python
%timeit !pypy multiTest.py
```

    333333383333335000000
    333333383333335000000
    333333383333335000000
    333333383333335000000
    1 loops, best of 3: 19.1 s per loop


由此可见还是pypy靠谱
