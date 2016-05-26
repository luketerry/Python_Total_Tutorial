
# 国际化翻译(gettext)

我们写app希望可以适应本地化需求,也就是当换一种语言的时候可以自动转成翻译好的对应文本.我们当然可以每个语言些一个版本,代码相同只是修改其中的文本.

一个简单的解决方案是使用一个函数包裹字符串,让函数负责找到对应翻译.比如



```python
%%writefile international.py
#coding:utf-8
spanishStrings = {'Hello world!': 'Hola Mundo!'}
frenchStrings = {'Hello world!': 'Bonjour le monde!'}
germanStrings = {'Hello world!': 'Hallo Welt!'}
  
```

    Overwriting international.py



```python
from international import *
def trans(s):
    if LANGUAGE == 'English':
        return s
    if LANGUAGE == 'Spanish':
        return spanishStrings.get(s)
    if LANGUAGE == 'French':
        return frenchStrings.get(s)
    if LANGUAGE == 'German':
        return germanStrings.get(s)
```


```python
LANGUAGE = 'French'
print(trans("Hello world!"))
```

    Bonjour le monde!


但是很明显,一旦文本量变大了就会无法管理了~

Python提供了gettext模块用于解决这类问题


## gettext的使用

> 创建国际化文档的文件夹目录


    ----|
        |-src-|
              |-locale-|
                       |-en-|
                       |    |-LC_MESSAGES
                       |
                       |-cn-|
                       |    |-LC_MESSAGES
                       |
                       |-fr-|
                            |-LC_MESSAGES
        

> gettext初始化

使用脚本工具`pygettext`初始化gettext设置(如果安装的python中没有的话可以来[这里下载](./pygettext.py))


```python
!pygettext.py 
```


```python
!cat messages.pot
```

    # SOME DESCRIPTIVE TITLE.
    # Copyright (C) YEAR ORGANIZATION
    # FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
    #
    msgid ""
    msgstr ""
    "Project-Id-Version: PACKAGE VERSION\n"
    "POT-Creation-Date: 2016-01-06 15:41+CST\n"
    "PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
    "Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
    "Language-Team: LANGUAGE <LL@li.org>\n"
    "MIME-Version: 1.0\n"
    "Content-Type: text/plain; charset=CHARSET\n"
    "Content-Transfer-Encoding: ENCODING\n"
    "Generated-By: pygettext.py 1.5\n"
    
    


我们修改它的

"Content-Type: text/plain; charset=CHARSET\n"
"Content-Transfer-Encoding: ENCODING\n"

两个字段


```python
%%writefile messages.pot
# SOME DESCRIPTIVE TITLE.
# Copyright (C) YEAR ORGANIZATION
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
#
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\n"
"POT-Creation-Date: 2016-01-06 10:05+CST\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language-Team: LANGUAGE <LL@li.org>\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=gb2312\n"
"Content-Transfer-Encoding: utf-8\n"
"Generated-By: pygettext.py 1.5\n"
```

    Overwriting messages.pot


接着我们将它保存为lang.po


```python
!rename.py messages.pot lang.po
```

    done!


> 注册国际化文本


```python
%%writefile transfer.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gettext
langen = gettext.translation('lang', './locale', languages=['en'])
langcn = gettext.translation('lang', './locale', languages=['cn'])
langfr = gettext.translation('lang', './locale', languages=['fr'])

```

    Overwriting transfer.py


其中:

+ `gettext_te.py`是要翻译模块或app名
+ `./locale`是存放翻译文件的路径,
+ `languages`参数指定要使用的语言存放的子目录,这里cn表示使用`./locale/cn/LC_MESSAGES/`路径下的翻译文件.

这样我们就有了一个`_()`方法来翻译文本

> 编辑之前的lang.po


```python
%%writefile lang.po
# SOME DESCRIPTIVE TITLE.
# Copyright (C) YEAR ORGANIZATION
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
#
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\n"
"POT-Creation-Date: 2016-01-06 10:05+CST\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language-Team: LANGUAGE <LL@li.org>\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=utf-8\n"
"Content-Transfer-Encoding: utf-8\n"
"Generated-By: pygettext.py 1.5\n"

msgid "Hello world!"
msgstr "世界你好!"

msgid "Python is a good Language."
msgstr "Python是门好语言."
```

    Overwriting lang.po


> 生成mo文件


```python
!msgfmt.py lang.po
```

之后将生成的mo文件放入`./locale/cn/LC_MESSAGES/`下


```python
!cp lang.mo locale/cn/LC_MESSAGES/lang.mo
```


```python
!rm lang.mo
```


```python
!rm lang.po
```

再编辑另外两个文件


```python
!pygettext.py
```


```python
%%writefile messages.pot
# SOME DESCRIPTIVE TITLE.
# Copyright (C) YEAR ORGANIZATION
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
#
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\n"
"POT-Creation-Date: 2016-01-06 10:05+CST\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language-Team: LANGUAGE <LL@li.org>\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=IBM037\n"
"Content-Transfer-Encoding: utf-8\n"
"Generated-By: pygettext.py 1.5\n"
```

    Overwriting messages.pot



```python
!rename.py messages.pot lang.po
```

    done!



