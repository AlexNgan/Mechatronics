#-------------------------------------------------------------------------------------------------------#
#Author: Gloria
#This program allows a robot to be controlled with arrow keys
#through the Linux terminal and a GUI. Utlizes Tkinter.
#   Reference:
#   Min pulse length out of 4096 is 150
#   Max pulse length out of 4096 is 600.
#   Stop value for servo in channel 1(left) )is 402.
#   Stop value for servo in channel 0 (right) is 400.
#-------------------------------------------------------------------------------------------------------#
import Tkinter as Tk
import sys
import time
from Adafruit_PWM_Servo_Driver import PWM
from gopigo import *

pwm.setPWMFreq(60)
pwm = PWM(0x40)         # Initialise the PWM device using the default address
controller = Tk()

def drive(leftSpd, rightSpd):
    global pwm
    pwm.setPWM(0, 0, leftSpd)
    pwm.setPWM(1, 0, rightSpd)
    time.sleep(0.05)
    pwm.setPWM(0, 0, 402)
    pwm.setPWM(1, 0, 400)
    time.sleep(0.05)

#Returns console to standard state.
def killSwitch():
    global stdscr
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    sys.exit()                           #Exits program.

def key_input(event):
    key_press = event.keysym.lower()
    print(key_press)

def init():
    global controller
    w = Label(controller, text="Use arrow keys to control the robot."")
    w.pack()
    self.quitButton = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.quitButton.pack(side=LEFT

controller.bind_all('', key_input)
controller.mainloop()
controller.destroy()           #Needed?
