
#coding:utf-8

from employee import *
from tools import *
from customer import *
class PizzaShop:

    def __init__(self):
        self.waiter = Waiter("Pat")
        self.chef = PizzaRobot('Bob')
        self.oven = Oven()

    def order(self,name):
        customer = Customer(name)
        customer.order(self.waiter)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.waiter)