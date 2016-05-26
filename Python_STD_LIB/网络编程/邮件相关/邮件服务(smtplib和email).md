
# 邮件服务(smtplib和email)

SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。

Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。

>构造一个最简单的纯文本邮件 


```python
from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
```

+ 第一个参数就是邮件正文
+ 第二个参数是MIME的subtype，传入'plain'，最终的MIME就是'text/plain'
+ 最后一定要用utf-8编码保证多语言兼容性

我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。SMTP协议就是简单的文本命令和响应。login()方法用来登录SMTP服务器，sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str。


邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA，而是包含在发给MTA的文本中的，所以，我们必须把From、To和Subject添加到MIMEText中，才是一封完整的邮件：

    # -*- coding: utf-8 -*-

    from email import encoders
    from email.header import Header
    from email.mime.text import MIMEText
    from email.utils import parseaddr, formataddr
    import smtplib

    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr(( \
            Header(name, 'utf-8').encode(), \
            addr.encode('utf-8') if isinstance(addr, unicode) else addr))

    from_addr = raw_input('From: ')
    password = raw_input('Password: ')
    to_addr = raw_input('To: ')
    smtp_server = raw_input('SMTP server: ')

    msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
    msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
    msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
    msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


> 发送HTML邮件

如果我们要发送HTML邮件，而不是普通的纯文本文件怎么办？方法很简单，在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以了：

    msg = MIMEText('<html><body><h1>Hello</h1>' +
        '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
        '</body></html>', 'html', 'utf-8')

> 发送附件

如果Email中要加上附件怎么办？带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，所以，可以构造一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象即可：


```python
#发送附件 ,要添加
from email.MIMEMultipart import MIMEMultipart 
from email.MIMEBase import MIMEBase

# 邮件对象:
msg = MIMEMultipart()
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('/Users/michael/Downloads/test.png', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='test.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)
```

> 发送图片

如果要把一个图片嵌入到邮件正文中怎么做？直接在HTML邮件中链接图片地址行不行？答案是，大部分邮件服务商都会自动屏蔽带有外链的图片，因为不知道这些链接是否指向恶意网站。

要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，然后，在HTML中通过引用


    src="cid:0"就可以把附件作为图片嵌入了。如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。

把上面代码加入MIMEMultipart的MIMEText从plain改为html，然后在适当的位置引用图片

    msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
        '<p><img src="cid:0"></p>' +
        '</body></html>', 'html', 'utf-8'))

> 同时支持HTML和Plain格式

如果我们发送HTML邮件，收件人通过浏览器或者Outlook之类的软件是可以正常浏览邮件内容的，但是，如果收件人使用的设备太古老，查看不了HTML邮件怎么办？

办法是在发送HTML的同时再附加一个纯文本，如果收件人无法查看HTML格式的邮件，就可以自动降级查看纯文本邮件。

利用MIMEMultipart就可以组合一个HTML和Plain，要注意指定subtype是alternative：

    msg = MIMEMultipart('alternative')
    msg['From'] = ...
    msg['To'] = ...
    msg['Subject'] = ...

    msg.attach(MIMEText('hello', 'plain', 'utf-8'))
    msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))


> 加密SMTP

使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件的整个过程可能会被窃听。要更安全地发送邮件，可以加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。

某些邮件服务商，例如Gmail，提供的SMTP服务必须要加密传输。我们来看看如何通过Gmail提供的安全SMTP发送邮件。

必须知道，Gmail的SMTP端口是587，因此，修改代码如下：

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    # 剩下的代码和前面的一模一样:
    server.set_debuglevel(1)
    ...

> 写一个163邮箱的发送方法


