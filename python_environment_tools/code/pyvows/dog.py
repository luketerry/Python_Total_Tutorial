# coding:utf-8
from __future__ import print_function, unicode_literals


class Dog(object):

    def __str__(self):
        return "<Dog:{self.name}--{self.age}>".format(self=self)

    def __repr__(self):
        return self.__str__()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        return "{self.name} is eating {food}".format(self=self, food=food)
