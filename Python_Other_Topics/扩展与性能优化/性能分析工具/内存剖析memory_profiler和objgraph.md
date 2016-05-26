
## 内存分析

[memory_profiler](https://pypi.python.org/pypi/memory_profiler/)是用来分析内存使用情况和追踪内存泄露的工具.它需要pip安装


它的使用及其简单:


```python
%%writefile memory_test.py
from memory_profiler import profile
@profile
def foo():
    sum = 0
    for i in range(10000):
        sum += i
    return sum
if __name__=="__main__":
    try :
        import profile as cProfile
    except:
        import cProfile 
        
    cProfile.run("foo()","foo.txt")
    import pstats
    p = pstats.Stats("foo.txt")
    p.sort_stats("time").print_stats()
```

    Overwriting memory_test.py



```python
!python memory_test.py
```

    Filename: memory_test.py
    
    Line #    Mem usage    Increment   Line Contents
    ================================================
         2     21.1 MiB      0.0 MiB   @profile
         3                             def foo():
         4     21.1 MiB      0.0 MiB       sum = 0
         5     21.3 MiB      0.2 MiB       for i in range(10000):
         6     21.3 MiB      0.0 MiB           sum += i
         7     21.3 MiB      0.0 MiB       return sum
    
    
    Sun Feb 28 15:43:39 2016    foo.txt
    
             45866 function calls (45816 primitive calls) in 0.701 seconds
    
       Ordered by: internal time
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.444    0.444    0.445    0.445 memory_test.py:2(foo)
          308    0.028    0.000    0.136    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/posixpath.py:380(_joinrealpath)
          617    0.028    0.000    0.051    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/posixpath.py:329(normpath)
         2984    0.023    0.000    0.037    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/posixpath.py:61(join)
         2982    0.021    0.000    0.061    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/posixpath.py:132(islink)
         2982    0.021    0.000    0.021    0.000 :0(lstat)
         6139    0.015    0.000    0.015    0.000 :0(append)
         2953    0.013    0.000    0.019    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/stat.py:55(S_ISLNK)
         5144    0.013    0.000    0.013    0.000 :0(startswith)
          309    0.009    0.000    0.032    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/inspect.py:440(getsourcefile)
         2982    0.008    0.000    0.008    0.000 :0(partition)
         2986    0.007    0.000    0.007    0.000 :0(endswith)
         2953    0.006    0.000    0.006    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/stat.py:24(S_IFMT)
          9/1    0.006    0.001    0.248    0.248 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/inspect.py:472(getmodule)
          274    0.006    0.000    0.006    0.000 :0(stat)
          617    0.005    0.000    0.061    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/posixpath.py:358(abspath)
         1162    0.005    0.000    0.007    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/string.py:222(lower)
         1686    0.005    0.000    0.005    0.000 :0(isinstance)
          983    0.004    0.000    0.006    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/inspect.py:51(ismodule)
          925    0.004    0.000    0.006    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/posixpath.py:52(isabs)
          309    0.003    0.000    0.067    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/inspect.py:460(getabsfile)
          308    0.003    0.000    0.169    0.001 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/posixpath.py:372(realpath)
         1162    0.003    0.000    0.003    0.000 :0(lower)
    1024/1018    0.002    0.000    0.002    0.000 :0(len)
          347    0.002    0.000    0.005    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/inspect.py:398(getfile)
          617    0.002    0.000    0.002    0.000 :0(split)
          683    0.002    0.000    0.002    0.000 :0(hasattr)
          617    0.002    0.000    0.002    0.000 :0(join)
          273    0.002    0.000    0.007    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/genericpath.py:23(exists)
          309    0.001    0.000    0.001    0.000 :0(get_suffixes)
          322    0.001    0.000    0.001    0.000 :0(get)
         14/1    0.001    0.000    0.002    0.002 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/sre_compile.py:64(_compile)
          309    0.001    0.000    0.001    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/posixpath.py:44(normcase)
          9/3    0.000    0.000    0.002    0.001 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/sre_parse.py:395(_parse)
           34    0.000    0.000    0.001    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/tokenize.py:287(generate_tokens)
            2    0.000    0.000    0.000    0.000 :0(range)
           60    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/sre_parse.py:141(__getitem__)
           41    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/sre_parse.py:193(__next)
         17/5    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/sre_parse.py:151(getwidth)
            1    0.000    0.000    0.001    0.001 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/tokenize.py:175(tokenize_loop)
          6/1    0.000    0.000    0.002    0.002 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/sre_parse.py:317(_parse_sub)
           30    0.000    0.000    0.000    0.000 :0(match)
            2    0.000    0.000    0.000    0.000 :0(items)
            5    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/sre_compile.py:256(_optimize_charset)
            1    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/memory_profiler.py:594(show_results)
           31    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/sre_parse.py:212(get)
            1    0.000    0.000    0.000    0.000 :0(setprofile)
           33    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/inspect.py:641(tokeneater)
           33    0.000    0.000    0.000    0.000 :0(min)
           29    0.000    0.000    0.000    0.000 :0(span)
           10    0.000    0.000    0.000    0.000 :0(write)
           26    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/sre_parse.py:149(append)
            2    0.000    0.000    0.000    0.000 :0(getcwd)
            1    0.000    0.000    0.701    0.701 profile:0(foo())
            5    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/sre_compile.py:228(_compile_charset)
           18    0.000    0.000    0.000    0.000 :0(format)
           30    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/sre_parse.py:206(match)
           20    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/sre_parse.py:137(__len__)
            1    0.000    0.000    0.254    0.254 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/inspect.py:518(findsource)
            1    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/sre_compile.py:433(_compile_info)
           11    0.000    0.000    0.000    0.000 :0(ord)
            1    0.000    0.000    0.001    0.001 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/inspect.py:673(getblock)
           14    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/sre_parse.py:92(__init__)
            1    0.000    0.000    0.255    0.255 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/memory_profiler.py:412(add)
            1    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/linecache.py:72(updatecache)
            1    0.000    0.000    0.005    0.005 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/re.py:230(_compile)
            3    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/sre_compile.py:428(_simple)
            5    0.000    0.000    0.000    0.000 :0(find)
            7    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/memory_profiler.py:451(<genexpr>)
            1    0.000    0.000    0.700    0.700 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/memory_profiler.py:890(wrapper)
            6    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/inspect.py:209(iscode)
            5    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/sre_parse.py:268(_escape)
            1    0.000    0.000    0.005    0.005 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/sre_compile.py:567(compile)
            1    0.000    0.000    0.000    0.000 :0(readlines)
            1    0.000    0.000    0.255    0.255 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/memory_profiler.py:465(__call__)
            1    0.000    0.000    0.445    0.445 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/memory_profiler.py:495(f)
            1    0.000    0.000    0.003    0.003 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/sre_compile.py:552(_code)
            1    0.000    0.000    0.002    0.002 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/sre_parse.py:706(parse)
            1    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/memory_profiler.py:458(__init__)
            1    0.000    0.000    0.000    0.000 :0(open)
            1    0.000    0.000    0.255    0.255 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/inspect.py:682(getsourcelines)
            5    0.000    0.000    0.000    0.000 :0(max)
            4    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/sre_parse.py:85(closegroup)
            4    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/sre_parse.py:74(opengroup)
            3    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/inspect.py:142(isfunction)
            3    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/inspect.py:59(isclass)
            3    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/inspect.py:181(istraceback)
            3    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/inspect.py:191(isframe)
            3    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/inspect.py:67(ismethod)
            1    0.000    0.000    0.700    0.700 <string>:1(<module>)
            4    0.000    0.000    0.000    0.000 :0(remove)
            2    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/linecache.py:33(getlines)
            1    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/memory_profiler.py:528(disable_by_count)
            1    0.000    0.000    0.255    0.255 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/memory_profiler.py:479(add_function)
            1    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/memory_profiler.py:583(enable)
            1    0.000    0.000    0.000    0.000 :0(filter)
            1    0.000    0.000    0.005    0.005 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/re.py:192(compile)
            1    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/memory_profiler.py:521(enable_by_count)
            1    0.000    0.000    0.001    0.001 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/tokenize.py:156(tokenize)
            2    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/memory_profiler.py:445(items)
            2    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/sre_compile.py:546(isstring)
            1    0.000    0.000    0.000    0.000 :0(compile)
            3    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/sre_parse.py:145(__setitem__)
            1    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/memory_profiler.py:590(disable)
            2    0.000    0.000    0.000    0.000 :0(settrace)
            1    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/sre_parse.py:189(__init__)
            1    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/memory_profiler.py:408(__init__)
            1    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/sre_parse.py:67(__init__)
            1    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/memory_profiler.py:491(wrap_function)
            1    0.000    0.000    0.000    0.000 /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/inspect.py:634(__init__)
            1    0.000    0.000    0.000    0.000 :0(getattr)
            1    0.000    0.000    0.000    0.000 :0(update)
            1    0.000    0.000    0.000    0.000 :0(iter)
            1    0.000    0.000    0.000    0.000 :0(gettrace)
            0    0.000             0.000          profile:0(profiler)
    
    


指定精度可以在profile装饰器后面加上参数
如:

    @profile(precision=4)

### 基于时间的内存可视化分析


```python
%%writefile memory_test.py
from memory_profiler import profile
@profile
def foo():
    sum = 0
    for i in range(10000):
        sum += i
    return sum
if __name__=="__main__":
    foo()
```

    Overwriting memory_test.py



```python
!mprof run memory_test.py
```

    mprof: Sampling memory every 0.1s
    running as a Python program...
    Filename: memory_test.py
    
    Line #    Mem usage    Increment   Line Contents
    ================================================
         2     21.6 MiB      0.0 MiB   @profile
         3                             def foo():
         4     21.6 MiB      0.0 MiB       sum = 0
         5     21.8 MiB      0.3 MiB       for i in range(10000):
         6     21.8 MiB      0.0 MiB           sum += i
         7     21.8 MiB      0.0 MiB       return sum
    
    



```python
!mprof plot
```

    Using last profile data.


这样就可以出图了

## 对象分析及追踪

[Objgraph](http://mg.pov.lt/objgraph/)可以实现对象分析和追踪,它也是用pip安装,不过它依赖xdot(pip 安装)
和[graphviz](http://www.graphviz.org/)(brew安装)

它可以实现的功能有:

+ 统计
+ 定义过滤对象
+ 遍历和显示对象图



```python
%%writefile Obj_test.py
#encoding=utf-8  
import objgraph  
  
if __name__ == '__main__':  
    x = []  
    y = [x, [x], dict(x=x)]  
    objgraph.show_refs([y], filename='sample-graph.png') #把[y]里面所有对象的引用画出来  
    objgraph.show_backrefs([x], filename='sample-backref-graph.png') #把对x对象的引用全部画出来  
    #objgraph.show_most_common_types() #所有常用类型对象的统计，数据量太大，意义不大  
    objgraph.show_growth(limit=4) #打印从程序开始或者上次show_growth到现在增加的对象（按照增加量的大小排序）  
```

    Writing Obj_test.py



```python
!python Obj_test.py
```

    Graph written to /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/objgraph-Charrs.dot (5 nodes)
    Image generated as sample-graph.png
    Graph written to /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/objgraph-0csGnv.dot (7 nodes)
    Image generated as sample-backref-graph.png
    wrapper_descriptor             1084     +1084
    function                       1029     +1029
    builtin_function_or_method      666      +666
    method_descriptor               535      +535


于是你可以看到图了

![](sample-graph.png)
![](sample-backref-graph.png)
