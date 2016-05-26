
# 容器类模块(collections)

这个模块是python中容器的官方扩展

容器名|说明
---|---
namedtuple|带名元祖
deque|高效实现插入和删除操作的双向列表,适合用来做队列和栈
ChainMap|(3.3后独有)链图
Counter	|计数器,返回一个各元素为key,出现次数为value的字典
OrderedDict	|有序字典
defaultdict|key不存在时，返回一个默认值的字典


```python
from collections import *
```

## namedtuple
如果用元组我们可以很容易的描述坐标,向量等有序不变序列,但我们并不知道他们具体是啥,
这样我们只能做标注或者命名变量的时候用额定格式的变量名,这样都显得不直观.比较好的解决方案就是用这个带名元组.

我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。

*定义坐标:*


```python
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)
```

    1
    2


## deque

deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈


```python
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

```

    deque(['y', 'a', 'b', 'c', 'x'])


deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。

## ChainMap(3.3新增)

这个容器是字典的扩展,主要解决的是查看字典更新前状态的问题.


```python
s=ChainMap({1:10},{2:22})#定义一个默认的ChainMap容器
ss=s.new_child({1:5})#定义一个s的子容器,
print(ss.maps)#查看ss的映射关系
print(ss.parents)#返回ss的父ChainMap实例
```

    [{1: 5}, {1: 10}, {2: 22}]
    ChainMap({1: 10}, {2: 22})


可以自己试试,我们可以发现如果子容器有和父容器相同的键值,那使用的时候是用的子容器的value,
但父容器的也被保留了下来,有点类似单继承的类

## Counter

Counter是一个简单的计数器，例如，统计字符出现的个数:

    




```python
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
```

    Counter({'g': 2, 'r': 2, 'm': 2, 'i': 1, 'p': 1, 'o': 1, 'n': 1, 'a': 1})


用这个实现wordcount就太方便了


```python
with open("source/readme.md") as f:
    file=f.read()
#print(file)
import re
l = re.split("[ #\n\]\[`/.:<>(){}]",file)
d = Counter()
for ch in l:
    d[ch] = d[ch] + 1
