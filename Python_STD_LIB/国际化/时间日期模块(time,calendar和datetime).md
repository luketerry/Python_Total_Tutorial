
# 时间日期模块(time,calendar和datetime)


python3和时间有关的模块常用的主要有3个

+ 基本时间模块`time`
+ 日历模块`calendar`
+ 时间日历模块`datetime`


## 基本时间模块time

time 模块中一般有三种表示时间的方式:

+ 第一种是时间戳(timestamp)的方式(相对于1970.1.1 00:00:00以秒计算的偏移量),时间戳是惟一的,也是各种语言通用的.有的语言如java,js时间以ms记,所以处理的时候注意下,适当的时候`/1000`

+ 第二种以数组的形式表示即(struct_time,结构化时间),共有九个元素，分别表示，同一个时间戳的struct_time会因为时区不同而不同
    
    
    
元素属性|范围及说明
---|---
year| (four digits, e.g. 1998)
month| (1-12)
day |(1-31)
hours| (0-23)
minutes| (0-59)
seconds| (0-59)
weekday| (0-6, Monday is 0)
Julian day |(一年中的第几天, 1-366)
DST |(-1, 0 or 1) 是否是夏令时,</br>0说明是不是,1说明是,-1说明不确定
    
+ 第三种是字符串表述,也就我们可以直接看懂的形式

可以用如下的符号格式化字符串输出:

符号|意思及取值范围
---|---
%y |两位数的年份表示（00-99）
%Y |四位数的年份表示（000-9999）
%m |月份（01-12）
%d |月内中的一天（0-31）
%H |24小时制小时数（0-23）
%I |12小时制小时数（01-12） 
%M |分钟数（00=59）
%S |秒（00-59）
%a |本地简化星期名称
%A |本地完整星期名称
%b |本地简化的月份名称
%B |本地完整的月份名称
%c |本地相应的日期表示和时间表示
%j |年内的一天（001-366）
%p |本地A.M.或P.M.的等价符
%U |一年中的星期数（00-53）星期天为星期的开始
%w |星期（0-6），星期天为星期的开始
%W |一年中的星期数（00-53）星期一为星期的开始
%x |本地相应的日期表示
%X |本地相应的时间表示
%Z |当前时区的名称
%% |%号本身 
    



```python
import time
```

### 时间获取
>获取当前时间戳 time()


```python
now_timestamp = time.time()
now_timestamp
```




    1452007708.870304



> 获取当前结构化时间 localtime()


```python
now_struct = time.localtime()
now_struct
```




    time.struct_time(tm_year=2016, tm_mon=1, tm_mday=5, tm_hour=23, tm_min=28, tm_sec=29, tm_wday=1, tm_yday=5, tm_isdst=0)



> 直接获取当前时间字符串 asctime() 


```python
time.asctime()
```




    'Tue Jan  5 23:28:30 2016'



### 时间表现形式转化

> 时间戳=>结构化时间 localtime()  gmtime()


```python
# 当前时区
time.localtime(now_timestamp)
```




    time.struct_time(tm_year=2016, tm_mon=1, tm_mday=5, tm_hour=23, tm_min=28, tm_sec=28, tm_wday=1, tm_yday=5, tm_isdst=0)




```python
# UTC时区(0时区)
time.gmtime(now_timestamp)
```




    time.struct_time(tm_year=2016, tm_mon=1, tm_mday=5, tm_hour=15, tm_min=28, tm_sec=28, tm_wday=1, tm_yday=5, tm_isdst=0)



> 结构化时间=>时间戳 mktime()


```python
time.mktime(now_struct)
```




    1452007709.0



>结构化时间=>字符串 asctime() strftime()


```python
time.asctime(now_struct)
```




    'Tue Jan  5 23:28:29 2016'




```python
time.strftime("%Y-%m-%d %H:%M:%S", now_struct) 
```




    '2016-01-05 23:28:29'



>时间戳=>字符串 ctime()


```python
time.ctime(now_timestamp)
```




    'Tue Jan  5 23:28:28 2016'



