
# hmac算法模块(hmac)

和hashlib中的算法不同,hmac算法需要一个key作为seed才可以得到散列点.具体用法如下:



```python
import hmac
```


```python
myhmac = hmac.new(b'key')
```


```python
myhmac.update(u"我得密码".encode("utf-8"))
```


```python
myhmac.hexdigest()
```




    'd63cd3fbde648491d690927a7e13fc58'




```python
len(myhmac.hexdigest())
```




    32




```python
int(myhmac.hexdigest(),16)
```




    284770628453006438846849445760286850136



## 参数
hamc的new方法可以带参数

    hmac.new(key[, msg[, digestmod]])
    
+ key 秘钥
+ msg 需要散列的信息
+ digestmod 摘要算法,默认为md5,可以是任何hashlib中的算法


```python
myhmac2 = hmac.new(b'key',digestmod="sha1")
```


```python
myhmac2.update(u"我得密码".encode("utf-8"))
```


```python
myhmac2.update(u"我得密码压法嘎斯的".encode("utf-8"))
```


```python
myhmac2.hexdigest()
```




    'c3862bbe06828bce94b0ba5d636b5446b85c0f7e'




```python
len(myhmac2.hexdigest())
```




    40




```python
int(myhmac2.hexdigest(),16)
```




    1116245310657849793583615546118457557393233153918



可以看到结果就不同了
