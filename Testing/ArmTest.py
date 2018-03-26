#-----------------------------------------------------#
# Author: Mortyyy
# Note that the claw has a mechanical stopper that 
# restricts movement beyond a certain point. Motor
# can still be damaged if it is kept running against
# stopper.
# Reference:
#	100 - Open claw fully (sleep 1).
#	440 - Close all the way (sleep 1).
#-----------------------------------------------------#
import time
from Adafruit_PWM_Servo_Driver import PWM

pwm = PWM(0x40)
pwm.setPWMFreq(60)

def moveClaw(speed, sleepTime):
	pwm.setPWM(6, 0, speed)
	time.sleep(sleepTime)

#Need following to ensure motor stops.
def stopClaw():
	pwm.setPWM(6, 0, 0)
	time.sleep(1)

moveClaw(110, 1)
stopClaw()
