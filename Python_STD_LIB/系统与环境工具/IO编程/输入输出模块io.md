
# 输入输出模块(io)

IO编程就是处理文件.文件操作基本上可以看做有读操作和写操作

python的打开一个文件用命令`open`,无论读还是写都必须先打开,操作完之后也必须要用`close()`将其关闭,但现在用`with ... as`语句,可以不要再写`close()`了

    with open(path, 'rwb', encoding='gbk', errors='ignore') as f:
        XXXX

## 读:



> `readline`一行一行读,返回一个生成器,一次读取一行


```python
# 读文本文件
with open('source/README.md', 'r') as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())
```

    # Apache Spark
    
    
    
    Spark is a fast and general cluster computing system for Big Data. It provides
    


> `readlines`一行一行读,返回整个列表,列表中每一个元素是一行


```python
with open('source/README.md', 'r') as f:
    print(f.readlines()[:5])
```

    ['# Apache Spark\n', '\n', 'Spark is a fast and general cluster computing system for Big Data. It provides\n', 'high-level APIs in Scala, Java, and Python, and an optimized engine that\n', 'supports general computation graphs for data analysis. It also supports a\n']


> 直接读取生成字符串


```python
with open('source/README.md', 'r') as f:
    print(f.read()[:5])
```

    # Apa


>读取图片等2进制数据,后面的参数中加入`b`


```python
with open('source/LBQ.jpg', 'rb') as f:
    print(f.read()[:20])
```

    b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00'


## 写:



```python
string = """我是一只小鸭子咿呀咿呀呦
是一只小鸭子咿呀咿呀呦
一只小鸭子咿呀咿呀呦
只小鸭子咿呀咿呀呦
小鸭子咿呀咿呀呦
鸭子咿呀咿呀呦
子咿呀咿呀呦
咿呀咿呀呦
呀咿呀呦
咿呀呦
呀呦
呦
这是回声
"""
with open('source/newbee.txt', 'w') as f:
    f.write(string)
```

## 内存读写 StringIO和BytesIO


很多时候，数据读写不一定是文件，也可以在内存中读写。在2.7中,string和byte不分家,所以有个库叫cStringIO用来处理内存读写.

python3中则提供了专门的IO库,我们可以利用它来实现内存读写

StringIO顾名思义就是在内存中读写str。而BytesIO也就是在内存中读写二进制数据了


```python
from io import StringIO,BytesIO
```

### 写


```python
f = StringIO()
f.write('hello')
```




    5




```python
f.write(' ')
```




    1




```python
f.write('world!')
```




    6




```python
print(f.getvalue())
```

    hello world!



```python
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
```

    b'\xe4\xb8\xad\xe6\x96\x87'


### 读


```python
f = StringIO('Hello!\nHi!\nGoodbye!')
f.read()
```




    'Hello!\nHi!\nGoodbye!'




```python
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()
```




    b'\xe4\xb8\xad\xe6\x96\x87'



## 文件及文件夹操作

python提供了`os`模块来操作操作系统的文件系统


```python
import os
```

### 系统信息


```python
os.name # 操作系统类型
```




    'posix'



如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。


```python
os.uname()
```




    posix.uname_result(sysname='Darwin', nodename='hszMba.local', release='14.5.0', version='Darwin Kernel Version 14.5.0: Wed Jul 29 02:26:53 PDT 2015; root:xnu-2782.40.9~1/RELEASE_X86_64', machine='x86_64')



### 环境变量


