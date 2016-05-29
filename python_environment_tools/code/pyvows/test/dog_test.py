# coding:utf-8
from __future__ import print_function,absolute_import, unicode_literals

from pyvows import Vows,expect
import sys
import os
from forgery_py import name as random_name
from random import randint

root = os.path.dirname(os.path.dirname(__file__))
sys.path[0] = root

import dog


@Vows.batch
class DogTest(Vows.Context):
    def topic(self):
        name = random_name.full_name()
        age = randint(18,30)
        return dog.Dog(name,age)
 
    def can_eat(self, topic):
        food = "apple"
        expect(topic.eat(food)).to_equal("{topic.name} is eating {food}".format(topic=topic, food=food))
 
    def can_be_print(self, topic):
        expect(str(topic)).to_equal("<Dog:{topic.name}--{topic.age}>".format(topic=topic))
 