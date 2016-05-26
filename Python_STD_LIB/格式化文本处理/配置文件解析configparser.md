
# 配置文件解析(configparser)
configparser 是用来读取配置文件的包,在python2.7中叫`ConfugParser`。配置文件的格式如下：中括号“[ ]”内包含的为section。section 下面为类似于key-value 的配置内容。配置文件一般以`config`,`conf`或者`ini`作为扩展名.
大约是这个样子


```python
%%writefile server.conf
    [db]
      db_host = 127.0.0.1
      db_port = 22
      db_user = root
      db_pass = rootroot

    [concurrent]
      thread = 10
      processor = 20
```

    Writing server.conf



```python
try:
    import configparser
except ImportError:
    import ConfigParser as configparser
config = configparser.ConfigParser()
```

> 读取配置文件


```python
config.read("server.conf") 
```




    ['server.conf']



> 解析配置文件


```python
config.sections()# 获取sections的列表
```




    ['db', 'concurrent']




```python
config.options("db") #获取对应section的options的键
```




    ['db_host', 'db_port', 'db_user', 'db_pass']




```python
config.items("db") #获取对应section的options的键值对
```




    [('db_host', '127.0.0.1'),
     ('db_port', '22'),
     ('db_user', 'root'),
     ('db_pass', 'rootroot')]




```python
config.get("db", 'db_host') #获取对应section的options的值
```




    '127.0.0.1'



> 写配置文件


```python
config.set("db", 'db_host', "192.168.3.150") 
#set a new value 
config.set("db", "db_dbname", "mydb") 
#create a new section 
config.add_section('jupyter_notebook') 
config.set('jupyter_notebook', 'host', '192.168.3.150')
```


```python
with open("server_new.conf", "w") as f:
    config.write(f)
```


```python
!cat server_new.conf
```

    [db]
    db_host = 192.168.3.150
    db_port = 22
    db_user = root
    db_pass = rootroot
    db_dbname = mydb
    
    [concurrent]
    thread = 10
    processor = 20
    
    [jupyter_notebook]
    host = 192.168.3.150
    

