#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import sys

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096
leftStop = 402  # Stop value for servo in channel 1
rightStop = 400 # Stop value for servo in channel 0

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)
try:                    # Set frequency to 60 Hz
     while (True):
		  pwm.setPWM(0, 0, servoMin)
		  pwm.setPWM(1, 0, servoMax)
		  time.sleep(1)
		  pwm.setPWM(0, 0, 400)
		  pwm.setPWM(1, 0, 402)
		  time.sleep(1)
except KeyboardInterrupt:
    pwm.setPWM(0, 0, 400)
    pwm.setPWM(1, 0, 402)
    sys.exit()
