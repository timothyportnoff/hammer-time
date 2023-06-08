import RPi.GPIO as GPIO
from time import sleep

def print_tickets (num):
    print("Printing out ", num, " tickets")
    #GPIO.output(17, GPIO.HIGH) #run ticket motor
    #GPIO.output(17, GPIO.LOW) #stop ticket motor
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
    i = 0
    step_count = points * 10
    for i in range(step_count):
        for pin in range(0, len(motor_pins)):
            GPIO.output( motor_pins[pin], step_sequence[motor_step_counter][pin])
            if direction==True:
                motor_step_counter = (motor_step_counter - 1) % 8
            else:
                motor_step_counter = (motor_step_counter + 1) % 8
            time.sleep(step_sleep)
    
    GPIO.output(in1, GPIO.LOW )
    GPIO.output(in2, GPIO.LOW )
    GPIO.output(in3, GPIO.LOW )
    GPIO.output(in4, GPIO.LOW )
    #GPIO.cleanup()
    return


if __name__ =="__main__":
    print("main: sonar.py")
    # Wrap main content in a try block so we can
    # catch the user pressing CTRL-C and run the
    # GPIO cleanup function. This will also prevent
    # the user seeing lots of unnecessary error
    # messages.
    try:
        print_tickets(1)
        sleep(0.5)
        print_tickets(2)
        sleep(0.5)
        print_tickets(3)
        sleep(0.5)

    except KeyboardInterrupt:
        # User pressed CTRL-C
      # Reset GPIO settings
      GPIO.cleanup()
