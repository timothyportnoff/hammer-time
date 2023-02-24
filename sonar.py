#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# ultrasonic_2.py
# Measure distance using an ultrasonic module
# in a loop.
#
# Author : Matt Hawkins
# Date   : 28/01/2013
# Editor : Lara

# -----------------------
# Import required Python libraries
# -----------------------
import time
import RPi.GPIO as GPIO

# -----------------------
# Define some functions
# -----------------------

def measure():
    # This function measures a distance
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()

    while GPIO.input(GPIO_ECHO)==0:
        start = time.time()

    while GPIO.input(GPIO_ECHO)==1:
        stop = time.time()

    elapsed = stop-start
    distance = (elapsed * 34300)/2

    return distance

def measure_average():
    # This function takes 3 measurements and returns the average.
    distance1=measure()
    time.sleep(0.1)
    distance2=measure()
    time.sleep(0.1)
    distance3=measure()
    distance = distance1 + distance2 + distance3
    distance = distance / 3
    return distance

def measure_better_distance():
    # This function takes 3 measurements and returns the average.
    distance1=measure()
    time.sleep(0.05)
    distance2=measure()
    time.sleep(0.05)
    distance3=measure()
    time.sleep(0.05)
    distance4=measure()
    time.sleep(0.05)
    distance5=measure()
    distance = distance1 + distance2 + distance3 + distance4 + distance5
    distance = distance / 5
    return distance

# This function takes in a distance and returns a boolean.
def within_sonar_range(CM):
    if measure_better_distance() < CM: return True       #Try 1
    elif measure_better_distance() < CM: return True  #Try 2
    elif measure_better_distance() < CM: return True  #Try 3
    else: return False

    # -----------------------
# Main Script
# -----------------------

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO    = 24

# Speed of sound in cm/s at temperature
temperature = 20
speedSound = 33100 + (0.6*temperature)

#Hello message
print("Ultrasonic Measurement: sonar.py")
print("Speed of sound is",speedSound/100,"m/s at ",temperature,"deg")

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

# Allow module to settle
# time.sleep(1)

# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.
try:
    min = 1000
    while True:
        distance = measure_average()
        centimeters = distance
        print("Distance : {0:5.1f}".format(distance), "cm")
        #print "Distance : %.1f" % distance
        if centimeters < min:
            min = centimeters
        time.sleep(1)

except KeyboardInterrupt:
    # User pressed CTRL-C
  # Reset GPIO settings
  GPIO.cleanup()
