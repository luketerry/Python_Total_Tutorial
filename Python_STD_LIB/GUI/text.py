
#coding:utf-8
try:
    from tkinter import *
except ImportError:
    from Tkinter import *
    
root = Tk()

text = Text(root)
text.pack()

# INSERT 索引表示插入光标当前的位置
text.insert(INSERT, "I love ")
text.insert(END, "Python!")

mainloop()