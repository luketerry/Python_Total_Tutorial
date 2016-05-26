
池模式多用于并发,它把一系列对象看做是一个个元素放在一个池子里统一管理,并利用上下文处理元素获取和放入的操作.

当调用对象时，不使用常规的构造方式，而是通过一个对象池操作。即如果池中存在该对象，则取出；如果不存在，则新建一个对象并存储在池中。当使用完该对象后，则将该对象的归还给对象池

恰当地使用对象池化技术，可以有效地减少对象生成和初始化时的消耗，提高系统的运行效率.也让代码更加直观


```python
class QueueObject():

    def __init__(self, queue, auto_get=False):
        self._queue = queue
        self.object = self._queue.get() if auto_get else None

    def __enter__(self):
        if self.object is None:
            self.object = self._queue.get()
        return self.object

    def __exit__(self, Type, value, traceback):
        if self.object is not None:
            self._queue.put(self.object)
            self.object = None

    def __del__(self):
        if self.object is not None:
            self._queue.put(self.object)
            self.object = None


def main():
    try:
        import queue
    except ImportError:  # python 2.x compatibility
        import Queue as queue

    def test_object(queue):
        queue_object = QueueObject(queue, True)
        print('Inside func: {}'.format(queue_object.object))

    sample_queue = queue.Queue()

    sample_queue.put('yam')
    with QueueObject(sample_queue) as obj:
        print('Inside with: {}'.format(obj))
    print('Outside with: {}'.format(sample_queue.get()))

    sample_queue.put('sam')
    test_object(sample_queue)
    print('Outside func: {}'.format(sample_queue.get()))

    if not sample_queue.empty():
        print(sample_queue.get())

main()
```

    Inside with: yam
    Outside with: yam
    Inside func: sam
    Outside func: sam

