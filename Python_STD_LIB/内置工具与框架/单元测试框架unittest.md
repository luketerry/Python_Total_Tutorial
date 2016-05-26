
# 单元测试框架(unittest)

unittest 从名字上看，它是一个单元测试框架；从官方文档的字数上看，它的能力应该比 doctest 强一些。

使用 unittest 的标准流程为：

+ 从 unittest.TestCase 派生一个子类
+ 在类中定义各种以 `"test_"` 打头的方法
+ 通过 unittest.main() 函数来启动测试

unittest 的一个很有用的特性是 TestCase 的 setUp() 和 tearDown() 方法，它们提供了为测试进行准备和扫尾工作的功能，听起来就像上下文管理器一样。这种功能很适合用在测试对象需要复杂执行环境的情况下。 




```python
!cat func_oper.py
```

    #!/usr/bin/env python
    # -*- coding:utf-8 -*-
    
    """\
    这里可以写用到多个函数的
    
    >>> summing(multiply(2,3),multiply(2,3))
    12
    
    """
    from functools import reduce
    from operator import mul,add
    
    def multiply(*args):
        """\
        这里可以写单元测试
        >>> multiply(2,3)
        6
        >>> multiply('baka~',3)
        'baka~baka~baka~'
        """
        return reduce(mul,args)
    
    def  summing(*args):
        """\
        这里可以写单元测试
        >>> summing(2,3)
        5
        >>> summing(2,3,4)
        9
        """
        return reduce(add,args)
    
    if __name__ == '__main__':
        import doctest
        doctest.testmod(verbose=True)


```python
%%writefile test_my.py
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
    
from func_oper import multiply,summing

class Test_mul(unittest.TestCase):
    def setUp(self):
        pass
    def test_number_3_4(self):
        self.assertEqual(multiply(3,4),12)
    def test_string_a_3(self):
        self.assertEqual(multiply('a',3),'aaa')
        
class Test_sum(unittest.TestCase):
    def setUp(self):
        pass
    def test_number_3_4(self):
        self.assertEqual(summing(3,4),7)
    def test_number_3_4_5(self):
        self.assertEqual(summing(3,4,5),12)
class TestCase1(unittest.TestCase):
    def setUp(self):
        pass
    def test_sum_mul_2_3_mul_2_3(self):
        self.assertEqual(summing(multiply(2,3),multiply(2,3)),12)

if __name__ == '__main__':
    unittest.main()

```

    Overwriting test_my.py


> 调用测试文件测试


```python
%run test_my.py -v
```

    test_sum_mul_2_3_mul_2_3 (__main__.TestCase1) ... ok
    test_number_3_4 (__main__.Test_mul) ... ok
    test_string_a_3 (__main__.Test_mul) ... ok
    test_number_3_4 (__main__.Test_sum) ... ok
    test_number_3_4_5 (__main__.Test_sum) ... ok
    
    ----------------------------------------------------------------------
    Ran 5 tests in 0.004s
    
    OK


> 命令行启动测试


```python
!python -m unittest discover -v
```

    test_sum_mul_2_3_mul_2_3 (test_my.TestCase1) ... ok
    test_number_3_4 (test_my.Test_mul) ... ok
    test_string_a_3 (test_my.Test_mul) ... ok
    test_number_3_4 (test_my.Test_sum) ... ok
    test_number_3_4_5 (test_my.Test_sum) ... ok
    
    ----------------------------------------------------------------------
    Ran 5 tests in 0.000s
    
    OK

