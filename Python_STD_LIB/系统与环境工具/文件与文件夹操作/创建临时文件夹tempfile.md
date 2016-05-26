
# python3基础应用--创建临时文件夹(tempfile)


tempfile模块，是为创建临时文件(夹)所提供的

　
如果你的应用程序需要一个临时文件来存储数据，但不需要同其他程序共享，那么tempfile模块来创建临时文件(夹)是个不错的选择

其他的应用程序是无法找到或打开这个文件(夹),因为tempfile在创建的过程中没有引用文件系统表，用tempfile创建的临时文件(夹)，关闭

后会自动删除。


```python
import tempfile
```


```python
temp = tempfile.TemporaryFile()
try:
    print('temp : {}'.format(temp))
    print('temp.name : {}'.format(temp.name))
    temp.write(b'hello, I\'m Hongten')
    temp.seek(0)
    print('#' * 50)
    print('content : {}'.format(temp.read()))
finally:
    temp.close()  #then the system will automatically cleans up the file 
```

    temp : <_io.BufferedRandom name=74>
    temp.name : 74
    ##################################################
    content : b"hello, I'm Hongten"



```python

```
