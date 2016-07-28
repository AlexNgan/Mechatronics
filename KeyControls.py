#Author: Gloria
#This program is a test for Python's curse functions.

import sys
import curses
from curses import wrapper

#Configures console to work with arrow keys.
def config():
    try:        #Configures console to work with arrow keys.
        stdscr = curses.initscr()
        stdscr.clear()                #Clears screen.
        curses.noecho()
        curses.cbreak()             #Negates usual buffer mode.
        stdscr.keypad(True)       #Enables keypad input.

        userSays = stdscr.getch()
        if userSays == curses.KEY_UP:
            print ("Yay.")
    except KeyboardInterrupt:  #Returns console to standard state.
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        sys.exit()
