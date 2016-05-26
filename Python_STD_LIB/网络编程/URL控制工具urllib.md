
# URL控制工具(urllib)

urllib提供了一系列用于操作URL的功能。注意,在python2中这些功能分别在urllib,urllib2,urlparse中实现


```python
import urllib
```

urllib由4个模块组成:

模块|说明
---|---
error|urllib可能发生的错误
parse|url地址句法分析
request|http请求模块
robotparser|robot.txt网站设置文件解析(请看格式化文件处理中的介绍)

## 地址句法分析 urllib.parse(urlparse)

urllib.parse可以将url地址分解为元件,再重新组合


```python
from urllib.parse import urlparse,urlsplit,urljoin
```


```python
url1="https://www.google.com.hk/?gws_rd=ssl#safe=strict&q=python"
```


```python
url2="http://www.cwi.nl:80/%7Eguido/Python.html"
```


```python
o1 = urlparse(url1)
o1
```




    ParseResult(scheme='https', netloc='www.google.com.hk', path='/', params='', query='gws_rd=ssl', fragment='safe=strict&q=python')




```python
o2 = urlparse(url2)
o2
```




    ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html', params='', query='', fragment='')




```python
o2.port
```




    80




```python
o1.geturl()
```




    'https://www.google.com.hk/?gws_rd=ssl#safe=strict&q=python'




```python
s1=urlsplit(url1)
s1
```




    SplitResult(scheme='https', netloc='www.google.com.hk', path='/', query='gws_rd=ssl', fragment='safe=strict&q=python')




```python
urljoin('http://www.cwi.nl/%7Eguido/Python.html', 'FAQ.html')
```




    'http://www.cwi.nl/%7Eguido/FAQ.html'



## http请求urllib.request(urllib2)

这个貌似是最常用的模块了,写爬虫,做网站测试啥的都用它


```python
from urllib.request import Request,urlopen,ProxyHandler
```

### 最简单的打开一个网页

    urlopen(url,timeout=XXX)



```python
with urlopen('http://www.python.org/',timeout=10) as f:
    print(f.read().decode("utf-8")[:300])
```

    <!doctype html>
    <!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->
    <!--[if IE 7]>      <html class="no-js ie7 lt-ie8 lt-ie9">          <![endif]-->
    <!--[if IE 8]>      <html class="no-js ie8 lt-ie9">                 <![endif]-->
    <!--[if gt IE 8]><!--><html class="no-js"


### 使用Request

使用Request可以为每个请求添加一些数据,头文件等

Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)

+ date:发送的数据(put,post)
+ headers: 头
+ method:方法
+


```python
req = Request('http://python.org/')
with urlopen(req) as f:
    print(f.read().decode("utf-8")[:300])
```

    <!doctype html>
    <!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->
    <!--[if IE 7]>      <html class="no-js ie7 lt-ie8 lt-ie9">          <![endif]-->
    <!--[if IE 8]>      <html class="no-js ie8 lt-ie9">                 <![endif]-->
    <!--[if gt IE 8]><!--><html class="no-js"


#### 设定头文件

对有些 header 要特别留意，Server 端会针对这些 header 做检查

User-Agent 有些 Server 或 Proxy 会检查该值，用来判断是否是浏览器发起的 Request
Content-Type 在使用 REST 接口时，Server 会检查该值，用来确定 HTTP Body 中的内容该怎样解析。
 

常见的取值有：

+ application/xml ：在 XML RPC，如 RESTful/SOAP 调用时使用
+ application/json ：在 JSON RPC 调用时使用
+ application/x-www-form-urlencoded ：浏览器提交 Web 表单时使用

  ……
 

在使用 RPC 调用 Server 提供的 RESTful 或 SOAP 服务时， Content-Type 设置错误会导致 Server 拒绝服务。


```python
#方法1.直接定义头文件
url = 'http://python.org/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
headers = { 'User-Agent' : user_agent,
           'Accept':'text/html;q=0.9,*/*;q=0.8',
   'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
  'Accept-Encoding':'gzip',
       'Connection':'close'
}
req = urllib.request.Request(url, headers=headers)
with urlopen(req,timeout=10) as f:
    print(f.read().decode("utf-8")[:300])

```

    <!doctype html>
    <!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->
    <!--[if IE 7]>      <html class="no-js ie7 lt-ie8 lt-ie9">          <![endif]-->
    <!--[if IE 8]>      <html class="no-js ie8 lt-ie9">                 <![endif]-->
    <!--[if gt IE 8]><!--><html class="no-js"



```python
#方法2:用build_opener定义,这样便于扩展
url = 'http://python.org/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
headers = { 'User-Agent' : user_agent,
           'Accept':'text/html;q=0.9,*/*;q=0.8',
   'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
  'Accept-Encoding':'gzip',
       'Connection':'close'
}
opener = urllib.request.build_opener()
opener.addheaders = [(k,v) for k,v in headers.items()]
with opener.open(req,timeout=10) as f:
    print(f.read().decode("utf-8")[:300])
```

    <!doctype html>
    <!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->
    <!--[if IE 7]>      <html class="no-js ie7 lt-ie8 lt-ie9">          <![endif]-->
    <!--[if IE 8]>      <html class="no-js ie8 lt-ie9">                 <![endif]-->
    <!--[if gt IE 8]><!--><html class="no-js"


### 设定代理ProxyHandler

    proxy_support = ProxyHandler({'sock5': 'localhost:1080'})