```python
%%writefile email_sender.py
#--*--coding:utf-8 --*--
from __future__ import absolute_import,division,print_function,unicode_literals
class EmailServer(object):
    """定义邮箱服务器"""
    def __str__(self):
        return "stmp server ["+self.smtp_server+":"+self.smtp_port+"]"+("with tls" if self.tls == True else "")
    def __repr__(self):
        return self.__str__()
    def __init__(self,smtp_server,smtp_port,tls=False):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.tls = tls
        
    def setclient(self,from_addr, password):
        """设置客户端与邮件服务器间的链接
        """
        from smtplib import SMTP 
        email_client = SMTP(self.smtp_server, self.smtp_port) 
        if self.tls == True:
            email_client.starttls()
        email_client.set_debuglevel(1)
        email_client.login(from_addr, password)
        return email_client
    
class EmailSender(object):
    """邮件发送器,需要用发件邮箱的账号密码来初始化,之后可以调用实例实现发送
    """
    server = EmailServer(None,None,False)
    def __str__(self):
        return "sender {sender} at [{server}:{port}]{tls}".format(sender = self.sender_addr,
                                                                 server = self.server.smtp_server,
                                                                 port = self.server.smtp_port,
                                                                 tls = "with tls" if self.server.tls == True else "")
    def __repr__(self):
        return self.__str__()
    def __init__(self,sender_addr,password):
        self.sender_addr = sender_addr
        self.password = password
        
    def setServer(self,server):
        self.server = server
    def setServerByAttr(self,smtp_server,smtp_port,tls=False):
        self.server = EmailServer(smtp_server,smtp_port,tls)

    #格式化文本
    def _format_addr(self,s):
        from email.header import Header
        from email.utils import parseaddr, formataddr
        name, addr = parseaddr(s)
        import sys
        if sys.version_info <(3,0):
            return formataddr(( Header(name, 'utf-8').encode(),
                               addr.encode('utf-8') if isinstance(addr, unicode) else addr))
        else:
            return formataddr((Header(name, 'utf-8').encode(), addr))
        
    def _add_attachment(self,file_type,extension,name,aid):
        from email import encoders
        try:
            from email.mime.base import MIMEBase 
        except:
            from email.MIMEBase import MIMEBase
        with open(path, 'rb') as f:
            # 设置附件的MIME和文件名，这里是png类型:
            mime = MIMEBase(file_type, extension, filename=name)
            # 加上必要的头信息:
            mime.add_header('Content-Disposition', 'attachment', filename=name)
            mime.add_header('Content-ID', '<{i}>'.format(i=aid))
            mime.add_header('X-Attachment-Id', '{i}'.format(i=aid))
                # 把附件的内容读进来:
            mime.set_payload(f.read())
                # 用Base64编码:
            encoders.encode_base64(mime)
        return mime
    
    def _make_msg(self,to_addr,
                 subject = None,
                 header = {'FROM':None,
                          'TO':None},
                 content = {"plain":None,
                            "html":None},
                 attachments=None):
        from email.header import Header
        from email.mime.text import MIMEText
        try:
            from email.mime.multipart import MIMEMultipart 
        except:
            from email.MIMEMultipart import MIMEMultipart
        import re
        # 创建内容
        msg = MIMEMultipart('alternative') 
        msg['From'] = self._format_addr('{from_addr}'.\
                        format(from_addr=self.sender_addr) if (header.get('FROM') is None) else '{From} {from_addr}'.\
                                 format(From=header.get('FROM'),from_addr=self.sender_addr))
        msg['To'] = self._format_addr('{to_addr}'.\
                               format(to_addr=to_addr) if (header.get('TO') is None) else '{to} {to_addr}'.\
                                 format(to=header.get('TO'),to_addr=to_addr))
        msg['Subject'] = Header(subject, 'utf-8').encode()
            
        #附件    
        if attachments != None:
            import os
            for i in range(len(attachments)): 
                file_type = attachments[i][0]
                path = attachments[i][1]
                _,extension = os.path.splitext(path)
                _,name = os.path.split(path)
                mine = self._add_attachment(file_type,extension,name,str(i))
                msg.attach(mime)
        #正文        
        if content.get("plain"):
            msg.attach(MIMEText(content.get("plain"), 'plain', 'utf-8'))
        if content.get("html"):
            html=content.get("html")
            img_paths = re.findall('<img src="(.*?)">', html)
            if img_paths:
                img_ids = ["img"+str(i) for i in range(len(img_paths))]
                result,number = re.subn('<img src="(.*?)">', """'<img src="%s">'""", html) 
                import os
                for i in range(number): 
                    file_type = "img"
                    path = img_paths[i]
                    _,extension = os.path.splitext(path)
                    _,name = os.path.split(path)
                    mine = self._add_attachment(file_type,extension,name,img_ids[i])
                    msg.attach(mime)

                res=result%tuple(["cid:{i}".format(i=i) for i in range(number)])
            else:
                res=html
            msg.attach(MIMEText(res, 'html', 'utf-8'))
        return msg
    def _send(self,to_addrs,client,msg):
        client.sendmail(self.sender_addr,to_addrs, msg.as_string())
        return True

    def __call__(self,to_addrs,
                 subject = None,
                 header = {'FROM':None,
                          'TO':None},
                 content = {"plain":None,
                            "html":None},
                 attachments=None):
        """
        to_addrs -- 接收邮箱
        subject -- 主题
        header -- 头部,记录用户的昵称等,必须是一个
                            {'FROM':None,
                              'TO':None}
                            形式的字典
        content -- 主体内容,分为一般文本和html两种,必须是一个
                                {"plain":None,
                                "html":None}
                            形式的字典
        attachments -- 附件(类型,本地文件地址)
        """
        #判断是否为空
        if subject is None :
            print('subject is None.')
            return False 
        if (content.get("plain") is None) and (content.get("html") is None): 
            print('content is None.')
            return False 
        for to_addr in to_addrs:
            msg = self._make_msg(to_addr,subject,header,content,attachments)
            client = self.server.setclient(self.sender_addr,self.password)
            self._send(to_addrs,client,msg)
        client.quit()
        return True
    
class Sender_163(EmailSender):
     def __init__(self,sender_addr,password):
        EmailSender.__init__(self,sender_addr,password)
        self.setServerByAttr(smtp_server="smtp.163.com",smtp_port="25",tls=False)
            
class Sender_163_tls(EmailSender): 
    def __init__(self,sender_addr,password):
        EmailSender.__init__(self,sender_addr,password)
        self.setServerByAttr(smtp_server="smtp.163.com",smtp_port="465",tls=True)
        
class Sender_gmail(EmailSender):
    def __init__(self,sender_addr,password):
        EmailSender.__init__(self,sender_addr,password)
        self.setServerByAttr(smtp_server="smtp.googlemail.com",smtp_port="587",tls=True)

class Sender_sinacn_tls(EmailSender): 
    def __init__(self,sender_addr,password):
        EmailSender.__init__(self,sender_addr,password)
        self.setServerByAttr(smtp_server="smtp.sina.cn",smtp_port="465",tls=True)
class Sender_sinacn(EmailSender): 
    def __init__(self,sender_addr,password):
        EmailSender.__init__(self,sender_addr,password)
        self.setServerByAttr(smtp_server="smtp.sina.cn",smtp_port="25",tls=False)
```

    Overwriting email_sender.py



