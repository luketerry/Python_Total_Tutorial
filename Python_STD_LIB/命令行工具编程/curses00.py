# -*- coding: utf-8 -*-
import curses
screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
screen.keypad(1)

screen.addstr("hello world!\n\n")
while True:
    event = screen.getch()
    if event == ord("q"): break
curses.endwin()