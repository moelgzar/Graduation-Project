import RPi.GPIO as GPIO
import threading

trig_pin = 23
echo_pin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(trig_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)


def measure_distance():
    # send signal to start measure
    GPIO.output(trig_pin, GPIO.HIGH)

    time.sleep(0.00001)

    GPIO.output(trig_pin, GPIO.LOW)
    
    # read respond time
    while GPIO.input(echo_pin) == 0:
        pulse_start = time.time()

    while GPIO.input(echo_pin) == 1:
        pulse_end = time.time()
    
    # determine the distanse
    pulse_duration = pulse_end - pulse_start
    
    distance = pulse_duration * 17150

    distance = round(distance, 2)
    
    return distance