print(d)
```

    Counter({'': 226, 'the': 21, 'Spark': 16, 'to': 14, 'for': 11, 'and': 10, 'apache': 9, 'a': 9, 'org': 9, 'run': 9, 'http': 7, 'spark': 7, 'can': 6, 'on': 6, 'is': 6, 'latest': 5, 'also': 5, 'bin': 5, 'html': 5, 'of': 5, 'in': 5, 'you': 4, 'building': 4, 'Hadoop': 4, 'if': 4, 'with': 4, 'docs': 4, 'documentation': 4, 'example': 4, 'You': 4, 'examples': 4, '1000': 4, 'that': 3, 'locally': 3, 'class': 3, 'including': 3, 'run-example': 3, 'Please': 3, 'building-spark': 3, 'cluster': 3, 'using': 3, 'build': 3, 'package': 3, 'particular': 3, 'or': 3, 'guidance': 3, 'an': 3, 'use': 3, 'project': 3, 'do': 2, 'data': 2, 'one': 2, 'Hive': 2, 'should': 2, 'For': 2, 'be': 2, 'This': 2, 'It': 2, 'count': 2, 'following': 2, 'Hadoop,': 2, 'return': 2, 'at': 2, 'tests': 2, 'shell': 2, 'Apache': 2, 'Python': 2, 'supports': 2, 'https': 2, 'detailed': 2, 'refer': 2, 'Interactive': 2, 'command,': 2, 'Configuration': 2, 'cwiki': 2, 'set': 2, 'To': 2, 'how': 2, 'programs': 2, 'Scala': 2, 'N': 2, 'Python,': 2, 'SPARK': 2, 'display': 2, 'SparkPi': 2, 'general': 2, 'Shell': 2, 'sc': 2, 'processing,': 2, 'SQL': 2, 'distribution': 2, 'which': 2, 'confluence': 2, 'params': 2, 'parallelize': 2, 'distributions': 1, 'Tests': 1, 'mesos': 1, 'run-tests': 1, 'About': 1, 'available': 1, 'Documentation': 1, 'see': 1, 'Java,': 1, 'YARN,': 1, 'Try': 1, 'prefer': 1, 'contains': 1, 'README': 1, 'systems': 1, '"local': 1, 'fast': 1, 'Contributing+to+Spark': 1, 'Testing': 1, 'file': 1, 'when': 1, 'thread,': 1, 'And': 1, 'processing': 1, '"Building': 1, 'machine': 1, 'different': 1, 'all': 1, 'easiest': 1, 'automated': 1, 'need': 1, '"': 1, 'Building': 1, 'dev': 1, 'scala': 1, '-DskipTests': 1, 'Versions': 1, 'changed': 1, 'See': 1, 'Version"': 1, '"Third': 1, 'learning,': 1, '"Specifying': 1, 'other': 1, 'application': 1, 'A': 1, 'comes': 1, 'core': 1, '7077': 1, 'not': 1, 'storage': 1, 'requires': 1, 'rich': 1, 'site,': 1, 'ContributingtoSpark-AutomatedTesting': 1, 'downloaded': 1, 'Streaming': 1, 'abbreviated': 1, 'usage': 1, 'from': 1, 'MASTER=spark': 1, 'overview': 1, 'higher-level': 1, 'Party': 1, 'no': 1, 'Scala,': 1, 'this': 1, 'several': 1, 'Alternatively,': 1, 'will': 1, 'programming': 1, 'Programs': 1, 'programs,': 1, 'computation': 1, 'Pi': 1, 'them,': 1, 'Spark"': 1, 'pre-built': 1, 'version': 1, 'talk': 1, 'structured': 1, 'name': 1, 'environment': 1, 'works': 1, 'provides': 1, '1': 1, 'high-level': 1, 'web': 1, 'engine': 1, 'built': 1, 'MLlib': 1, 'mvn': 1, 'must': 1, 'setup': 1, 'configure': 1, 'Online': 1, 'range': 1, 'More': 1, 'your': 1, 'page': 1, 'computing': 1, 'specifying-the-hadoop-version': 1, 'threads': 1, 'instance': 1, 'maven': 1, 'Note': 1, 'have': 1, 'host': 1, 'graph': 1, 'are': 1, 'basic': 1, 'first': 1, 'variable': 1, 'Data': 1, 'directory': 1, 'GraphX': 1, 'submit': 1, 'start': 1, 'Many': 1, '"yarn-client"': 1, 'The': 1, 'guide,': 1, 'runs': 1, 'Maven': 1, 'optimized': 1, 'guide': 1, 'Running': 1, 'spark-shell': 1, 'print': 1, 'instructions': 1, '"yarn-cluster"': 1, 'sample': 1, 'hadoop-third-party-distributions': 1, 'find': 1, 'Once': 1, 'tools': 1, 'Distributions"': 1, 'pyspark': 1, 'Thriftserver': 1, 'same': 1, 'documentation,': 1, 'its': 1, 'Because': 1, 'analysis': 1, 'against': 1, 'stream': 1, 'configuration': 1, 'built,': 1, 'graphs': 1, 'help': 1, 'system': 1, 'library': 1, '"local"': 1, 'HDFS': 1, 'Big': 1, 'URL,': 1, 'protocols': 1, 'through': 1, 'wiki': 1, 'Example': 1, 'uses': 1, 'way': 1, 'clean': 1, 'online': 1, 'APIs': 1, 'versions': 1, 'running': 1, 'MASTER': 1, 'only': 1, 'given': 1, 'Hadoop-supported': 1})


## OrderedDict

使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
如果要保持Key的顺序，可以用OrderedDict：


```python
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d) # dict的Key是无序的
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od) # OrderedDict的Key是有序的
```

    {'c': 3, 'b': 2, 'a': 1}
    OrderedDict([('a', 1), ('b', 2), ('c', 3)])


注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序


```python
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
list(od.keys()) # 按照插入的Key的顺序返回
```




    ['z', 'y', 'x']



*实现一个FIFO的dict:*


```python
class FIFOOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(FIFOOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

fifo=FIFOOrderedDict(3)
fifo[1]="a"
fifo[2]="b"
fifo[3]="c"
print(fifo)
fifo[4]="d"
print(fifo)
```

    add: (1, 'a')
    add: (2, 'b')
    add: (3, 'c')
    FIFOOrderedDict([(1, 'a'), (2, 'b'), (3, 'c')])
    remove: (1, 'a')
    add: (4, 'd')
    FIFOOrderedDict([(2, 'b'), (3, 'c'), (4, 'd')])



## defaultdict

使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：

    dd = defaultdict(lambda: 'N/A')
    dd['key1'] = 'abc'
    print(dd['key1']) # key1存在
    print(dd['key2']) # key2不存在，返回默认值





```python
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1']) # key1存在
print(dd['key2']) # key2不存在，返回默认值

```

    abc
    N/A


注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
