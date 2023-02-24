import RPi.GPIO as GPIO
import threading
from tickets import * 
from led import * 
from time import sleep
from sonar import *
#from motor import * 
#from speaker import * 
#from button import * 

#CONSTANTS
POTENTIOMMETER = 0
START_BUTTON = 26
STOP_BUTTON = 0
TRIG = 17
ECHO = 27
#BUZZER = 0
#KNOB = 0
#MOTOR = 0

#LED'S
RED = 2
YELLOW = 3
GREEN = 4
#BLUE = 0

#SETUP
def setup():
    #GPIO settings
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.IN)

#main function
if __name__ =="__main__":
    #Welcome, and setup
    print("It's Hammer Time.")
    setup()

    #check distance
    while True:
        puck_seen = 0
        #DISTANCE = get_distance()
        if within_sonar_range(90):
            puck_seen = puckseen + 1
            led_on(RED)
            if within_sonar_range(60):
                puck_seen = puckseen + 1
                led_on(YELLOW)
                if within_sonar_range(30):
                    puck_seen = puckseen + 1
                    led_on(GREEN)
        sleep(0.1)
        if puck_seen > 0:
            break
        sleep(0.1)
        print_tickets()

    #Exit cleanly
    print("Exiting program.")
    GPIO.cleanup()
