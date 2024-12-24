import RPi.GPIO as GPIO
import time

buzzer_pin = 21
delay_sec = 2

#initializes buzzer pin
def buzzer_init():

    #Set the pin numbering mode
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(buzzer_pin, GPIO.OUT) 


#toggle buzzer 
def buzzer_warning():

    GPIO.output(buzzer_pin,GPIO.HIGH)
    time.sleep(delay_sec) 

    GPIO.output(buzzer_pin,GPIO.LOW)
    time.sleep(delay_sec)

    GPIO.cleanup()
