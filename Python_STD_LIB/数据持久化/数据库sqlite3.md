
# 数据库sqlite3

SQLite3 是一个由C写成的超轻量级数据库.python的自带库中包含它,同时还有它的python接口,也就是说无需单独安装,就能使用SQLite3.

## 连接数据库


```python
import sqlite3
```


```python
conn = sqlite3.connect('people.db')
```

## 使用SQL语句

> 操作数据


```python
c = conn.cursor()
# Create table 
c.execute('''CREATE TABLE people              
     (name text, age int)''')
conn.commit()
```


```python
i = conn.cursor()
i.execute('INSERT INTO people (name) VALUES ("Michael")')
i.execute('INSERT INTO people (name,age) VALUES ("Andy",30)')
i.execute('INSERT INTO people (name,age) VALUES ("Justin",19)')
conn.commit()
```

> 浏览数据


```python
s = conn.cursor()
s.execute('SELECT * FROM people')
print(s.fetchall())
```

    [('Michael', None), ('Andy', 30), ('Justin', 19)]

