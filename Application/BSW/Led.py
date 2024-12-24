import RPi.GPIO as GPIO
import time

LOW = 0
HIGH = 1

#Function that initializes led as output
def Led_init(pin_no):

    #Set the pin numbering mode
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(pin_no, GPIO.OUT)




#Function that toggles led (warning)
def Led_warning(pin_no, delay_sec):

    GPIO.output(pin_no, GPIO.HIGH)
    time.sleep(delay_sec)

    GPIO.input(pin_no, GPIO.LOW)
    time.sleep(delay_sec)

    GPIO.cleanup()