```python
os.environ
```




    environ({'SHLVL': '1', 'CLICOLOR': '1', 'LUA_PATH': '/Users/huangsizhe/.luarocks/share/lua/5.1/?.lua;/Users/huangsizhe/.luarocks/share/lua/5.1/?/init.lua;/Users/huangsizhe/torch/install/share/lua/5.1/?.lua;/Users/huangsizhe/torch/install/share/lua/5.1/?/init.lua;./?.lua;/Users/huangsizhe/torch/install/share/luajit-2.1.0-alpha/?.lua;/usr/local/share/lua/5.1/?.lua;/usr/local/share/lua/5.1/?/init.lua', 'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.sjU1LTVbmR/Listeners', 'TERM': 'xterm-color', 'CATALINA_BASE': '/Users/huangsizhe/workspace/Framework/tomcat/apache-tomcat-8.0.26', 'JAVA_HOME': '/Library/Java/JavaVirtualMachines/jdk1.8.0_51.jdk/Contents/Home', 'GOPATH': '/Users/huangsizhe/workspace/STUDY/LANGUAGE/go/mygo:/Users/huangsizhe/workspace/STUDY/LANGUAGE/go/mygo01', 'XPC_FLAGS': '0x0', '__CF_USER_TEXT_ENCODING': '0x1F5:0x19:0x34', 'PAGER': 'cat', 'LANG': 'zh_CN.UTF-8', 'DISPLAY': '/private/tmp/com.apple.launchd.2A3Hd8hnPt/org.macosforge.xquartz:0', 'USER': 'huangsizhe', 'CLASSPATH': ':/Users/huangsizhe/workspace/Framework/tomcat/apache-tomcat-8.0.26/common/lib/jsp-api.jar', 'JPY_PARENT_PID': '533', 'TMPDIR': '/var/folders/8z/vx2qsp9d7bs5wxkvm2t44xfr0000gn/T/', 'TERM_PROGRAM_VERSION': '343.7', 'SHELL': '/bin/bash', 'LOGNAME': 'huangsizhe', 'GIT_PAGER': 'cat', 'TERM_PROGRAM': 'Apple_Terminal', 'APACHE_SPARK_VERSION': '1.4.1', '_': '/usr/local/bin/jupyter', 'LD_LIBRARY_PATH': '/Users/huangsizhe/torch/install/lib:', 'Apple_PubSub_Socket_Render': '/private/tmp/com.apple.launchd.1lLuNbFxbq/Render', 'PS1': '\\[\\033[01;32m\\]\\u@\\h\\[\\033[00m\\]:\\[\\033[01;36m\\]\\w\\[\\033[00m\\]\\$ ', 'PWD': '/Users/huangsizhe', 'LUA_CPATH': '/Users/huangsizhe/.luarocks/lib/lua/5.1/?.so;/Users/huangsizhe/torch/install/lib/lua/5.1/?.so;./?.so;/usr/local/lib/lua/5.1/?.so;/usr/local/lib/lua/5.1/loadall.so', '__PYVENV_LAUNCHER__': '/usr/local/Cellar/python3/3.5.0/bin/python3.5', 'HOME': '/Users/huangsizhe', 'CATALINA_HOME': '/Users/huangsizhe/workspace/Framework/tomcat/apache-tomcat-8.0.26', 'LSCOLORS': 'gxfxcxdxbxegedabagacad', 'XPC_SERVICE_NAME': '0', 'ANDROID_HOME': '/usr/local/opt/android-sdk', 'TERM_SESSION_ID': 'CE37796D-5338-4667-947B-129E17750481', 'DYLD_LIBRARY_PATH': '/Users/huangsizhe/torch/install/lib:', 'PATH': '/Users/huangsizhe/torch/install/bin:/Users/huangsizhe/workspace/Framework/tomcat/apache-tomcat-8.0.26/bin:/Users/huangsizhe/workspace/Framework/tomcat/apache-tomcat-8.0.26/lib:/Users/huangsizhe/workspace/STUDY/LANGUAGE/go/mygo/bin:/Users/huangsizhe/workspace/STUDY/LANGUAGE/go/mygo01/bin:/Users/huangsizhe/node_modules/.bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin'})




```python
os.environ.get('JAVA_HOME')
```




    '/Library/Java/JavaVirtualMachines/jdk1.8.0_51.jdk/Contents/Home'



### 操作文件和文件夹


