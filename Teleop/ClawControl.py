#-------------------------------------------------------------------------------------------------------#
#Author: Mortyyy
#This program allows the claw to be controlled with the A and D  keys
#through the Linux terminal.
#   Reference:
#   Min pulse length out of 4096 is 150
#   Max pulse length out of 4096 is 600.
#   100 (sleep 1) opens claw fully.
#   440 (sleep 1) closes claw fully.
#-------------------------------------------------------------------------------------------------------#
import sys
import time
from Adafruit_PWM_Servo_Driver import PWM

pwm = PWM(0x40)
pwm.setPWMFreq(60)
armPWM = 440

#Function that adjusts the movement of the claw based on input.
def incrementClaw(sgn):
    global  armPWM
    temp = armPWM
    armPWM = temp + sgn * 10

    #Prevents value from exceeding mechansm limit.
    if armPWM > 440:
        armPWM = temp
        return
    elif armPWM < 100:
        armPWM = 100
        return
    pwm.setPWM(6,0, armPWM)

#Funtion to open/close the claw a predetermined amount.
def moveClaw(speed, sleepTime):
    pwm.setPWM(6, 0, speed)
    time.sleep(sleepTime)

def init():
    try:
        pwm.setPWM(6,0,440)           #Robot closes claw automatically when program starts.
        while True:
            userSays = stdscr.getch()
            if userSays == 97:                #Closes claw.
                incrementClaw(-1)
            elif userSays == 100:           #Opens claw.
                incrementClaw(1)
            elif userSays == 115:           #Stops claw.
                moveClaw(6, 0, 0)
    except KeyboardInterrupt:
        moveClaw(6, 0, 0)

init()
