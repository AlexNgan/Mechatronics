#-------------------------------------------------------------------------------------------------------#
#Author: Mortyyy
#This program allows a robot to be controlled with arrow keys
#through the Linux terminal.
#   Reference:
#   Min pulse length out of 4096 is 150
#   Max pulse length out of 4096 is 600.
#   Stop value for servo in channel 4(left) )is 402.
#   Stop value for servo in channel 5 (right) is 400.
#-------------------------------------------------------------------------------------------------------#
import sys
import curses
import time
from Adafruit_PWM_Servo_Driver import PWM
from curses import wrapper

stdscr = curses.initscr()
pwm = PWM(0x40)
pwm.setPWMFreq(60)

def drive(leftSpd, rightSpd):         # Initialise the PWM device using the default address
    pwm.setPWM(4, 0, leftSpd)
    pwm.setPWM(5, 0, rightSpd)

#Returns console to standard state.
def killSwitch():
    global stdscr
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    drive(402, 400)
    sys.exit()                           #Exits program.

#Configures console to work with arrow keys.
def init():
    global stdscr
    try:        #Configures console to work with arrow keys.
        stdscr.clear()                #Clears screen.
        curses.noecho()
        curses.cbreak()             #Negates usual buffer mode.
        stdscr.keypad(True)      #Enables keypad input.
        while True:
            userSays = stdscr.getch()
            if ord(userSays == "^C"):         #Should handle KeyboardInterrupt.
                killSwitch()
                break
            elif userSays == curses.KEY_UP:            #Forward.
                drive(150, 600)
            elif userSays == curses.KEY_DOWN:    #Backwards.
                drive(600, 150)
            elif userSays == curses.KEY_LEFT:         #Left.
                drive(150, 150)
            elif userSays == curses.KEY_RIGHT:      #Right.
                drive(600, 600)
            elif userSays == 115:                   #Stops if 's' is inputted.
                drive(402, 400)
    except KeyboardInterrupt:  #Returns console to standard state.
        killSwitch()

init()
