
# 文件文件夹比较(filecmp)

+ filecmp.cmp(f1, f2[, shallow])

 比较两个文件的内容是否匹配。参数f1, f2指定要比较的文件的路径。可选参数shallow指定比较文件时是否需要考虑文件本身的属性（通过os.stat函数可以获得文件属性）。如果文件内容匹配，函数返回True，否则返回False。

+ filecmp.cmpfiles(dir1, dir2, common[, shallow])

比较两个文件夹内指定文件是否相等。参数dir1, dir2指定要比较的文件夹，参数common指定要比较的文件名列表。函数返回包含3个list元素的元组，分别表示匹配、不匹配以及错误的文件列表。错误的文件指的是不存在的文件，或文件被琐定不可读，或没权限读文件，或者由于其他原因访问不了该文件。

filecmp模块中定义了一个dircmp类，用于比较文件夹，通过该类比较两个文件夹，可以获取一些详细的比较结果（如只在A文件夹存在的文件列表），并支持子文件夹的递归比较。

dircmp提供了三个方法用于报告比较的结果：

+ report()：只比较指定文件夹中的内容（文件与文件夹）
+ report_partial_closure()：比较文件夹及第一级子文件夹的内容
+ report_full_closure()：递归比较所有的文件夹的内容


```python
import filecmp
```


```python
filecmp.cmp("source/newbee.txt","source/readme.md")
```




    False


