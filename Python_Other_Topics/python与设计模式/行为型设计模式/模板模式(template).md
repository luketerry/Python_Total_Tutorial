
模板方法模式：定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。模板方法使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。

使用模板方法模式的场合和好处:

模板方法模式是通过把不变的行为搬移到超类(这边也可以是一个方法)，去除子类中的重复代码来体现它的优势的。也就提供了一个很好的代码复用平台。如果以后遇到这种情况：有一个过程需要执行，这个过程包括一系列步骤，整个过程从高层次看是一样的，但是每个步骤的具体细节不一样，这时我们就可以考虑这种模板方法模式了。即当不变的行为和可变的行为在类中混在一起的时候，不变的行为就会在子类中重复出现，这是通过模板方法模式把这些行为搬移到单一的地方实现（超类），而把不同的部分在子类实现，这就使子类摆脱了重复的不变行为的困扰。


```python
ingredients = "spam eggs apple"
line = '-' * 10


# Skeletons
def iter_elements(getter, action):
    """Template skeleton that iterates items"""
    for element in getter():
        action(element)
        print(line)


def rev_elements(getter, action):
    """Template skeleton that iterates items in reverse order"""
    for element in getter()[::-1]:
        action(element)
        print(line)


# Getters
def get_list():
    return ingredients.split()


def get_lists():
    return [list(x) for x in ingredients.split()]


# Actions
def print_item(item):
    print(item)


def reverse_item(item):
    print(item[::-1])


# Makes templates
def make_template(skeleton, getter, action):
    """Instantiate a template method with getter and action"""
    def template():
        skeleton(getter, action)
    return template

# Create our template functions
templates = [make_template(s, g, a)
             for g in (get_list, get_lists)
             for a in (print_item, reverse_item)
             for s in (iter_elements, rev_elements)]

# Execute them
for template in templates:
    template()
```

    spam
    ----------
    eggs
    ----------
    apple
    ----------
    apple
    ----------
    eggs
    ----------
    spam
    ----------
    maps
    ----------
    sgge
    ----------
    elppa
    ----------
    elppa
    ----------
    sgge
    ----------
    maps
    ----------
    ['s', 'p', 'a', 'm']
    ----------
    ['e', 'g', 'g', 's']
    ----------
    ['a', 'p', 'p', 'l', 'e']
    ----------
    ['a', 'p', 'p', 'l', 'e']
    ----------
    ['e', 'g', 'g', 's']
    ----------
    ['s', 'p', 'a', 'm']
    ----------
    ['m', 'a', 'p', 's']
    ----------
    ['s', 'g', 'g', 'e']
    ----------
    ['e', 'l', 'p', 'p', 'a']
    ----------
    ['e', 'l', 'p', 'p', 'a']
    ----------
    ['s', 'g', 'g', 'e']
    ----------
    ['m', 'a', 'p', 's']
    ----------



```python

```
