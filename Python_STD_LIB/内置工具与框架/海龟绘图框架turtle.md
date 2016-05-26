
# 海龟绘图框架(turtle)

Python内置的一个绘图库,基于Tk.用起来很简单.可以玩玩试试.


海龟绘图属性：

+ 位置
+ 方向
+ 画笔(画笔的属性，颜色、画线的宽度)

操纵海龟绘图有着许多的命令,这些命令可以划分为两种:

+ 运动命令

命令|说明
---|---
forward(degree)  |向前移动距离degree代表距离
backward(degree)  |向后移动距离degree代表距离
right(degree)    |向右移动多少度
left(degree)  |向左移动多少度
goto(x,y)  |将画笔移动到坐标为x,y的位置
stamp()     |复制当前图形
speed(speed)  |画笔绘制的速度范围[0,10]整数
reset()|是将整个画布清空并将画笔置于原点(画布的中心)

+ 画笔控制命令

命令|说明
---|---
down() |移动时绘制图形,缺省时也为绘制
up() |移动时不绘制图形
pensize(width) |设置绘制图形时的宽度
color(colorstring) |设置绘制图形时笔的颜色
fillcolor(colorstring) |设置绘制图形的填充颜色
fill(Ture)|---
fill(false)|---

> 例子:画个正方形


```python
%%writefile sq.py
#--*-- coding:utf-8 --*--
import turtle
import time
#定义绘制时画笔的颜色
turtle.color("purple")
#定义绘制时画笔的线条的宽度
turtle.pensize(5)
#定义绘图的速度 
turtle.speed(10)
#以0,0为起点进行绘制
turtle.goto(0,0)
turtle.down()
#绘出正方形的四条边
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
#画笔移动到点(-150,-120)时不绘图
turtle.up()
turtle.goto(-150,-120)
#再次定义画笔颜色
turtle.color("red")
#在(-150,-120)点上打印"Done"
turtle.write("Done")
time.sleep(3)
```

    Overwriting sq.py



```python
!python3 sq.py
```

> 画个五角星


```python
%%writefile fs.py
#--*-- coding:utf-8 --*--
import turtle
import time
turtle.color("purple")
turtle.pensize(5)
turtle.goto(0,0)
turtle.speed(10)
turtle.down()
for i in range(6):
    turtle.forward(100)
    turtle.right(144)
turtle.up()
turtle.forward(100)
turtle.goto(-150,-120)
turtle.color("red")
turtle.write("Done")
time.sleep(3)
```

    Writing fs.py



```python
!python3 fs.py
```
