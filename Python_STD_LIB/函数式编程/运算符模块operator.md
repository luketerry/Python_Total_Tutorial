
# 运算符模块(operator)

operator模块提供了一系列的符号操作,比如`operator.add(x, y)`等于`x+y`.

它长作为方法与map,reduce等函数式编程工具配合使用.


```python
import operator
```


```python
c = list(map(operator.mul,range(2,6),range(3,7)))
print(c)
```

具体符号如下:

Operation|	Syntax|	Function
---|---|---
Addition|	a + b	|add(a, b)
Concatenation|	seq1 + seq2	|concat(seq1, seq2)
Containment Test|	obj in seq	|contains(seq, obj)
Division|	a / b	|truediv(a, b)
Division|	a // b	|floordiv(a, b)
Bitwise And|	a & b	|and\_(a, b)
Bitwise Exclusive Or|	a ^ b	|xor(a, b)
Bitwise Inversion|	~ a	|invert(a)
Bitwise Or|	a l b	|or\_(a, b)
Exponentiation|	a \*\* b	|pow(a, b)
Identity|	a is b	|is\_(a, b)
Identity|	a is not b	|is\_not(a, b)
Indexed Assignment|	obj[k] = v	|setitem(obj, k, v)
Indexed Deletion|	del obj[k]	|delitem(obj, k)
Indexing|	obj[k]	|getitem(obj, k)
Left Shift|	a << b	|lshift(a, b)
Modulo|	a % b	|mod(a, b)
Multiplication|	a \* b	|mul(a, b)
Matrix Multiplication|	a @ b	|matmul(a, b)
Negation (Arithmetic)|	- a	|neg(a)
Negation (Logical)|	not a	|not\_(a)
Positive|	+ a	|pos(a)
Right Shift|	a >> b	|rshift(a, b)
Slice Assignment|	seq[i:j] = values	|setitem(seq, slice(i, j), values)
Slice Deletion|	del seq[i:j]	|delitem(seq, slice(i, j))
Slicing	|seq[i:j]|	getitem(seq, slice(i, j))
String Formatting|	s % obj	|mod(s, obj)
Subtraction|	a - b|	sub(a, b)
Truth Test|	obj	|truth(obj)
Ordering|	a < b	|lt(a, b)
Ordering|	a <= b	|le(a, b)
Equality|	a == b	|eq(a, b)
Difference|	a != b	|ne(a, b)
Ordering|	a >= b	|ge(a, b)
Ordering|	a > b	|gt(a, b)
Matrix Multiplication|a @ b|matmul(a, b)