> 将格式化字符串转化为时间戳


```python
a = "Sat Sep 24 22:22:22 2015"
b = time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
b
```




    1443104542.0



> 将格式化字符串转化为结构化时间


```python
c = time.strptime(a,"%a %b %d %H:%M:%S %Y")
c
```




    time.struct_time(tm_year=2015, tm_mon=9, tm_mday=24, tm_hour=22, tm_min=22, tm_sec=22, tm_wday=5, tm_yday=267, tm_isdst=-1)



### 特殊函数

> 线程推迟指点时间 sleep(sec)


```python
time.sleep(1)
```

## 基本的日历模块calendar

calendar模块，即日历模块，提供了对日期的一些操作方法，和生成日历的方法。

主要提供的常量(用list查看):

常量|说明
---|---
calendar.day_name|一周的星期几名字
calendar.day_abbr|一周的星期几名字的简写
calendar.month_name|月份名字
calendar.month_abbr|月份名字的简写

主要的方法有:

方法|说明
---|---
calendar.setfirstweekday(weekday)|设置日历中星期的的第一天是周几
calendar.firstweekday()|查看日历中一星期的第一天是周几(在列表中的位置)
calendar.isleap(year)  |判断是否是闰年
calendar.leapdays(y1, y2)   |获取两个年份之间闰年数 
calendar.weekday(year, month, day)|查看某一天是星期几(在列表中的位置)
calendar.weekheader(n)|返回星期几的英文缩写,n表示用几位字母
calendar.monthrange(year, month)|返回第一天是周几(列表中位置和月的长度)
calendar.monthcalendar(year, month)|返回一个表示日历的二维数组
calendar.prmonth(theyear, themonth, w=0, l=0)|直接打印日历
calendar.month(theyear, themonth, w=0, l=0)|返回某月的日历文本
calendar.prcal(year, w=0, l=0, c=6, m=3)|打印一年的日历
calendar.calendar(year, w=2, l=1, c=6, m=3)|返回一年日历的字符串
calendar.timegm(tuple)|把一个 UTC 的 struct_time 转化为 POSIX 时间戳

其中有三个主要的类型可以实例化:

+ calendar.Calendar(firstweekday=0) 
    
    该类提供了许多生成器，如星期的生成器，某月日历生成器
主要有:

方法|说明
---|---
iterweekdays()|返回一周几天的生成器
itermonthdates(year, month)|返回某月的每一天的datetime构成的生成器
itermonthdays2(year, month)|返回某月的每一天的(日期,星期)构成的生成器
itermonthdays(year, month)|返回某月的每一天的日期构成的生成器
monthdatescalendar(year, month)|返回某月的每一天的datetime构成的list(每周是一个list)
monthdays2calendar(year, month)|返回某月的每一天的(日期,星期)构成的list(每周是一个list)
monthdayscalendar(year, month)|返回某月的每一天的日期构成的list(每周是一个list)
yeardatescalendar(year, width=3)|返回某年的每一天的datetime构成的list(每月一个list,每周是一个list)
yeardays2calendar(year, width=3)|返回某年的每一天的(日期,星期)构成的list(每月一个list,每周是一个list)
yeardayscalendar(year, width=3)|返回某年的每一天的日期构成的list(每月一个list,每周是一个list)

+ calendar.TextCalendar(firstweekday=0) 

    该类提供了按月、按年生成日历字符串的方法。
主要有:

方法|说明
---|---
formatmonth(theyear, themonth, w=0, l=0)|返回某月的日历字符串
prmonth(theyear, themonth, w=0, l=0)|打印某月的日历字符串
formatyear(theyear, w=2, l=1, c=6, m=3)|返回某年的日历字符串
pryear(theyear, w=2, l=1, c=6, m=3)|打印某年的日历字符串

子类有:

`calendar.LocaleTextCalendar(firstweekday=0, locale=None)`

用来生成本地日历,主要就是月份和星期的本地语言化,locale默认是计算机的locale

