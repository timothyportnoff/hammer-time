import RPi.GPIO as GPIO
import threading
from tickets import * 
from motor import * 
from speaker import * 
from button import * 
from led import * 
from time import sleep

#CONSTANTS
POTENTIOMMETER = 0
START_BUTTON = 26
STOP_BUTTON = 0
TRIG = 17
ECHO = 27
#BUZZER = 0
#KNOB = 0
#MOTOR = 0
#YELLOW = 0
#GREEN = 0
#BLUE = 0
#RED = 0

#SETUP
def setup():
    #GPIO settings
    GPIO.setmode(GPIO.BCM)

    #GPIO.setup(START_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # set in as off when initializing
    GPIO.setup(26, GPIO.IN)

#main function
if __name__ =="__main__":
    #Welcome, and setup
    setup()
    print("It's Hammer Time.")

    #check distance
    while True:
        get_distance()
            # Create new threads
            #thread1 = spin_motor(1, "Thread-1-sound", 1)
            #threa2 = play_sound(2, "Thread-2-sound", 2)

            # Start new Threads
            #thread1.start()
            #thread2.start()

        #elif button_is_pressed(STOP_BUTTON): # Sleep for half a second? FIXME
            #print("stop button pressed!")
        #else: 
        sleep(0.1)

    #Exit cleanly
    GPIO.cleanup()
