
抽象工厂模式是工厂模式的扩展,它和工厂方法模式不同之处在于,其实它需要判断使用什么工厂而不是使用什么类,打个比方

宠物店有猫有狗,我们只是要找个宠物,是猫是狗的需要我们自己定义

抽象工厂同样也是模式匹配,只是它匹配的是一个抽象概念而不是对象


```python
import random


class PetShop:

    """A pet shop"""

    def __init__(self, animal_factory=None):
        """pet_factory is our abstract factory.  We can set it at will."""

        self.pet_factory = animal_factory

    def show_pet(self):
        """Creates and shows a pet using the abstract factory"""

        pet = self.pet_factory.get_pet()
        print("We have a lovely {}".format(pet))
        print("It says {}".format(pet.speak()))
        print("We also have {}".format(self.pet_factory.get_food()))


# Stuff that our factory makes

class Dog:

    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class Cat:

    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"


# Factory classes

class DogFactory:

    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food"


class CatFactory:

    def get_pet(self):
        return Cat()

    def get_food(self):
        return "cat food"


# Create the proper family
def get_factory():
    """Let's be dynamic!"""
    return random.choice([DogFactory, CatFactory])()


# Show pets with various factories
if __name__ == "__main__":
    for i in range(3):
        shop = PetShop(get_factory())
        shop.show_pet()
        print("=" * 20)
```

    We have a lovely Dog
    It says woof
    We also have dog food
    ====================
    We have a lovely Dog
    It says woof
    We also have dog food
    ====================
    We have a lovely Dog
    It says woof
    We also have dog food
    ====================

