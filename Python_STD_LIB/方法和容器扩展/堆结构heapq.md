
# 堆结构(heapq)

heapq模块使用一个用堆实现的优先级队列。堆是一种简单的有序列表，并且置入了堆的相关规则。

堆是一种树形的数据结构，树上的子节点与父节点之间存在顺序关系。二叉堆(binary heap)能够用一个经过组织的列表或数组结构来标识，在这种结构中，元素N的子节点的序号为2*N+1和2*N+2(下标始于0)。简单来说，这个模块中的所有函数都假设序列是有序的，所以序列中的第一个元素(seq[0])是最小的，序列的其他部分构成一个二叉树，并且seq[i]节点的子节点分别为seq[2*i+1]以及seq[2*i+2]。当对序列进行修改时，相关函数总是确保子节点大于等于父节点。

因此把数据放入堆就等于排序了



```python
import heapq
```


```python
heap = [] 
for value in [20, 10, 30, 50, 40]:
    heapq.heappush(heap, value)
while heap:
    print(heapq.heappop(heap))
```

    10
    20
    30
    40
    50


## 相关操作

操作|说明
---|---
heappush(heap,x)        |将x入堆
heappop(heap)           |将堆中最小的元素弹出
heapify(heap)           |将heap属性强制应用到任意一个列表
heapreplace(heap,x)     |将堆中最小的元素弹出，同时将x入堆
nlargest(n,iter)        |返回iter中第n大的元素
nsmallest(n,iter)      | 返回iter中第n小的元素
merge(\*iterables, key=None, reverse=False)|合并可迭代对象并入堆
