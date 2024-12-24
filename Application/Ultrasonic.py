import RPi.GPIO as GPIO 
import time

trig_pin = 26
echo_pin = 6

# initialize ultrasonic pins
def ultrasonic_init():

    GPIO.setwarnings(False)

    #Set the pin numbering mode
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(trig_pin, GPIO.OUT)
    GPIO.setup(echo_pin, GPIO.IN) 

# measure distance in cm
def ultrasonic_calc_distance():

    GPIO.output(trig_pin, GPIO.LOW) 
    time.sleep(2)
    GPIO.output(trig_pin, GPIO.HIGH) 
    time.sleep(0.00001) 
    GPIO.output(trig_pin, GPIO.LOW)

    while GPIO.input(echo_pin)==0: 

        start_time = time.time() 

    while GPIO.input(echo_pin)==1: 

        Bounce_back_time = time.time() 

    pulse_duration = Bounce_back_time - start_time 

    distance = round(pulse_duration * 17150, 2) 
    
    #GPIO.cleanup()
    return distance  


"""
try:
    ultrasonic_init()
    while True:

        distance = ultrasonic_calc_distance()
        print(f"Distance = ", distance)
    
except KeyboardInterrupt:
    pass 
"""   
    

		    
 



    
