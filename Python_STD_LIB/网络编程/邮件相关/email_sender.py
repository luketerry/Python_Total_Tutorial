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