```python
# 查看当前目录的绝对路径:
os.path.abspath('.')
```




    '/Users/huangsizhe/workspace/STUDY/LANGUAGE/Python/ipython3/由浅入深/Python3基础应用'




```python
os.getcwd()
```




    '/Users/huangsizhe/workspace/STUDY/LANGUAGE/Python/ipython3/由浅入深/Python3基础应用'




```python
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
Path = os.path.join(os.path.abspath('.'), 'testdir')
#合并路径用join可以避免不同平台符号不同的问题
```


```python
#拆分文件扩展名
os.path.splitext(
    '/Users/huangsizhe/workspace/STUDY/LANGUAGE/Python/ipython3/由浅入深/Python3基础应用/python3基础应用--IO编程.ipynb')
```




    ('/Users/huangsizhe/workspace/STUDY/LANGUAGE/Python/ipython3/由浅入深/Python3基础应用/python3基础应用--IO编程',
     '.ipynb')




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




    '/Users/huangsizhe/workspace/STUDY/LANGUAGE/Python/ipython3/由浅入深/Python3基础应用'




```python
Path = os.path.join(Path,'source','tes.txt')
Path
```




    '/Users/huangsizhe/workspace/STUDY/LANGUAGE/Python/ipython3/由浅入深/Python3基础应用/source/tes.txt'




```python
with open(Path,"w") as file:
    file.write("qwert")

```


```python
with open(Path,"r") as file:
    print(file.read())
```

    qwert



```python
#查看有什么文件文件夹
os.listdir('./source')
```




    ['.DS_Store', 'LBQ.jpg', 'newbee.txt', 'README.md', 'tes.txt']




```python
os.rename(Path, './source/test.txt')
```


```python
os.listdir('./source')
```




    ['.DS_Store', 'LBQ.jpg', 'newbee.txt', 'README.md', 'test.txt']




```python
os.remove('./source/test.txt')
```


```python
os.listdir('./source')
```




    ['.DS_Store', 'LBQ.jpg', 'newbee.txt', 'README.md']




```python
# 运行shell命令
#os.system("atom")
```


```python
#判断是不是文件
os.path.isfile(os.getcwd())
```




    False




```python
#判断是不是文件夹
os.path.isdir(os.getcwd())
```




    True




```python
#判断是否存在
os.path.exists(os.getcwd())
```




    True




```python
#获取文件大小
os.path.getsize("./source/LBQ.jpg")
```




    29248




```python
import time
```


```python
#获取文件的修改时间:

time.ctime(os.path.getatime("./source/LBQ.jpg"))
```




    'Thu Sep 24 05:31:16 2015'




```python
#获取文件的创建时间:

time.ctime(os.path.getctime("./source/LBQ.jpg"))
```




    'Wed Sep 23 15:02:49 2015'




```python
from __future__ import absolute_import, print_function, unicode_literals


```


```python


```


```python
def captcha():
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
    import random
    import cStringIO
    # 随机字母:
    def rndChar():
        return chr(random.randint(65, 90))

    # 随机颜色1:
    def rndColor():
        return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

    # 随机颜色2:
    def rndColor2():
        return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
    while True:
        width = 60 * 4
        height = 60
        image = Image.new('RGB', (width, height), (255, 255, 255))
        # 创建Font对象:
        font = ImageFont.truetype('Arial.ttf', 36)
        # 创建Draw对象:
        draw = ImageDraw.Draw(image)
        # 填充每个像素:
        for x in range(width):
            for y in range(height):
                draw.point((x, y), fill=rndColor())
        # 输出文字:
        for t in range(4):
            draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
        # 模糊:
        buf = cStringIO.StringIO() 
        image.save(buf, format=u'png')
        #help(image.save)
        result = buf.getvalue()
        import base64
        result = base64.b64encode(result)
        yield result

```


```python
s = captcha()
```


```python
a = next(s)
```


```python
b = next(s)
```


```python
a == b
```




    False




```python
with open("a.html","wb") as ss:
    ss.write(s)
```


```python

```
