#Author: Gloria
#This program is a test for Python's curse functions.
#Should print "Yay" when the up arrow key is struck.
#Hit ctrl+c to exit.

import sys
import curses

def init():
    try:
        stdscr = curses.initscr()
        stdscr.clear()                #Clears screen.
        curses.noecho()
        curses.cbreak()             #Negates usual buffer mode.
        stdscr.keypad(True)       #Enables keypad input.
        
        userSays = stdscr.getKey()
        if userSays == KEY_UP:
           print "Yay."
    except KeyboardInterrupt:
        #Will return terminal to regular state.
        curses.nocbreak()
        stdscr.keypad(False)    
        curses.echo()
        curses.endwin()
        sys.exit()
       
init()
