
很多人会问到`__builtin__`、`__builtins__`和`builtins`之间有什么关系。这边就聊聊python的内建模块.


在Python中，有一个内建模块,也就是python的变量名作用域规则`LEGB`中的`B`，该模块中有一些常用函数.

而该模块在Python启动后、且没有执行程序员所写的任何代码前，Python会首先加载该内建函数到内存。另外，该内建模块中的功能可以直接使用，不用在其前添加内建模块前缀.简单回顾下`LEBG`

> LEGB


```python
%%writefile LEGB_test.py
#coding:utf-8
from __future__ import unicode_literals
from math import sin
import sys
print sin(int(sys.argv[1]))
```

    Writing LEGB_test.py



```python
!python LEGB_test.py 1
```

    0.841470984808



```python
%%writefile LEGB_test.py
#coding:utf-8
from __future__ import unicode_literals
from math import sin
import sys
def sin(n):
    import math
    return "这是G中的sin"+str(math.sin(n))
print sin(int(sys.argv[1]))
```

    Overwriting LEGB.test



```python
!python LEGB_test.py 1
```

    这是G中的sin0.841470984808



```python
%%writefile LEGB_test.py
#coding:utf-8
from __future__ import unicode_literals
from math import sin
import sys
def sin(n):
    import math
    return "这是G中的sin"+str(math.sin(n))
def main():
    def sin(n):
        import math
        return "这是E中的sin"+str(math.sin(n))
    def pr():
        print sin(int(sys.argv[1]))
    pr()
        
if __name__ == "__main__":
    main()
```

    Overwriting LEGB.test



```python
!python LEGB_test.py 1
```

    0.841470984808



```python
%%writefile LEGB_test.py
#coding:utf-8
from __future__ import unicode_literals
from math import sin
import sys
def sin(n):
    import math
    return "这是G中的sin"+str(math.sin(n))
def main():
    def sin(n):
        import math
        return "这是E中的sin"+str(math.sin(n))
    def pr():
        def sin(n):
            import math
            return "这是L中的sin"+str(math.sin(n))
        print sin(int(sys.argv[1]))
    pr()
        
if __name__ == "__main__":
    main()
```

    Overwriting LEGB_test.py



```python
!python LEGB_test.py 1
```

    这是L中的sin0.841470984808


关于`E和L`我们已经在进阶部分有过讨论了,今天主要讨论的是`G和B`的部分

> 内建模块添加`__builtin__`和builtins

内建模块被命名为`__builtin__`，而到了Python3.X版本中，却更名为`builtins`。

当使用内建模块中函数或其它功能时，可以直接使用，不用添加内建模块的名字;但是，如果想要向内建模块中添加一些功能，以便在任何函数中都能直接使用而不 用再进行import，这时，就要导入内建模块，在内建模块的命名空间(即__dict__字典属性)中添加该功能。在导入时，如果是Python2.X 版本，就要导入__builtin__模块;如果是Python3.X版本，就要导入builtins模块。如：在Python2.X中，向内建模块添加 一个函数(该函数打印“hello, world”)，可以这样写(以下的用法是在主模块中的使用，其它模块请看下面)：


```python
%%writefile B_test.py
#coding:utf-8
import __builtin__
def print_hello():
    print "hello, world"
__builtin__.__dict__['hello'] = print_hello
print_hello() # 将打印"hello, world"
hello() # 将打印"hello, world"
```

    Writing B_test.py



```python
!python B_test.py
```

    hello, world
    hello, world


此时，print_hello和hello两个函数名几乎是一样，但是有一点区别，print_hello只能在该模块中使用，而hello可以在本程序中的其它任何一个模块中使用，因为hello已经放到内建模块中了.

为了统一Python2.X和Python3.X，在下面的论述中，内建模块一律统称为`__builtin__`.

> `__builtins__`内建模块引用

我们知道，`__builtin__`存在于Python2.X中，而builtins存在于Python3.X中，但是对于 `__builtins__`，它却同时存在于Python2.X和Python3.X中。那么它到底是什么东西呢?由名字可知，它肯定与内建模块有关。其实 简单地说，它就是对内建模块一个引用。

1. `__builtins__`即是引用，那么它内建模块有一个相同点：Python程序一旦启动，它们二者就会在程序员所写的代码没有运行之前就已经被加载到内存中了。
2. 虽是一个引用，但__builtins__和内建模块是有一点区别的：

    + 无论任何地方要想使用内建模块，都必须在该位置所处的作用域中导入`__builtin__`内建模块;而对于`__builtins__`却不用导入，它在任何模块都直接可见， 可以把它当作内建模块直接使用(这句并不完全正确，请看下一条。即：`__builtins__`在任何地方、任何模块都可见，而内建模块名只在相应的 作用域中被import后才可以(该import并不是把内建模块加载到内存中——内建早已经被加载了，它仅仅是让内建模块名在该作用域中可见)。
    
    + `__builtins__`虽是对内建模块的引用，但这个引用要看是使用`__builtins__`的模块是哪个模块：
            
        1. 在主模块`__main__`中：
            `__builtins__`是对内建模块`__builtin__`本身的引用，即`__builtins__`完全等价于`__builtin__`，二者完全是一个东西，不分彼此。它在任何地方都可见，即在任何地方都可使用它。此时，`__builtins__`的类型是模块类型。
            `__builtin__`仅仅在导入它时才可见。哪个作用域中使用`__builtin__`，哪个作用域就要导入它(导入仅仅是让`__builitin__`标 识符在该作用域内可见)。一般都是在模块的顶层(即模块的全局作用域)导入`__builtin__`，这样，其后的任何作用域可通过标识符向上查找来引用 `__builtin__`。
        2. 在非`__main__`模块中：
            `__builtins__`仅是对`__builtin__`.`__dict__`的引用，而非`__builtin__`本身。它在任何地方都可见。此时`__builtins__`的类型是字典。
            `__builtin__`和在主模块中的情况一样。

## 总结

我们可以看出，`__builtins__`、`__builtin__`和`builtins`之间并没有太大的不同;在使用`__builtins__`时，只要注意其引用的到底是`__builtin__`还是`__builtin__.__dict__`即可。

此时，可能会有人说，既然`__builtin__`和`builtins`由于Python版本的不同而不同，导致在写兼容2.X和3.X版本时的代码时比较麻烦，而`__builtins__`在2.X和3.X中都是一样的，那么，不再使用`builtins`和`__builin__`，改用`__builtins__`不是更好?!

是的这种做法并没有错!但是有一点，在使用`__builtins__`时，要区分是在主模块`__main__`中，还是在其他的非`__main__`模块 中。Python标准库(比如gettext)中就使用的是`__builtin__`(在Python2.X中)和`builtins`(在 Python3.X中)，而并没有使用`__builtins__`。所以说没准会有一些其他的玄机

ps：

主模块`__main__`：在Python中，一个代码文件就是一个模块，一个模块就是一个代码文件;用来启动Python或者说首先执行的那个文件(相当 于C语言中main主函数所在的C文件)的模块名被Python命名为`__main__`，称为主模块，而对于其它被主模块或其他非主模块导入的模块，它们 的模块名则是文件名本身(除了后缀.py、.pyc或.pyo等)。每个模块都有一个名为`__name__`的属性，它表示着该模块的名字。除此之外，主模 块与其它非主模块之间还有一点区别，比如：

`from __future__ import absolute_import`语句在非主模块中可以正常使用，反而在主模块中，好像没有什么效果——有等无。
