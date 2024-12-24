import RPi.GPIO as GPIO
import time


buzzer_pin = 18


GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)


    GPIO.output(buzzer_pin, GPIO.HIGH)
    print("HIGH ")
    
   
    time.sleep(5)
    
    
    GPIO.output(buzzer_pin, GPIO.LOW)
    print("LOW ")
    
    
    GPIO.cleanup()