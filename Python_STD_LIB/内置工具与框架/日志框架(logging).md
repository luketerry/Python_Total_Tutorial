
# 日志框架(logging)

日志是程序必备的功能之一,如果一个程序天衣无缝,那确实没啥必要有日志了,但如果有可能有错误,我们就该用日志收集可能的错误,这样也可以更好的debug.另外在服务器端收集信息也可以用日志,分析日志是所有搞计算机的人的必修课...

在logging框架下首先我们需要初始化一个logger来处理log,之后通过添加handler,Formatter和config子属性来自定义我们的logger.

> 一个简单的例子


```python
import logging
import sys
#日志的名字,会在每行的一开始写
logger = logging.getLogger("endlesscode")
#格式化
formatter = logging.Formatter('%(name)-12s %(asctime)s %(levelname)-8s %(message)s', '%a, %d %b %Y %H:%M:%S',)
#设定输出文件
file_handler = logging.FileHandler("test.log")
#为handler设置输出格式
file_handler.setFormatter(formatter)
#流控制
stream_handler = logging.StreamHandler(sys.stderr)
#为logger设置handler
logger.addHandler(file_handler)
#发送信息到流
logger.addHandler(stream_handler)
#设置报错等级
#logger.setLevel(logging.ERROR)
#报错
logger.error("w")
#移除handler
logger.removeHandler(stream_handler)
#报错
logger.error("f")
```

    w
    ERROR:endlesscode:w
    ERROR:endlesscode:f


+ level: 设置日志级别，默认为logging.WARNING

+ stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略

## 输出文本的格式化

元素|格式化字符串|描述
---|---|---
args|不用格式化|	参数会是一个元组
asctime	|%(asctime)s	|可读的时间
created	|%(created)f|	记录的创建时间
filename	|%(filename)s	|文件名
funcName	|%(funcName)s	|函数名
levelname	|%(levelname)s	|错误,警报等的名字
levelno	|%(levelno)s|错误,警报等,是预警等级
lineno	|%(lineno)d	|报错行数
module	|%(module)s	|报错模块
msecs	|%(msecs)d	|毫秒级的出错时间
message|%(message)s	|错误信息
name	|%(name)s	|log的名字
pathname	|%(pathname)s	|报错文件所在path
process	|%(process)d	|进程id
processName	|%(processName)s	|进程名
relativeCreated	|%(relativeCreated)d	|微秒级的报错时间
thread	|%(thread)d	|线程id
threadName	|%(threadName)s|线程名

## 日志回滚


```python
from logging.handlers import RotatingFileHandler
```


```python
#定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M
Rthandler = RotatingFileHandler('myapp.log', maxBytes=10*1024*1024,backupCount=5)
Rthandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
Rthandler.setFormatter(formatter)
logging.getLogger('').addHandler(Rthandler)
```

## 几种handler
handler|说明
---|---
StreamHandler(stream=None) | 流输出
FileHandler(filename, mode='a', encoding=None, delay=False)| 写入文件
WatchedFileHandler(filename[, mode[, encoding[, delay]]])|监控log文件
RotatingFileHandler(filename, mode='a', maxBytes=0, backupCount=0, encoding=None, delay=0)|轮替日志,根据日志文件的大小来循环
 TimedRotatingFileHandler(filename, when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False, atTime=None)|轮替日志,根据时间来循环,interval参数可选的值有:["S"-Seconds;'M'-Minutes;'H'-Hours;'D'-Days;'W0'~'W6'-Weekday (0=Monday);'midnight'-半夜循环]
 SocketHandler(host, port)|把log送到网上的socket
 DatagramHandler(host, port)|把log送到网上的UDP sockets
 SysLogHandler(address=('localhost', SYSLOG_UDP_PORT), facility=LOG_USER, socktype=socket.SOCK_DGRAM)|log送到unix系统log
  SMTPHandler(mailhost, fromaddr, toaddrs, subject, credentials=None, secure=None, timeout=1.0)|log送到电子邮箱
  MemoryHandler(capacity, flushLevel=ERROR, target=None)|log存入内存
HTTPHandler(host, url, method='GET', secure=False, credentials=None, context=None)|log通过http网络送到服务器

## config
当然可以在程序中设置log了,但为了改起来方便也可以写在别的文件中然后用`config.fileConfig(path)`来设置,我们看看配置文件大约是啥样

    [loggers]
    keys=root,simpleExample

    [handlers]
    keys=consoleHandler

    [formatters]
    keys=simpleFormatter

    [logger_root]
    level=DEBUG
    handlers=consoleHandler

    [logger_simpleExample]
    level=DEBUG
    handlers=consoleHandler
    qualname=simpleExample
    propagate=0

    [handler_consoleHandler]
    class=StreamHandler
    level=DEBUG
    formatter=simpleFormatter
    args=(sys.stdout,)

    [formatter_simpleFormatter]
    format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
    datefmt=%a, %d %b %Y %H:%M:%S

要注意的是如果用这种方式那么,使用 rotation file handler 时，不要同时声明 file handler，否则 rotation 发生时，doRollover 函数的 os.rename 会报错(「另一个程序正在使用此文件，进程无法访问).当然,可以写另一个py文件专门用来初始化,要用的时候`import`进来就好了.
