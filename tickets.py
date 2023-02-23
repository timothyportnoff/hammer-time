import RPi.GPIO as GPIO

def print_tickets (num):
    print("Printing out " + num + " tickets")
    #GPIO.output(17, GPIO.HIGH) #run ticket motor

    print("Waiting for 1 second")
    sleep(1)

    #GPIO.output(17, GPIO.LOW) #stop ticket motor
    


