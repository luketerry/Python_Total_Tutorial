
中介模式其实作用就是把一个网状结构的关系变成星型结构
而中介在其中就是扮演了中心节点的作用,举个例子,村门口的告示板,qq群微信群等等,又比如共享缓存这种


中介者模式（Mediator Pattern）：定义一个中介对象来封装系列对象之间的交互。中介者使各个对象不需要显示地相互引用，从而使其耦合性松散，而且可以独立地改变他们之间的交互。

使用终结者模式的场合

1. 一组定义良好的对象，现在要进行复杂的通信。

2. 定制一个分布在多个类中的行为，而又不想生成太多的子类。

可以看出，中介对象主要是用来封装行为的，行为的参与者就是那些对象，但是通过中介者，这些对象不用相互知道。呵呵~~~

使用中介者模式的优点：

1. 降低了系统对象之间的耦合性，使得对象易于独立的被复用。

2. 提高系统的灵活性，使得系统易于扩展和维护。

使用中介者模式的缺点：

中介者模式的缺点是显而易见的，因为这个“中介“承担了较多的责任，所以一旦这个中介对象出现了问题，那么整个系统就会受到重大的影响。

> 例: 


```python
import random
import time
class TC:

    def __init__(self):
        self._tm = None
        self._bProblem = 0

    def setup(self):
        print("Setting up the Test")
        time.sleep(0.1)
        self._tm.prepareReporting()

    def execute(self):
        if not self._bProblem:
            print("Executing the test")
            time.sleep(0.1)
        else:
            print("Problem in setup. Test not executed.")

    def tearDown(self):
        if not self._bProblem:
            print("Tearing down")
            time.sleep(0.1)
            self._tm.publishReport()
        else:
            print("Test not executed. No tear down required.")

    def setTM(self, tm):
        self._tm = tm

    def setProblem(self, value):
        self._bProblem = value


class Reporter:

    def __init__(self):
        self._tm = None

    def prepare(self):
        print("Reporter Class is preparing to report the results")
        time.sleep(0.1)

    def report(self):
        print("Reporting the results of Test")
        time.sleep(0.1)

    def setTM(self, tm):
        self._tm = tm


class DB:

    def __init__(self):
        self._tm = None

    def insert(self):
        print("Inserting the execution begin status in the Database")
        time.sleep(0.1)
        # Following code is to simulate a communication from DB to TC
        if random.randrange(1, 4) == 3:
            return -1

    def update(self):
        print("Updating the test results in Database")
        time.sleep(0.1)

    def setTM(self, tm):
        self._tm = tm


class TestManager:

    def __init__(self):
        self._reporter = None
        self._db = None
        self._tc = None

    def prepareReporting(self):
        rvalue = self._db.insert()
        if rvalue == -1:
            self._tc.setProblem(1)
            self._reporter.prepare()

    def setReporter(self, reporter):
        self._reporter = reporter

    def setDB(self, db):
        self._db = db

    def publishReport(self):
        self._db.update()
        self._reporter.report()

    def setTC(self, tc):
        self._tc = tc


reporter = Reporter()
db = DB()
tm = TestManager()
tm.setReporter(reporter)
tm.setDB(db)
reporter.setTM(tm)
db.setTM(tm)
# For simplification we are looping on the same test.
# Practically, it could be about various unique test classes and their
# objects
for i in range(3):
    tc = TC()
    tc.setTM(tm)
    tm.setTC(tc)
    tc.setup()
    tc.execute()
    tc.tearDown()

```

    Setting up the Test
    Inserting the execution begin status in the Database
    Executing the test
    Tearing down
    Updating the test results in Database
    Reporting the results of Test
    Setting up the Test
    Inserting the execution begin status in the Database
    Reporter Class is preparing to report the results
    Problem in setup. Test not executed.
    Test not executed. No tear down required.
    Setting up the Test
    Inserting the execution begin status in the Database
    Executing the test
    Tearing down
    Updating the test results in Database
    Reporting the results of Test

