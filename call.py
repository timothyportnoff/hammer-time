#call.py>
#function
import RPi.GPIO as GPIO
import time

def TICKETS():
    
    in1 = 17
    in2 = 18
    in3 = 27
    in4 = 22

    points = 0

    step_sleep = 0.002

    step_count = 4096

    direction = False

    step_sequence = [[1,0,0,1],
                     [1,0,0,0],
                     [1,1,0,0],
                     [0,1,0,0],
                     [0,1,1,0],
                     [0,0,1,0],
                     [0,0,1,1],
                     [0,0,0,1]]

    GPIO.setmode( GPIO.BCM )
    GPIO.setup( in1, GPIO.OUT)
    GPIO.setup( in2, GPIO.OUT)
    GPIO.setup( in3, GPIO.OUT)
    GPIO.setup( in4, GPIO.OUT)

    GPIO.output( in1, GPIO.LOW )
    GPIO.output( in2, GPIO.LOW )
    GPIO.output( in3, GPIO.LOW )
    GPIO.output( in4, GPIO.LOW )
    
    motor_pins = [in1,in2,in3,in4]




    motor_step_counter = 0
    print( "Welcome to Step Motor testing ;)")
    points = int(input( 'how many points did you score: ' ))
    print('You scored: ' , points)
    
    i = 0
    step_count = points * 10
    for i in range(step_count):
        for pin in range(0, len(motor_pins)):
            GPIO.output( motor_pins[pin], step_sequence[motor_step_counter][pin])
            if direction==True:
                motor_step_counter = (motor_step_counter - 1) % 8
            elif direction==False:
                motor_step_counter = (motor_step_counter + 1) % 8
            else:
                print( " WHAT IN THE FUCK DID YOU DO IT SHOULD BE TRUE OR FALSE YOU DUMBASS" )
                cleanup()
                exit(1)
            time.sleep( step_sleep )
    
    GPIO.output(in1, GPIO.LOW )
    GPIO.output(in2, GPIO.LOW )
    GPIO.output(in3, GPIO.LOW )
    GPIO.output(in4, GPIO.LOW )
    GPIO.cleanup()

    