+ calendar.HTMLCalendar(firstweekday=0) 

    类似TextCalendar，不过生成的是HTML格式日历
主要有:

方法|说明
---|---
formatmonth(theyear, themonth, withyear=True)|返回某月的日历的html字符串
formatyear(theyear, width=3)|返回某年的日历的html字符串
formatyearpage(theyear, width=3, css='calendar.css', encoding=None)|返回完整的页面代码的字符串

子类有:

`calendar.LocaleHTMLCalendar(firstweekday=0, locale=None)`

用来生成本地日历,主要就是月份和星期的本地语言化,locale默认是计算机的locale


```python
import calendar
```


```python
cal = calendar.HTMLCalendar(calendar.MONDAY)
```


```python
with open('calendar.html',"wb") as f:
    f.write(cal.formatyearpage(2016))
```

## 最常用的时间日历模块 datetime

datetime同样是python标准库,不过它看起来就很OO很现代了~它用一个叫datetime的类型来表示时间,一般来说,做时间的计算会用它而不是time模块


```python
from datetime import datetime
```

>获取datetime 时间

>>获取当前日期和时间 datetime.now()


```python
now = datetime.now()
now
```




    datetime.datetime(2016, 1, 5, 23, 28, 36, 203192)




```python
now.__str__()
```




    '2016-01-05 23:28:36.203192'



>>获取某一时间datetime()


```python
yesterday = datetime(2015,9,23,17,2,4,220475)
yesterday
```




    datetime.datetime(2015, 9, 23, 17, 2, 4, 220475)



> datetime => 时间戳 .timestamp()


```python
now.timestamp()
```




    1452007716.203192



>时间戳 => datetime
>> 本地时间


```python
before_now = datetime.fromtimestamp(now_timestamp)
before_now.__str__()
```




    '2016-01-05 23:28:28.870304'



>> UTC标准时间


```python
before_now_UTC = datetime.utcfromtimestamp(now_timestamp)
before_now_UTC.__str__()
```




    '2016-01-05 15:28:28.870304'



> 格式化字符串 => datetime


```python
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
cday
```




    datetime.datetime(2015, 6, 1, 18, 19, 59)



> datetime => 格式化字符串


```python
now.strftime('%a, %b %d %H:%M')
```




    'Tue, Jan 05 23:28'



> 时区转换

步骤:

1. 确定当前时区
2. 确定目标时区


```python
from datetime import timedelta, timezone,datetime
```


```python
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now_utc = datetime.utcnow().replace(tzinfo=timezone.utc)
print(now_utc)

```

    2016-01-25 15:57:31.702187+00:00



```python
bj_dt = now_utc.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
```

    2016-01-25 23:57:31.702187+08:00



```python
tokyo_dt = now_utc.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
```

    2016-01-06 00:28:40.505821+09:00



```python
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)
```

    2016-01-06 00:28:40.505821+09:00


> 时间计算


```python
from datetime import datetime, timedelta
now = datetime.now()
print(now)

print(now + timedelta(hours=10))

print(now - timedelta(days=1))

print(now + timedelta(days=2, hours=12))

```

    2016-01-05 23:28:41.477190
    2016-01-06 09:28:41.477190
    2016-01-04 23:28:41.477190
    2016-01-08 11:28:41.477190



```python
tenten = datetime(2015, 10, 1, 0, 0, 0, 0)
```


```python
(tenten - now).__str__()
```




    '-97 days, 0:31:18.522810'




```python
from datetime import datetime, timedelta
```


```python
now = datetime.now()
```


```python
now
```




    datetime.datetime(2016, 2, 17, 13, 23, 41, 608079)




```python
now + timedelta(seconds=10)
```




    datetime.datetime(2016, 2, 17, 13, 23, 51, 608079)




```python
nowonow = datetime.now() 
```


```python
nowonow
```




    datetime.datetime(2016, 2, 17, 13, 24, 50, 434489)




```python
nowonow<now
```




    False




```python

```
