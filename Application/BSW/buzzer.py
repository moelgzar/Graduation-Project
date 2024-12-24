import RPi.GPIO as GPIO
import time


#Function that initializes buzzer pin
def buzzer_init(buzzer_pin):

    #Set the pin numbering mode
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(buzzer_pin, GPIO.OUT) 


#Function that gives buzzer warning
def buzzer_warning(buzzer_pin, delay_sec):

    GPIO.output(buzzer_pin,GPIO.HIGH)
    time.sleep(delay_sec) 

    GPIO.output(buzzer_pin,GPIO.LOW)
    time.sleep(delay_sec)

    GPIO.cleanup()
