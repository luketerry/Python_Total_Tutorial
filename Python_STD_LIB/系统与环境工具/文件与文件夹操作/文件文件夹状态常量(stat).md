
# 文件文件夹状态常量(stat)

stat模块提供了状态常量和判断是否是这些状态的方法:


常用的状态有:

+ st_mode -- protection bits(模式)
 
+ st_ino -- inode number(索引号)
 
+ st_dev -- device(设备)

+ st_nlink -- number of hard links(硬链接号)

+ st_uid -- user id of owner(用户id)

+ st_gid -- group id of owner (组id)

+ st_size -- size of file,in bytes (大小)

+ st_atime -- time of most recent access expressed in seconds (访问时间)

+ st_mtime -- time of most recent content modificatin expressed in seconds (修改时间)

+ st_ctime -- platform dependent;time of most recent metadata change on Unix,or the teime of creation on Windows,expressed in senconds (根据不同操作系统而定)


常用的方法有:

+ stat.S_ISREG( fileStats [ stat.ST_MODE ] )          判断是否一般文件

+ stat.S_ISLNK ( fileStats [ stat.ST_MODE ] )         判断是否链接文件

+ stat.S_ISSOCK ( fileStats [ stat.ST_MODE ] )        判断是否套接字文件    

+ stat.S_ISFIFO ( fileStats [ stat.ST_MODE ] )        判断是否命名管道

+ stat.S_ISBLK ( fileStats [ stat.ST_MODE ] )         判断是否块设备

+ stat.S_ISCHR ( fileStats [ stat.ST_MODE ] )         判断是否字符设置


```python
import os, sys
from stat import *

def walktree(top, callback):
    '''recursively descend the directory tree rooted at top,
       calling the callback function for each regular file'''

    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.stat(pathname).st_mode
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            walktree(pathname, callback)
        elif S_ISREG(mode):
            # It's a file, call the callback function
            callback(pathname)
        else:
            # Unknown file type, print a message
            print('Skipping %s' % pathname)

def visitfile(file):
    print('visiting', file)


walktree("source", visitfile)
```

    visiting source/f1.txt
    visiting source/f2.txt
    visiting source/newbee.txt
    visiting source/readme.md

