import sys
import curses
from curses import wrapper

#Author: Gloria
#This program allows a robot to be controlled with arrow keys
#through the Linux terminal.

def drive(leftSpd, rightSpd):
    #code here.

#Returns console to standard state.
def killSwitch():
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    sys.exit()                           #Exits program.

#Configures console to work with arrow keys.
def init():
    try:        #Configures console to work with arrow keys.
        stdscr = curses.initscr()
        stdscr.clear()                #Clears screen.
        curses.noecho()
        curses.cbreak()             #Negates usual buffer mode.
        stdscr.keypad(True)      #Enables keypad input.
        while True:
            userSays = stdscr.getch()
            if userSays == 3:         #Should handle KeyboardInterrupt.
                killSwitch()
                break
            elif userSays == curses.KEY_UP:
                print("Hi.")
            # elif userSays == curses.KEY_DOWN:
            #     drive()
            # elif userSays == curses.KEY_LEFT:
            #     drive()
            # elif userSays == curses.KEY_RIGHT:
            #     drive()
            # else:
            #     drive()
    except:  #Returns console to standard state.
        killSwitch()

init()
