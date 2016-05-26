
工厂方法是用来实现对一个抽象概念的

优点在于:

抽象了产品工厂这个类，让它变成了一个接口，只要某个类实现了这个接口，它就可以被当做工厂类来用，这样每添加一个产品的时候，就添加一下相应的生产工厂类，其它地方就可以使用了，满足“开放-封闭”原则


缺点在于:

把生产产品的逻辑判断从工厂中剥离了出去。


工厂方法简单说就是把对象和通过模式匹配的方式创建出来


> 例子:一个翻译软件

我们的翻译软件要能够通过告知翻译成啥语言而选择使用啥类




```python
class GreekGetter(object):

    """A simple localizer a la gettext"""

    def __init__(self):
        self.trans = dict(dog="σκύλος", cat="γάτα")

    def get(self, msgid):
        """We'll punt if we don't have a translation"""
        return self.trans.get(msgid, str(msgid))

class ChineseGetter(object):
    """A simple localizer """

    def __init__(self):
        self.trans = dict(dog="狗", cat="猫")

    def get(self, msgid):
        """We'll punt if we don't have a translation"""
        return self.trans.get(msgid, str(msgid))
    
    
    
class EnglishGetter(object):

    """Simply echoes the msg ids"""

    def get(self, msgid):
        return str(msgid)


def get_localizer(language):
    """The factory method"""
    languages = {"English":EnglishGetter,
                 "Greek":GreekGetter,
                 "Chinese":ChineseGetter
                }
    return languages.get(language,EnglishGetter)()

# Create our localizers
c, g ,j = get_localizer(language="Chinese"), get_localizer(language="Greek"),get_localizer(language="Japanese")
# Localize some text
for msgid in "dog parrot cat bear".split():
    print(c.get(msgid), g.get(msgid),j.get(msgid))
```

    狗 σκύλος dog
    parrot parrot parrot
    猫 γάτα cat
    bear bear bear


这个例子可以看到python实现工厂方法其实非常简单,只要左右子类有共同的接口,然后使用字典代替其他语言中的switch语句实现分支匹配判断即可
