
一个人在公司工作时间久了，难免遇到一点自己的私事，有私事就可能耽误上班的时间，可能就要请假，那么和谁去请假呢？可能是每个公司都有自己的请假制度。我们不妨假设：请假半天只要和部门主管说一声就行了，请假在半天到2天之间要通过人事部门，而请假超过两天就不那么好申请了，这时可能要总经理或者更高级别的人同意才行了。如果不考虑设计模式直接写代码，要完成这个逻辑就可能用到if—else或者多个if了.

如果我们把每个管理者都写一个类，每个管理者都负责处理请假信息，但是只有当主管处理不了时，才交给人事部门处理，以此类推。那么就是可以写出来一个职责链模式的代码

职责链模式（Chain Of Responsibility）：使多个对象都有机会处理请求，从而避免请求的发送者和接受者之间的耦合关系。将这个对象连成一条链，并沿着这条链传递该请求，直到有一个对象处理他为止。

说的通俗一点就是：职责链模式就是把让请求沿着链条一直传下去，知道有一个对象能够处理这个请求。在职责链上的对象都有机会处理到请求，但是只有前一个职责链不能完成请求的处理，才将请求传递给下一个对象。可以看出职责链上的对象到底谁能完成请求的处理是不确定的。并且需要注意的是，职责链是在客户端动态确定的哦，具体职责链上对象的顺序也是动态确定的。还是看看结构图

使用职责链模式的场合：

个人觉得，职责链模式主要用于当一个请求有多种处理方式的时候，并且具体处理方式不确定的情况。

使用职责链模式的优点：

1. 增强了系统的可扩展性。

2. 使用职责链模式可以避免众多的if或者if-else语句。

3. 使用职责链模式可以减小对象之间的耦合性。使得对象之间的联系减小。

4. 可以根据需要自由组合工作流程。如工作流程发生变化，可以通过重新分配对象链便可适应新的工作流程。

5. 责任的分担。每个类只需要处理自己该处理的工作（不该处理的传递给下一个对象完成），明确各类的责任范围，符合类的最小封装原则。

使用职责链模式的缺点：

1. 使用职责链模式的时候会有多个处理者对象，但是实际使用的处理者对象却只有一个，这在某种程度讲是资源的浪费。

2. 同时职责链的建立的合理性要靠客户端来保证，增加了程序的复杂性，也有可能由于职责链导致出错。

> 例


```python
# coding:utf-8
def printInfo(info):  
    #print unicode(info, 'utf-8').encode('gbk')  
    print(info)
#抽象职责类  
class Manager():  
    successor = None  
    name = ''  
    def __init__(self, name):  
        self.name = name  
      
    def SetSuccessor(self, successor):  
        self.successor = successor  
      
    def HandleRequest(self, request):  
        pass  
#具体职责类：经理  
class CommonManager(Manager):  
    def HandleRequest(self, request):  
        if request.RequestType == '请假' and request.Number <= 2:  
            printInfo('%s:%s 数量%d 被批准' % (self.name, request.RequestContent, request.Number))  
        else:  
            if self.successor != None:  
                self.successor.HandleRequest(request)  
                  
#具体职责类：总监  
class Majordomo(Manager):  
    def HandleRequest(self, request):  
        if request.RequestType == '请假' and request.Number <= 5:  
            printInfo('%s:%s 数量%d 被批准' % (self.name, request.RequestContent, request.Number))  
        else:  
            if self.successor != None:  
                self.successor.HandleRequest(request)  
#具体职责类：总经理  
class GeneralManager(Manager):  
    def HandleRequest(self, request):  
        if request.RequestType == '请假':  
            printInfo('%s:%s 数量%d 被批准' % (self.name, request.RequestContent, request.Number))  
        elif request.RequestType == '加薪' and request.Number <= 500:  
            printInfo('%s:%s 数量%d 被批准' % (self.name, request.RequestContent, request.Number))  
        elif request.RequestType == '加薪' and request.Number > 500:  
            printInfo('%s:%s 数量%d 再说吧' % (self.name, request.RequestContent, request.Number))  
class Request():  
    RequestType = ''  
    RequestContent = ''  
    Number = 0  
def clientUI():  
    jinLi = CommonManager('金力')  
    zongJian = Majordomo('宗健')  
    zhongJingLi = GeneralManager('钟金利')  
      
    jinLi.SetSuccessor(zongJian)  
    zongJian.SetSuccessor(zhongJingLi)  
      
    request = Request()  
    request.RequestType = '请假'  
    request.RequestContent = '小菜请假'  
    request.Number = 1  
    jinLi.HandleRequest(request)  
      
    request.RequestType = '请假'  
    request.RequestContent = '小菜请假'  
    request.Number = 5  
    jinLi.HandleRequest(request)  
      
    request.RequestType = '加薪'  
    request.RequestContent ='小菜要求加薪'  
    request.Number = 500  
    jinLi.HandleRequest(request)  
      
    request.RequestType = '加薪'  
    request.RequestContent = '小菜要求加薪'  
    request.Number = 1000  
    jinLi.HandleRequest(request)  
    return  
  

clientUI()
```

    金力:小菜请假 数量1 被批准
    宗健:小菜请假 数量5 被批准
    钟金利:小菜要求加薪 数量500 被批准
    钟金利:小菜要求加薪 数量1000 再说吧



```python

```
