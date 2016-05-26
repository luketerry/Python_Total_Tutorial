
#coding:utf-8

class Customer:
    def __init__(self,name):
        self.name = name
        
    def order(self,waiter):
        print(self.name," ordered a pizza from ",waiter)

    def pay(self,waiter):
        print(self.name," has payed to ",waiter)