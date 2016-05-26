
# 文档生成器(pydoc)

pydoc是python自带的文档生成器.一般要了解一个模块我们可以看它的源码,毕竟python代码可读性高嘛,但看文档也是个不错的选择

> pydoc的使用


```python
!python -m pydoc flask
```

    Help on package flask:
    
    NNAAMMEE
        flask
    
    FFIILLEE
        /usr/local/Pytho/Anaconda2/lib/python2.7/site-packages/flask/__init__.py
    
    DDEESSCCRRIIPPTTIIOONN
        flask
        ~~~~~
        
        A microframework based on Werkzeug.  It's extensively documented
        and follows best practice patterns.
        
        :copyright: (c) 2011 by Armin Ronacher.
        :license: BSD, see LICENSE for more details.
    
    PPAACCKKAAGGEE  CCOONNTTEENNTTSS
        _compat
        app
        blueprints
        config
        ctx
        debughelpers
        ext (package)
        exthook
        globals
        helpers
        json
        logging
        module
        sessions
        signals
        templating
        testing
        testsuite (package)
        views
        wrappers
    
    FFUUNNCCTTIIOONNSS
        eessccaappee(...)
            escape(s) -> markup
            
            Convert the characters &, <, >, ', and " in string s to HTML-safe
            sequences.  Use this if you need to display text that might contain
            such characters in HTML.  Marks return value as markup string.
    
    DDAATTAA
        ____vveerrssiioonn____ = '0.10.1'
        aabboorrtt = <werkzeug.exceptions.Aborter object>
        aappppccoonntteexxtt__ppooppppeedd = <flask.signals._FakeSignal object>
        aappppccoonntteexxtt__ppuusshheedd = <flask.signals._FakeSignal object>
        aappppccoonntteexxtt__tteeaarriinngg__ddoowwnn = <flask.signals._FakeSignal object>
        ccuurrrreenntt__aapppp = <LocalProxy unbound>
        gg = <LocalProxy unbound>
        ggoott__rreeqquueesstt__eexxcceeppttiioonn = <flask.signals._FakeSignal object>
        jjssoonn__aavvaaiillaabbllee = True
        mmeessssaaggee__ffllaasshheedd = <flask.signals._FakeSignal object>
        rreeqquueesstt = <LocalProxy unbound>
        rreeqquueesstt__ffiinniisshheedd = <flask.signals._FakeSignal object>
        rreeqquueesstt__ssttaarrtteedd = <flask.signals._FakeSignal object>
        rreeqquueesstt__tteeaarriinngg__ddoowwnn = <flask.signals._FakeSignal object>
        sseessssiioonn = <LocalProxy unbound>
        ssiiggnnaallss__aavvaaiillaabbllee = False
        tteemmppllaattee__rreennddeerreedd = <flask.signals._FakeSignal object>
    
    VVEERRSSIIOONN
        0.10.1
    
    


因为jupyter的输出和在terminal中不同,我们看到的是由很多重复字母的,你可以再你的terminal中运行一次看看效果


```python
!pydoc -h
```

    pydoc - the Python documentation tool
    
    pydoc <name> ...
        Show text documentation on something.  <name> may be the name of a
        Python keyword, topic, function, module, or package, or a dotted
        reference to a class or function within a module or module in a
        package.  If <name> contains a '/', it is used as the path to a
        Python source file to document. If name is 'keywords', 'topics',
        or 'modules', a listing of these things is displayed.
    
    pydoc -k <keyword>
        Search for a keyword in the synopsis lines of all available modules.
    
    pydoc -p <port>
        Start an HTTP server on the given port on the local machine.  Port
        number 0 can be used to get an arbitrary unused port.
    
    pydoc -g
        Pop up a graphical interface for finding and serving documentation.
    
    pydoc -w <name> ...
        Write out the HTML documentation for a module to a file in the current
        directory.  If <name> contains a '/', it is treated as a filename; if
        it names a directory, documentation is written for all the contents.
    


+ -k 查找关键字
+ -p 用localhost打开网页版,后面填端口号
+ -g GUI版
+ -w 生成html文件
