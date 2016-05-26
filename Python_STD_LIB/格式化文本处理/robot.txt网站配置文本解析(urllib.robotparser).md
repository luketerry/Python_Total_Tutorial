
# robot.txt网站配置文本解析(urllib.robotparser)

在python2.7中这个模块叫robotparser.

robotparser为robots.txt文件实现了一个解释器，可以用来读取robots文本的格式和内容，用函数方法检查给定的User-Agent是否可以访问相应的网站资源。如果要编写一个网络蜘蛛，这个模块可以限制一些蜘蛛抓取无用的或者重复的信息，避免蜘蛛掉入动态asp/php网页程序的死循环中。
简单的来说，robots.txt文件是每个网站都应该有的，指引蜘蛛抓取和禁止抓取的一个文本格式的文件，一些合法的蜘蛛或者叫爬虫，都是遵守这个规则的，可以控制他们的访问。

一个`robots.txt`大约是这个样子:

    User-agent: *
    Disallow: /search
    Disallow: /404.html
    Disallow: /tags.php
    Disallow: /tags/
    
    
以上代码会阻止，搜索引擎和其它一些蜘蛛程序抓取网站的某些目录和文件，另外百度有官方文档对于 robots.txt 文件有更为详细的介绍:

[如何禁止搜索引擎收录的方法](http://help.baidu.com/question?prod_en=search&class=%BD%FB%D6%B9%CB%D1%CB%F7%D2%FD%C7%E6%CA%D5%C2%BC%B5%C4%B7%BD%B7%A8)。

他有几个主要的方法:

方法|说明
---|---
set_url(url)| 设定robot.txt文件提及的url
read()|读取robots.txt的URL并做句法分析
parse(lines)|句法分析
can_fetch(useragent, url)|如果用户代理被允许根据包含在解析robots.txt文件的规则来获取URL。返回true
mtime()|返回最后获取文件的时间
modified()|设置robots.txt文件上次读取到当前时间


```python
import  urllib.robotparser 
```


```python
rp  =  urllib.robotparser.RobotFileParser () 
rp.set_url ( "http://www.musi-cal.com/robots.txt" ) 
rp.read () 
```


```python
rp.can_fetch ( "*" ,  "http://www.musi-cal.com/cgi-bin/search?city=San+Francisco" ) 
```




    True




```python
rp.can_fetch ( "*" ,  "http://www.musi-cal.com/" ) 
```




    True