```python
%%writefile lang.po
# SOME DESCRIPTIVE TITLE.
# Copyright (C) YEAR ORGANIZATION
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
#
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\n"
"POT-Creation-Date: 2016-01-06 10:05+CST\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language-Team: LANGUAGE <LL@li.org>\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=IBM037\n"
"Content-Transfer-Encoding: utf-8\n"
"Generated-By: pygettext.py 1.5\n"


```

    Overwriting lang.po



```python
!msgfmt.py lang.po
```


```python
!cp lang.mo locale/en/LC_MESSAGES/lang.mo
```


```python
!rm lang.mo
```


```python
!rm lang.po
```


```python
!pygettext.py
```


```python
%%writefile messages.pot
# SOME DESCRIPTIVE TITLE.
# Copyright (C) YEAR ORGANIZATION
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
#
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\n"
"POT-Creation-Date: 2016-01-06 10:05+CST\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language-Team: LANGUAGE <LL@li.org>\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=IBM01147\n"
"Content-Transfer-Encoding: utf-8\n"
"Generated-By: pygettext.py 1.5\n"
```

    Overwriting messages.pot



```python
!rename.py messages.pot lang.po
```

    done!



```python
%%writefile lang.po
# SOME DESCRIPTIVE TITLE.
# Copyright (C) YEAR ORGANIZATION
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
#
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\n"
"POT-Creation-Date: 2016-01-06 10:05+CST\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language-Team: LANGUAGE <LL@li.org>\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=utf-8\n"
"Content-Transfer-Encoding: utf-8\n"
"Generated-By: pygettext.py 1.5\n"

msgid "Hello world!"
msgstr "Bonjour le Monde!"

msgid "Python is a good language."
msgstr "Python est une bien langue."
```

    Overwriting lang.po



```python
!msgfmt.py lang.po
```


```python
!cp lang.mo locale/fr/LC_MESSAGES/lang.mo
```


```python
!rm lang.mo
```


```python
!rm lang.po
```

> 编辑主模块


```python
%%writefile gettext_te.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from transfer import *
langcn.install()
print(_("Hello world!"))
langen.install()
print(_("Hello world!"))
langfr.install()
print(_("Hello world!"))
```

    Overwriting gettext_te.py



```python
%run gettext_te.py
```

    世界你好!
    Hello world!
    Bonjour le Monde!


这样每次只要修改对应文件夹的`mo`文件就可以实现本地化了,一次受罪终身受用~

## 用format方法处理带变量字符串

当遇到要有变量的字符串时我们当然可以直接分段的翻译,但明显这样不好用不好看,可以利用字符串的format方法优雅的翻译

(请先将kernel重启)


```python
%%writefile lang.po
# SOME DESCRIPTIVE TITLE.
# Copyright (C) YEAR ORGANIZATION
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
#
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\n"
"POT-Creation-Date: 2016-01-06 10:05+CST\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language-Team: LANGUAGE <LL@li.org>\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=utf-8\n"
"Content-Transfer-Encoding: utf-8\n"
"Generated-By: pygettext.py 1.5\n"

msgid "Hello world!"
msgstr "Bonjour le Monde!"

msgid "Python is a good language."
msgstr "Python est une bien langue."

msgid "Hello"
msgstr "Bonjour"

msgid "Hello {name:}!"
msgstr "Bonjour {name:}!"
```

    Writing lang.po



```python
!msgfmt.py lang.po
```


```python
!cp lang.mo locale/fr/LC_MESSAGES/lang.mo
```


```python
!rm lang.po
```


```python
!rm lang.mo
```


```python
%%writefile lang.po
# SOME DESCRIPTIVE TITLE.
# Copyright (C) YEAR ORGANIZATION
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
#
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\n"
"POT-Creation-Date: 2016-01-06 10:05+CST\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language-Team: LANGUAGE <LL@li.org>\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=utf-8\n"
"Content-Transfer-Encoding: utf-8\n"
"Generated-By: pygettext.py 1.5\n"

msgid "Hello world!"
msgstr "世界你好!"

msgid "Python is a good Language."
msgstr "Python是门好语言."

msgid "Hello"
msgstr "你好"

msgid "Hello {name:}!"
msgstr "你好{name:}!"
```

    Writing lang.po



```python
!msgfmt.py lang.po
```


```python
!cp lang.mo locale/cn/LC_MESSAGES/lang.mo
```


```python
!rm lang.po
```


```python
!rm lang.mo
```


```python
%%writefile gettext_te2.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from transfer import *
langcn.install()
print(_("Hello world!"))
print(_("Hello"))
print(_("Hello {name:}!").format(name="Lily"))
langen.install()
print(_("Hello world!"))
print(_("Hello"))
print(_("Hello {name:}!").format(name="Lily"))
langfr.install()
print(_("Hello world!"))
print(_("Hello"))
print(_("Hello {name:}!").format(name="Lily"))
```

    Overwriting gettext_te2.py



```python
%run gettext_te2.py
```

    世界你好!
    你好
    你好Lily!
    Hello world!
    Hello
    Hello Lily!
    Bonjour le Monde!
    Bonjour
    Bonjour Lily!

