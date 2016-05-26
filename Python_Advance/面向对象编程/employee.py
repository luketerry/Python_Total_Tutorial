
#coding:utf-8

class Employee(object):
    u"""员工基类,规定名字,薪水的基本属性和基本的方法,涨工资,工作,打印
    """
    id = 0
    def __init__(self,name,salary=0):
        self.id = Employee.id
        self.name = name
        self.salary = salary
        Employee.id += 1

    def salary_raise(self,raised_ratio=0,raised_value=0):
        self.salary = self.salary*(1+raised_ratio)+raised_value

    def work(self):
        print(self.name," is working!")

    def __repr__(self):
        return "<id:{id}, employee:{name},salary:{salary}>".format(id = self.id,name = self.name,salary = self.salary)

class Chef(Employee):
    def __init__(self,name):
        Employee.__init__(self,name,5000)

    def work(self):
        print(self.name,"is cooking!")

class Waiter(Employee):
    def __init__(self,name):
        Employee.__init__(self,name,2000)
    def work(self):
        print(self.name,"is servering a customer")

class PizzaRobot(Chef):
    def __init__(self,name):
        Chef.__init__(self,name)

    def work(self):
        print(self.name,"is cooking pizzas")