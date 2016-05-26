
# 通用路径控制(os.path)

os.path下有这些操作:


操作|说明
---|---
os.path.abspath(相对路径)|获取绝对路径
os.getcwd()|获取当前绝对路径
os.walk(path)|遍历path目录下的所有文件并返回(python2中为os.path.walk)
os.path.splitext(path)|拆分路径文件名和扩展名
os.path.split(Path)|拆分路径和最近的一个文件夹
os.join(path1,path2)|将路径和路径合并,可以避免不同平台符号不同的问题
os.mkdir(path)|新建目录
os.rmdir(path)|删除目录
os.listdir(path)|查看path下有什么文件文件夹,只看这一层
os.rename(path, name)|重命名
os.remove(path)|删除文件
os.path.isfile()|判断是不是文件
os.path.isdir()|判断是不是文件夹
os.path.exists()|判断是否存在这个路径
os.path.getsize(path)|获取文件大小
os.path.getatime(path)|获取文件修改时间
os.path.getctime(path)|获取文件创建时间
os.stat(path)|获取文件夹或文件信息




```python
import os
```


```python
# 查看当前目录的绝对路径:
os.path.abspath('.')
```




    '/Users/huangsizhe/workspace/post/计算机编程/编程语言/Python_Total_Tutorial/标准库/系统与环境工具/文件与文件夹操作'




```python
os.getcwd()
```




    '/Users/huangsizhe/workspace/post/计算机编程/编程语言/Python_Total_Tutorial/标准库/系统与环境工具/文件与文件夹操作'




```python
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
Path = os.path.join(os.path.abspath('.'), 'testdir')
#合并路径用join可以避免不同平台符号不同的问题
```


```python
#拆分文件扩展名
os.path.splitext(
    '/Users/huangsizhe/workspace/post/计算机编程/编程语言/Python_Total_Tutorial/标准库/系统与环境工具/文件与文件夹操作')
```




    ('/Users/huangsizhe/workspace/post/计算机编程/编程语言/Python_Total_Tutorial/标准库/系统与环境工具/文件与文件夹操作',
     '')




```python
#新建目录
os.mkdir(Path)
```


```python
# 删掉一个目录:
os.rmdir(Path)
```


```python
#拆分目录
Path,_ = os.path.split(Path)
Path
```




    '/Users/huangsizhe/workspace/post/计算机编程/编程语言/Python_Total_Tutorial/标准库/系统与环境工具/文件与文件夹操作'




```python
Path = os.path.join(Path,'source','f1.txt.bak')
Path
```




    '/Users/huangsizhe/workspace/post/计算机编程/编程语言/Python_Total_Tutorial/标准库/系统与环境工具/文件与文件夹操作/source/f1.txt.bak'




```python
#查看有什么文件文件夹
os.listdir('./source')
```




    ['.DS_Store', 'f1', 'f1.txt', 'f2.txt', 'newbee.txt', 'readme.md']




```python
type(os.listdir('./source')[1])
```




    str




```python
#重命名
os.rename(Path, './source/readme.md')
```


```python
#删除文件
os.remove('./source/f2.txt.bak')
```


```python
list(os.walk(os.getcwd()))
```




    [('/Users/huangsizhe/workspace/post/计算机编程/编程语言/Python_Total_Tutorial/标准库/系统与环境工具/文件与文件夹操作',
      ['.ipynb_checkpoints', 'source'],
      ['创建临时文件夹(tempfile).ipynb',
       '多文件输入(fileinput).ipynb',
       '文件比较(filecmp).ipynb',
       '系统,文件,文件夹操作(os,filecmp,difflib).ipynb',
       '通用路径控制(os.path).ipynb',
       '高级文件操作(shutil).ipynb']),
     ('/Users/huangsizhe/workspace/post/计算机编程/编程语言/Python_Total_Tutorial/标准库/系统与环境工具/文件与文件夹操作/.ipynb_checkpoints',
      [],
      ['多文件输入(fileinput)-checkpoint.ipynb',
       '文件比较(filecmp)-checkpoint.ipynb',
       '通用路径控制(os.path)-checkpoint.ipynb',
       '高级文件操作(shutil)-checkpoint.ipynb']),
     ('/Users/huangsizhe/workspace/post/计算机编程/编程语言/Python_Total_Tutorial/标准库/系统与环境工具/文件与文件夹操作/source',
      [],
      ['f1.txt', 'f2.txt', 'readme.md'])]




```python
os.stat(os.getcwd())
```




    os.stat_result(st_mode=16877, st_ino=7513348, st_dev=16777217, st_nlink=10, st_uid=501, st_gid=20, st_size=340, st_atime=1452234419, st_mtime=1452234381, st_ctime=1452234381)


