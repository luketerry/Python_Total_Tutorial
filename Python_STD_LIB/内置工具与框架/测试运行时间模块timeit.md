
# 测试运行时间模块(timeit)

Python中的timeit是测试代码执行效率的工具.可以用命令行直接测试脚本,也可以测试代码字符串的效率,当然最简单的还是直接用ipython的内置timeit魔法命令测某段代码的效率


```python
import timeit
t = timeit.Timer('map(lambda x: x**2,range(1000))')
t.timeit()
```




    0.8761048480009777




```python
!python -m timeit -s "map(lambda x: x**2,range(1000))"
```

    100000000 loops, best of 3: 0.018 usec per loop

