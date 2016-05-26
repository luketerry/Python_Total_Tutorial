
作为一门脚本语言,将字符串最为代码运行可以大大的提高灵活度,`eval()`就是这样一种内置方法

它的接口是这样的:

    eval(exp[, globals[, locals]])
    
+ globals是字典形式,表示全局命名空间,如果传入globals的字典中缺少`__builtins__`的时候,当前的全局命名空间将作为globals参数输入并在表达式计算之前被解析.

+ locals则为任何映射对象,表示局部命名空间,与globals两者默认相同.

如果两者都省略则表示在eval的调用环境中执行

看个例子:


```python
a = eval("lambda *x: sum(x)")
```


```python
a
```




    <function __main__.<lambda>>




```python
a(1,2,3,4,5)
```




    15




```python
b = lambda x : eval("1 if x >0 else -1")
```


```python
b(10)
```




    1




```python
%timeit a(1,2,3,4,5,6,7,8,9)
```

    The slowest run took 5.78 times longer than the fastest. This could mean that an intermediate result is being cached 
    1000000 loops, best of 3: 610 ns per loop



```python
%timeit lambda *x:sum(x)(1,2,3,4,5,6,7,8,9)
```

    The slowest run took 11.07 times longer than the fastest. This could mean that an intermediate result is being cached 
    10000000 loops, best of 3: 111 ns per loop


与它类似的是exec()方法,但exec是翻译并执行,因此我们上面的例子得写成


```python
exec("aa = lambda x: x")
```


```python
aa
```




    <function __main__.<lambda>>




```python
aa(10)
```




    10



eval有两个弊端:

+ 降低运算效率

    如上面看到的,运行时间上差距不小

+ 安全性

    这主要是因为可以调用一些危险的方法二没有设限,比如:


```python
eval("__import__('sh').ls()")
```




    [1m[36m__pycache__[m[m                     装饰器(decorator).ipynb         字符串变代码!(eval).ipynb
    元类(metaclass).ipynb           动态补丁(monkey-path).ipynb     基本类型扩展.ipynb



于是你的系统底裤都被别人看光啦


```python
%%writefile eval_test.py
import sys

print eval(sys.argv[1])

```

    Overwriting eval_test.py



```python
!python eval_test.py "__import__('sh').ls()"
```

    [1m[36m__pycache__[m[m                     装饰器(decorator).ipynb         基本类型扩展.ipynb
    eval_test.py                    动态补丁(monkey-path).ipynb
    元类(metaclass).ipynb           字符串变代码!(eval).ipynb
    


当然了,我们也可以通过限制globals和locals来实现对可用项的限制,但你懂得...总有让你吃瘪的库和方法的.所以没事别用,尤其不要用在webapp上.

如果只是为了传入参数,那么可以使用ast库的literal_eval函数,它是安全的


```python
import ast
```


```python
ast.literal_eval("[1,2,3]")
```




    [1, 2, 3]


