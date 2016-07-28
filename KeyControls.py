#Author: Gloria
#This program is a test for Python's curse functions.

import sys
import curses

#Configures console to work with arrow keys.
def config():
    stdscr = curses.initscr()
    stdscr.clear()                #Clears screen.
    curses.noecho()
    curses.cbreak()             #Negates usual buffer mode.
    stdscr.keypad(True)       #Enables keypad input.

#Returns console to standard state.
def revert():
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    sys.exit()
