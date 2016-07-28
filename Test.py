# Program quits completely if a Keyboard Interrupt is registered,
# even in an infinite while loop.

import sys    #GOTTA HAVE THIS.

def interruptTest():
    try:
        #Put code that you want to actually run here.
        while True:
            print "Hi."
    except KeyboardInterrupt:
        #Quits the try above if ctrl+c is inputted.
        sys.exit()

interruptTest()
