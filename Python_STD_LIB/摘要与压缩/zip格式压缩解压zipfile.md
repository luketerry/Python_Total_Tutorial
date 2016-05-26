
# zip格式压缩解压(zipfile)

从简单的角度来看的话，zip压缩格式是个不错的选择.python对zip格式的支持够简单，够好用。


```python
import zipfile
```

## 简单应用

> 文本压缩成zip文件


```python
with zipfile.ZipFile('output.zip', 'w',zipfile.ZIP_DEFLATED) as f:
    f.write("input副本.txt")
```


```python
!rm input副本.txt
```


```python
with zipfile.ZipFile('output.zip', 'r',zipfile.ZIP_DEFLATED) as f:
    f.extractall()
```

+ zipfile.ZipFile(fileName[, mode[, compression[, allowZip64]]]) 

    + mode和一般的文件操作一样,'r'表示打开一个存在的只读ZIP文件；'w'表示清空并打开一个只写的ZIP文件，或创建一个只写的ZIP文件；'a'表示打开一个ZIP文件，并添加内容。 
    + compression表示压缩格式，可选的压缩格式只有2个：ZIP_STORE;ZIP_DEFLATED。ZIP_STORE是默认的，表示不压缩；ZIP_DEFLATED表示压缩，如果你不知道什么是Deflated。 
    + allowZip64为True时，表示支持64位的压缩，一般而言，在所压缩的文件大于2G时，会用到这个选项；默认情况下，该值为False，因为Unix系统不支持。 
+ zipfile.write(filename[, arcname[, compress_type]]) 
    + acrname是压缩文件中该文件的名字，默认情况下和filename一样 
    + compress_type的存在是因为zip文件允许被压缩的文件可以有不同的压缩类型。
+ zipfile.extractall([path[, member[, password]]]) 
    + path解压缩目录，没什么可说的 
    + member需要解压缩的文件名儿列表 
    + password当zip文件有密码时需要该选项 

## 高级


```python
zipfile.is_zipfile("output.zip") #查看是不是zip压缩文件
```




    True




```python
# 查看zip中的文件列表
with zipfile.ZipFile('output.zip', 'r',zipfile.ZIP_DEFLATED) as f:
    print(f.namelist())
```

    ['input副本.txt']



