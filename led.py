import RPi.GPIO as GPIO

def led_on(PIN):
    GPIO.output(PIN, GPIO.HIGH)

def led_off(PIN):
    GPIO.output(PIN, GPIO.LOW)

def led_off(PIN1, PIN2):
    GPIO.output(PIN1, GPIO.LOW)
    GPIO.output(PIN2, GPIO.LOW)

def led_off(PIN1, PIN2, PIN3):
    GPIO.output(PIN1, GPIO.LOW)
    GPIO.output(PIN2, GPIO.LOW)
    GPIO.output(PIN3, GPIO.LOW)

def blink_led ():
    print("Waiting for 1 second")
    sleep(1)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(19, GPIO.HIGH)

    print("Waiting for 1 second")
    sleep(1)
    GPIO.output(17, GPIO.LOW)
    


