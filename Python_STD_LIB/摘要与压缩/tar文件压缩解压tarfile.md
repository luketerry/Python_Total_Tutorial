
# tar文件压缩解压(tarfile)

这次的是对tar文件的压缩解压模块

> `Tarfile.open(cls, name=None, mode='r', fileobj=None, bufsize=10240, **kwargs)`

  mode:
  
    'r' or 'r:*' open for reading with transparent compression
    'r:'         open for reading exclusively uncompressed
    'r:gz'       open for reading with gzip compression
    'r:bz2'      open for reading with bzip2 compression
    'a' or 'a:'  open for appending, creating the file if necessary
    'w' or 'w:'  open for writing without compression
    'w:gz'       open for writing with gzip compression
    'w:bz2'      open for writing with bzip2 compression
   
    'r|*'        open a stream of tar blocks with transparent compression
    'r|'         open an uncompressed stream of tar blocks for reading
    'r|gz'       open a gzip compressed stream of tar blocks
    'r|bz2'      open a bzip2 compressed stream of tar blocks
    'w|'         open an uncompressed stream for writing
    'w|gz'       open a gzip compressed stream for writing
    'w|bz2'      open a bzip2 compressed stream for writing
 

## 创建压缩包


```python
import os
```


```python
with tarfile.open("tartest.tar.gz","w:gz") as tar:
    for root,dir,files in os.walk("in"):
        for file in files:
            fullpath = os.path.join(root,file)
            tar.add(fullpath)

```

## 解压


```python
with tarfile.open("tartest.tar.gz") as tar:
    names = tar.getnames()
    for name in names:
       tar.extract(name,path="out")
```


```python

```