```python
# 打开zip中某个文件
with zipfile.ZipFile('output.zip', 'r',zipfile.ZIP_DEFLATED) as f:
    print(f.open('input副本.txt').read().decode("utf-8"))
```

    强大的交互执行框架--Jupyter及其支持的几种优秀语言介绍
    
    Jupyter 是ipython notebook 脱离ipython项目后的一个独立项目.不同于notebook, Jupyter已经不再只是python的交互执行框架,
    而是致力于多语言通用的交互执行.
    
    在以前 notebook作为ipython的一个子项目就受到许多人的喜爱和追捧,当时就已经可以通过多种途径利用它执行其他非python语言.
    现在Jupyter 与ipython分家后,这一特性得到了更好的支持.
    
    现在的Jupyter只负责交互执行,而执行的是什么语言其实是由其执行核心--kernel 来实现的,而现在的ipython可以自带其执行python版本的python核心.
    
    于是顺带的,本文也介绍几种支持Jupyter的优秀的语言.
    
    ## Jupyter支持的语言:
    
    在[这里](https://github.com/ipython/ipython/wiki/IPython-kernels-for-other-languages)你可以看到目前支持的语言.
    
    
    ## Jupyter的安装:
    
    Jupyter 现在是独立安装.当然,你依然需要装有python 和 pip.
    
    
        $pip install jupyter
    
    如果你用brew 安装的python3,那么自然的
    
        $pip3 install jupyter
    
    ## 运行
    
        $jupyter notebook
    
    
        当然了,没有kernel是没法运行的
    
    
    ## 几个比较值得安装的的kernel安装:
    
    本文中介绍的的kernel只在mac下测试安装成功,在linux下应当都能成功,但windows下未必.
    欢迎朋友们写下其他平台的经验,我看到也会进行修改,谢谢
    
    ### 通用依赖
    几乎所有kernel都需要`zeromq`和`openssl`这两个库,他们都可以用brew安装
    
    brew install zeromq
    brew install openssl
    
    > python2与python3并存
    
    ### 安装依赖
    
    python的kernel自然依赖于python.
    
    对于新手来说python2和python3并存本身就是件比较纠结蛋碎的事儿,mac下一般会用homebrew安装两个版本
    (当然也会有人安装其他比如pypy之类,那个咱不管)
    
        $brew install python
        $brew install python3
    
    
    如果是这样安装,那python python2 python3对应的便是不同版本的python如下表(可能版本不同有些许不同)
    
    命令|python来源|pip命令|库位置
    ---|---|---|---
    python|brew 安装的 python|pip|/usr/local/lib/python2.7/site-packages
    python2|brew 安装的 python|pip|/usr/local/lib/python2.7/site-packages
    python3|brew 安装的 python3|pip3|/usr/local/lib/python3.4/site-packages
    
    
    ### 安装kernel
    
    **分别安装ipython,在各自环境下执行**
    
        $pip install ipython[all]
        $ipython kernelspec install-self
        $pip3 install ipython[all]
        $ipython kernelspec install-self
    
    ### 测试下
    
    打开Jupyter:
    
        jupyter notebook
    
    可以在*new*看到里面出现*Python 2*和*Python 3*两个可选项
    
    >Bash
    
    Bash 不用多介绍,最通用的shell命令语言,同时它的kernel也是安装起来最简单的kernel了.
    
    ### 安装Bash-kernel
    
    安装Bash-kernel只要用pip工具即可
    
        pip install bash_kernel
        python -m bash_kernel.install
    
    ### 测试下
    
    新建一个bash用的notebook
    在其中的一个cell中输入
    
        for i in {1..5}
        do  
            echo $i  
        done  
    
    
    看看是不是输出了1到5这5个数
    
    更多的bash语言细节可以[点击这里查看](http://www.yiibai.com/shell/)
    
    >Golang
    
    Go语言是谷歌几年前推出的一门编译型语言,它以简洁优雅高,高开发效率,高可维护性和善于处理高并发而著称
    Go有一套完善的开发流程和语言规范,而在Jupyter下执行Go主要是用于学习其语言特性



```python
# 查看zip的信息列表
with zipfile.ZipFile('output.zip', 'r',zipfile.ZIP_DEFLATED) as f:
    print(f.infolist())
```

    [<ZipInfo filename='input副本.txt' compress_type=deflate filemode='-rw-r--r--' file_size=3425 compress_size=1778>]



```python
# 查看zip中某文件的信息
with zipfile.ZipFile('output.zip', 'r',zipfile.ZIP_DEFLATED) as f:
    info = f.getinfo('input副本.txt')
print(info)
```

    <ZipInfo filename='input副本.txt' compress_type=deflate filemode='-rw-r--r--' file_size=3425 compress_size=1778>



```python
info.date_time#年月日小时分钟秒
```




    (2016, 1, 5, 13, 27, 8)




```python
# 检查zip中每个文件的CRC,有错误会返回对应文件作为列表成员
with zipfile.ZipFile('output.zip', 'r',zipfile.ZIP_DEFLATED) as f:
    print(f.testzip())
```

    None



```python
#给文件加密码
with zipfile.ZipFile('output.zip', 'r',zipfile.ZIP_DEFLATED) as f:
    f.setpassword(" ".encode())
```


```python
#带密码打开
with zipfile.ZipFile('output.zip', 'r',zipfile.ZIP_DEFLATED) as f:
    print(f.read('input副本.txt'," ".encode()).decode("utf-8"))
```

    强大的交互执行框架--Jupyter及其支持的几种优秀语言介绍
    
    Jupyter 是ipython notebook 脱离ipython项目后的一个独立项目.不同于notebook, Jupyter已经不再只是python的交互执行框架,
    而是致力于多语言通用的交互执行.
    
    在以前 notebook作为ipython的一个子项目就受到许多人的喜爱和追捧,当时就已经可以通过多种途径利用它执行其他非python语言.
    现在Jupyter 与ipython分家后,这一特性得到了更好的支持.
    
    现在的Jupyter只负责交互执行,而执行的是什么语言其实是由其执行核心--kernel 来实现的,而现在的ipython可以自带其执行python版本的python核心.
    
    于是顺带的,本文也介绍几种支持Jupyter的优秀的语言.
    
    ## Jupyter支持的语言:
    
    在[这里](https://github.com/ipython/ipython/wiki/IPython-kernels-for-other-languages)你可以看到目前支持的语言.
    
    
    ## Jupyter的安装:
    
    Jupyter 现在是独立安装.当然,你依然需要装有python 和 pip.
    
    
        $pip install jupyter
    
    如果你用brew 安装的python3,那么自然的
    
        $pip3 install jupyter
    
    ## 运行
    
        $jupyter notebook
    
    
        当然了,没有kernel是没法运行的
    
    
    ## 几个比较值得安装的的kernel安装:
    
    本文中介绍的的kernel只在mac下测试安装成功,在linux下应当都能成功,但windows下未必.
    欢迎朋友们写下其他平台的经验,我看到也会进行修改,谢谢
    
    ### 通用依赖
    几乎所有kernel都需要`zeromq`和`openssl`这两个库,他们都可以用brew安装
    
    brew install zeromq
    brew install openssl
    
    > python2与python3并存
    
    ### 安装依赖
    
    python的kernel自然依赖于python.
    
    对于新手来说python2和python3并存本身就是件比较纠结蛋碎的事儿,mac下一般会用homebrew安装两个版本
    (当然也会有人安装其他比如pypy之类,那个咱不管)
    
        $brew install python
        $brew install python3
    
    
    如果是这样安装,那python python2 python3对应的便是不同版本的python如下表(可能版本不同有些许不同)
    
    命令|python来源|pip命令|库位置
    ---|---|---|---
    python|brew 安装的 python|pip|/usr/local/lib/python2.7/site-packages
    python2|brew 安装的 python|pip|/usr/local/lib/python2.7/site-packages
    python3|brew 安装的 python3|pip3|/usr/local/lib/python3.4/site-packages
    
    
    ### 安装kernel
    
    **分别安装ipython,在各自环境下执行**
    
        $pip install ipython[all]
        $ipython kernelspec install-self
        $pip3 install ipython[all]
        $ipython kernelspec install-self
    
    ### 测试下
    
    打开Jupyter:
    
        jupyter notebook
    
    可以在*new*看到里面出现*Python 2*和*Python 3*两个可选项
    
    >Bash
    
    Bash 不用多介绍,最通用的shell命令语言,同时它的kernel也是安装起来最简单的kernel了.
    
    ### 安装Bash-kernel
    
    安装Bash-kernel只要用pip工具即可
    
        pip install bash_kernel
        python -m bash_kernel.install
    
    ### 测试下
    
    新建一个bash用的notebook
    在其中的一个cell中输入
    
        for i in {1..5}
        do  
            echo $i  
        done  
    
    
    看看是不是输出了1到5这5个数
    
    更多的bash语言细节可以[点击这里查看](http://www.yiibai.com/shell/)
    
    >Golang
    
    Go语言是谷歌几年前推出的一门编译型语言,它以简洁优雅高,高开发效率,高可维护性和善于处理高并发而著称
    Go有一套完善的开发流程和语言规范,而在Jupyter下执行Go主要是用于学习其语言特性



```python
#查看信息
with zipfile.ZipFile('output.zip', 'r',zipfile.ZIP_DEFLATED) as f:
    f.printdir()
```

    File Name                                             Modified             Size
    input副本.txt                                    2016-01-05 13:27:08         3425


## 补充:

zip文件格式信息科普:

一个 ZIP 文件由三个部分组成：压缩源文件数据区+压缩源文件目录区+压缩源文件目录结束标志 

> 压缩源文件数据区 

在这个数据区中每一个压缩的源文件/目录都是一条记录，记录的格式如下： [文件头+ 文件数据 + 数据描述符]
    
+ 文件头结构 

组成| 长度 
---|---
文件头标记| 4 bytes (0x04034b50) 
解压文件所需 pkware 版本 |2 bytes 
全局方式位标记 |2 bytes 
压缩方式 |2 bytes 
最后修改文件时间 |2 bytes 
最后修改文件日期 |2 bytes 
CRC-32校验 |4 bytes 
压缩后尺寸 |4 bytes 
未压缩尺寸 |4 bytes 
文件名长度 |2 bytes 
扩展记录长度 |2 bytes 
文件名 |（不定长度） 
扩展字段 |（不定长度）
       
+ 文件数据 
    
+ 数据描述符 
    
组成 |长度 
---|---
CRC-32校验 |4 bytes 
压缩后尺寸 |4 bytes 
未压缩尺寸 |4 bytes 

这个数据描述符只在全局方式位标记的第３位设为１时才存在，紧接在压缩数据的最后一个字节后。这个数据描述符只用在不能对输出的 ZIP 文件进行检索时使用。例如：在一个不能检索的驱动器（如：磁带机上）上的 ZIP 文件中。如果是磁盘上的ZIP文件一般没有这个数据描述符。 


> 压缩源文件目录区 

在这个数据区中每一条纪录对应在压缩源文件数据区中的一条数据 

 组成 |长度 
 ---|---
目录中文件文件头标记| 4 bytes (0x02014b50) 
压缩使用的pkware 版本| 2 bytes 
解压文件所需 pkware 版本| 2 bytes 
全局方式位标记 |2 bytes 
压缩方式| 2 bytes 
最后修改文件时间| 2 bytes 
最后修改文件日期 |2 bytes 
ＣＲＣ－３２校验 |4 bytes 
压缩后尺寸| 4 bytes 
未压缩尺寸| 4 bytes 
文件名长度 |2 bytes 
扩展字段长度| 2 bytes 
文件注释长度 |2 bytes 
磁盘开始号 |2 bytes 
内部文件属性 |2 bytes 
外部文件属性 |4 bytes 
局部头部偏移量 |4 bytes 
文件名 |（不定长度） 
扩展字段 |（不定长度） 
文件注释 |（不定长度） 


> 压缩源文件目录结束标志 

组成 |长度 
---|---
目录结束标记 |4 bytes (0x02014b50) 
当前磁盘编号 |2 bytes 
目录区开始磁盘编号| 2 bytes 
本磁盘上纪录总数 |2 bytes 
目录区中纪录总数| 2 bytes 
目录区尺寸大小 |4 bytes 
目录区对第一张磁盘的偏移量| 4 bytes 
ZIP 文件注释长度 |2 bytes 
ZIP 文件注释 |（不定长度）
