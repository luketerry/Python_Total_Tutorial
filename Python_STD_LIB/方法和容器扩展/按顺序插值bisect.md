
# 按顺序插值(bisect)

这个模块很有意思,它的功能是将一个元素找到合适的位置后插入一个序列,但它既可以找位置,也可以插入


```python
from bisect import bisect,bisect_left,bisect_right,insort,insort_left,insort_right
```


```python
l=[2,5,5,7,10]
```

> bisect,bisect_left,bisect_right

查看插入位置,bisect和bisect_left相似,而bisect_right是当有和元素重复的元素时放在右边


```python
bisect(l,3)
```




    1




```python
bisect_left(l,5)
```




    1




```python
bisect_right(l,5)
```




    3



> insort,insort_left,insort_right

插入元素,insort和insort_left相似,而insort_right是当有和元素重复的元素时放在右边


```python
l1=[2,5,5,7,10]
l2=[2,5,5,7,10]
l3=[2,5,5,7,10]
```


```python
insort(l1,3)
l1
```




    [2, 3, 5, 5, 7, 10]




```python
insort_left(l2,5)
l2
```




    [2, 5, 5, 5, 7, 10]




```python
insort_right(l3,5)
l3
```




    [2, 5, 5, 5, 7, 10]


