
# 迭代工具模块(itertools)

Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。

## “无限”迭代器：***注意千万别对它们用for循环***


```python
from __future__ import print_function
from itertools import count,cycle,repeat
```

### `count(start, [step])`累加器

`count()`会创建一个无限的迭代器，从初始值开始每次按`步长*调用次数累加`，根本停不下来，只能按Ctrl+C退出


```python
step_2=count(0,2)
```


```python
for i in range(10):
    print(next(step_2))
```

    0
    2
    4
    6
    8
    10
    12
    14
    16
    18


### `cycle(p)`循环器

 `cycle()`会把传入的序列无限的循环下去


```python
cyc = cycle("asdfg")
```


```python
for i in range(10):
    print(next(cyc))
```

    a
    s
    d
    f
    g
    a
    s
    d
    f
    g


### repeat(elem [,n])重复输出器

可以无限的重复元素,或者重复n次


```python
rep5 = repeat([1,2,3],5)
```


```python
try:
    for i in range(10):
        print(next(rep5))
except StopIteration:
    print("end")
```

    [1, 2, 3]
    [1, 2, 3]
    [1, 2, 3]
    [1, 2, 3]
    [1, 2, 3]
    end


## 迭代对象操作工具


```python
from itertools import chain,compress,groupby,dropwhile,takewhile,islice,tee
```

> `chain()`连接两个序列生成一个生成器 


```python
list(chain([1,2,3],[4,5,6]))
```




    [1, 2, 3, 4, 5, 6]



> `compress()`筛选序列


```python
list(compress([1,3,5,7,9],[0,0,1,0,0]))
```




    [5]



> groupby()聚合


```python
[k for k, g in groupby('AAAABBBCCDAABBB')]
```




    ['A', 'B', 'C', 'D', 'A', 'B']




```python
list(groupby("12321314",key = lambda x:int(x)))
```




    [(1, <itertools._grouper at 0x10bd17c18>),
     (2, <itertools._grouper at 0x10bd17f60>),
     (3, <itertools._grouper at 0x10bd17be0>),
     (2, <itertools._grouper at 0x10bd17940>),
     (1, <itertools._grouper at 0x10bd172b0>),
     (3, <itertools._grouper at 0x10bd17ba8>),
     (1, <itertools._grouper at 0x10bd17630>),
     (4, <itertools._grouper at 0x10bd17668>)]



> `dropwhile()`当有一个元素判断为假时开始执行,返回后面的元素


```python
list(dropwhile(lambda x: x<5, [1,4,6,4,1]))
```




    [6, 4, 1]



> takewhile()从开头开始输出,但判断结果为假时结束


```python
list(takewhile(lambda x: x<5, [1,4,6,4,1]))
```




    [1, 4]



> islice(seq, [start,] stop [, step])切片操作


```python
list(islice('ABCDEFG', 2, None))
```




    ['C', 'D', 'E', 'F', 'G']



> tee()复制序列 


```python
 for i in tee("asdsfqwer",3):
        print(list(i))
```

    ['a', 's', 'd', 's', 'f', 'q', 'w', 'e', 'r']
    ['a', 's', 'd', 's', 'f', 'q', 'w', 'e', 'r']
    ['a', 's', 'd', 's', 'f', 'q', 'w', 'e', 'r']


## 高阶函数补充

这部分是3以上的,2.7所用的方法不同,目的也不同


```python
from itertools import filterfalse,zip_longest,accumulate,starmap
```

> `filterfalse(func,seq)`当判断函数为`False`时则放入生成器


```python
list(filterfalse(lambda x: x%2, range(10)))
```




    [0, 2, 4, 6, 8]



>`zip_longest(p, q, ...)`与zip类似


```python
list(zip_longest('ABCD', 'xy', fillvalue='-'))
```




    [('A', 'x'), ('B', 'y'), ('C', '-'), ('D', '-')]



> `accumulate(p[,func])`堆积函数

与它相似的是`reduce`,只是它把过程中的中间值也存入了结果


```python
list(accumulate([3, 4, 6, 2, 1, 9, 0, 7, 5, 8], max))
```




    [3, 4, 6, 6, 6, 9, 9, 9, 9, 9]



> `starmap(func,seq)`类似map,但是输入的是一对一对的数据


```python
list(starmap(pow, [(2,5), (3,2), (10,3)]))
```




    [32, 9, 1000]



### 2.7中的高阶函数补充

在2.7中,各个高阶函数返回的是list,所以对应返回生成器的版本在该模块下,有:

+ `ifilter()`-->`filter()`
+ `ifilterfalse()`-->`filterfalse()`
+ `imap()`-->`map()`
+ `izip()`--`zip()`	
+ `izip_longest()`-->`zip_longest()`

另外2.7中`accumulate(p[,func])`堆积函数是没有的

## 生成器操作工具


```python
from itertools import product,permutations,combinations,combinations_with_replacement
```

> `product((iter1, iter2, ... iterN, [repeat=1])`

创建一个迭代器，生成表示item1，item2等中的项目的笛卡尔积的元组，repeat是一个关键字参数，指定重复生成序列的次数。


```python
list(product('ABCD','EFGH', repeat=1))
```




    [('A', 'E'),
     ('A', 'F'),
     ('A', 'G'),
     ('A', 'H'),
     ('B', 'E'),
     ('B', 'F'),
     ('B', 'G'),
     ('B', 'H'),
     ('C', 'E'),
     ('C', 'F'),
     ('C', 'G'),
     ('C', 'H'),
     ('D', 'E'),
     ('D', 'F'),
     ('D', 'G'),
     ('D', 'H')]



> `permutations(seq,r)`

创建一个迭代器，返回iterable中所有长度为r的项目序列，如果省略了r，那么序列的长度与iterable中的项目数量相同：(有顺序)


```python
list(permutations('ABCD',2))
```




    [('A', 'B'),
     ('A', 'C'),
     ('A', 'D'),
     ('B', 'A'),
     ('B', 'C'),
     ('B', 'D'),
     ('C', 'A'),
     ('C', 'B'),
     ('C', 'D'),
     ('D', 'A'),
     ('D', 'B'),
     ('D', 'C')]



> `combinations(iterable, r)`

创建一个迭代器，返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序无重复元素地排序:(无顺序)


```python
list(combinations('ABCD',2))
```




    [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]



> `combinations_with_replacement(seq,r)`

创建一个迭代器，返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序有重复元素地排序:(无顺序)


```python
list(combinations_with_replacement('ABCD', 2))
```




    [('A', 'A'),
     ('A', 'B'),
     ('A', 'C'),
     ('A', 'D'),
     ('B', 'B'),
     ('B', 'C'),
     ('B', 'D'),
     ('C', 'C'),
     ('C', 'D'),
     ('D', 'D')]


