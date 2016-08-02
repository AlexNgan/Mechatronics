#-----------------------------------------------------#
# Author: Gloria
# This program allows a user to control the claw
# of the robot using the A and D keys. Pressing S
# stops the claw.
#
# Note that the claw has a mechanical stopper that 
# restricts movement beyond a certain point. Motor
# can still be damaged if it is kept running against
# stopper.
#-----------------------------------------------------#

import sys
import time
from Adafruit_PWM_Servo_Driver import PWM

pwm = PWM(0x40)
pwm.setPWMFreq(60)

def moveClaw(speed, time):
	pwm.setPWM(6, 0, speed)
	time.sleep(time)

moveClaw(100, 1)
