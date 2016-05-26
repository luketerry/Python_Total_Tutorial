
# 多线程模块(threading)

threading提供了一个高层的API来提供线程的并发性。这些线程并发运行并共享内存。 多线程看着多么美好的,但因为数据安全的问题被加了锁..所以永远是单核运行....不细说了看个简单的用法吧
        
下面来看threading模块的具体用法： 



```python
%%writefile threading00.py
# --*--coding:utf-8 --*--
from __future__ import print_function

import threading
import time
 
def worker(i):
    print(i)
    time.sleep(1)
    print("AWAKE")
    
for i in xrange(5):
    t = threading.Thread(target=worker,args=(i,))
    t.start()
print("closed")
```

    Overwriting threading00.py



```python
!python threading00.py
```

    01
    
    2
    3
    4
    closed
    AWAKE
    AWAKE
    AWAKEAWAKE
    
    AWAKE


对比下不用多线程:


```python
def worker(i):
    print(i)
    import time
    time.sleep(1)
    print("AWAKE")
    
for i in xrange(5):
    worker(i)
```

    0
    AWAKE
    1
    AWAKE
    2
    AWAKE
    3
    AWAKE
    4
    AWAKE


> 几个方法:

setDaemon() 设为True时说明是守护进程

join() 表示阻塞等待


```python
import threading
import time
import Queue
q = Queue.Queue()
def worker(i):
    print(i)
    time.sleep(1)
    print("AWAKE")
    q.put("r")
for i in xrange(5):
    t = threading.Thread(target=worker,args=(i,))
    t.start()
    print(t.isAlive())
print("closed")
```

    0
    True
    1
    True
    2
    True
    3 True
    
    4
    True
    closed



```python
t.isAlive()
```

    AWAKE
    AWAKE
    AWAKE
    AWAKE
    AWAKE





    False




```python
t.join()
```


```python
t
```




    <Thread(Thread-37, stopped 123145338101760)>




```python
from datetime import datetime
```


```python
a = datetime.utcnow()
```


```python
b = datetime.utcnow()
```


```python
type((b-a).seconds)
```




    int




```python
from random import randint,random
from time import sleep
from datetime import datetime
class Worker(threading.Thread):
    def run (self):
        self.state = 0
        times = randint(5,30)
        self.ifdo = True
        for i in range(times):
            if random() < 0.2:
                self._state = "error"
                break
            if self.ifdo == False:
                self._state = "stoped"
                break

            print 'I am running...'
            time.sleep(2)
            self.state = int(100*(float(i)/times))
        else:
            self._state = "success"
            
        if self._state == "stoped":
            self.state = 'REVOKED'

        if self._state == "error":
            self.state = 'FAILURE'

        if self._state == "success":
            self.state = 'SUCCESS'
        self.end_time = datetime.utcnow()


    def stop (self):
        print 'I am stopping it...'
        self.ifdo = False;

    def getstate(self):
        return self.state
    def getend_time(self):
        if self.isAlive() == True:
            return False
        else:
            return self.end_time

```


```python
worker = Worker()
worker.setDaemon(True)
```


```python
worker.start()
```


```python
worker.getstate()
```




    'FAILURE'




```python
worker.stop()
worker.join()
```

    I am stopping it...



```python
worker.getstate()
```




    'FAILURE'




```python
type(worker.end_time)
```




    datetime.datetime




```python
worker.isAlive()
```




    False




```python
import requests
```


```python
import json
```


```python
task_no = randint(1000,10000)
input_fpath = "~/input"
output_fpath = "~/output"
time_limit = randint(600,6000)
```


```python
requests.post("http://192.168.10.136:5000/API/tasks",data=json.dumps({
                'task_no': task_no,
                'args':{
                    'input_fpath': input_fpath,
                    'output_fpath': output_fpath,
                    'time_limit': time_limit,
                    'clear_nodes': True
                }
            })).json()
```




    {u'message': u'',
     u'result': {u'message': u'task is running',
      u'start_time': u'2016-04-20 08:08:19.566249',
      u'task_no': 9326},
     u'state': u'success'}




```python

```