```python
import email_sender
```


```python
sender = email_sender.Sender_163("15851390734@163.com","hsz881224")
```


```python
sender
```




    sender 15851390734@163.com at [smtp.163.com:25]




```python
sender(("469389377@qq.com",),subject = "来自SMTP的问候……",
                 header = {'FROM': "master hsz",
                          'TO':"hsz pythoner"},
                 content = {"html":"""<html><body><h1>Hello</h1>
                            <p>send by <a href="http://www.python.org">Python</a>...</p>
                            </body></html>"""},
                 attachments=None)
```

    send: 'ehlo hszmba.local\r\n'
    reply: b'250-mail\r\n'
    reply: b'250-PIPELINING\r\n'
    reply: b'250-AUTH LOGIN PLAIN\r\n'
    reply: b'250-AUTH=LOGIN PLAIN\r\n'
    reply: b'250-coremail 1Uxr2xKj7kG0xkI17xGrU7I0s8FY2U3Uj8Cz28x1UUUUU7Ic2I0Y2Ur4KCNPUCa0xDrUUUUj\r\n'
    reply: b'250-STARTTLS\r\n'
    reply: b'250 8BITMIME\r\n'
    reply: retcode (250); Msg: b'mail\nPIPELINING\nAUTH LOGIN PLAIN\nAUTH=LOGIN PLAIN\ncoremail 1Uxr2xKj7kG0xkI17xGrU7I0s8FY2U3Uj8Cz28x1UUUUU7Ic2I0Y2Ur4KCNPUCa0xDrUUUUj\nSTARTTLS\n8BITMIME'
    send: 'AUTH PLAIN ADE1ODUxMzkwNzM0QDE2My5jb20AaHN6ODgxMjI0\r\n'
    reply: b'235 Authentication successful\r\n'
    reply: retcode (235); Msg: b'Authentication successful'
    send: 'mail FROM:<15851390734@163.com>\r\n'
    reply: b'250 Mail OK\r\n'
    reply: retcode (250); Msg: b'Mail OK'
    send: 'rcpt TO:<469389377@qq.com>\r\n'
    reply: b'250 Mail OK\r\n'
    reply: retcode (250); Msg: b'Mail OK'
    send: 'data\r\n'
    reply: b'354 End data with <CR><LF>.<CR><LF>\r\n'
    reply: retcode (354); Msg: b'End data with <CR><LF>.<CR><LF>'
    data: (354, b'End data with <CR><LF>.<CR><LF>')
    send: b'Content-Type: multipart/alternative; boundary="===============8756843679975483456=="\r\nMIME-Version: 1.0\r\nFrom: master hsz 15851390734@163.com\r\nTo: hsz pythoner 469389377@qq.com\r\nSubject: =?utf-8?b?5p2l6IeqU01UUOeahOmXruWAmeKApuKApg==?=\r\n\r\n--===============8756843679975483456==\r\nContent-Type: text/html; charset="utf-8"\r\nMIME-Version: 1.0\r\nContent-Transfer-Encoding: base64\r\n\r\nPGh0bWw+PGJvZHk+PGgxPkhlbGxvPC9oMT4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxw\r\nPnNlbmQgYnkgPGEgaHJlZj0iaHR0cDovL3d3dy5weXRob24ub3JnIj5QeXRob248L2E+Li4uPC9w\r\nPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgPC9ib2R5PjwvaHRtbD4=\r\n\r\n--===============8756843679975483456==--\r\n.\r\n'
    reply: b'250 Mail OK queued as smtp8,DMCowACHOslvk6hWF1u7AA--.51185S2 1453888371\r\n'
    reply: retcode (250); Msg: b'Mail OK queued as smtp8,DMCowACHOslvk6hWF1u7AA--.51185S2 1453888371'
    data: (250, b'Mail OK queued as smtp8,DMCowACHOslvk6hWF1u7AA--.51185S2 1453888371')
    send: 'quit\r\n'
    reply: b'221 Bye\r\n'
    reply: retcode (221); Msg: b'Bye'





    True


