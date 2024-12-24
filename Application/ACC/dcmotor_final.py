import RPi.GPIO as GPIO
import time

enable = 12
in1 = 23
in2= 24
frequency = 100
initial_speed = 50

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def dc_motor_init():
    GPIO.setup(enable, GPIO.OUT)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    global pwm
    pwm = GPIO.PWM(enable, frequency)

def dc_motor_set_speed(initial_speed):
    pwm.start(initial_speed)  

def dc_motor_move_forward():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)

def dc_motor_stop():
    pwm.stop()    

def dc_motor_decrease_speed(initial_speed, decrement):
    pwm.ChangeDutyCycle(initial_speed-decrement)

def dc_motor_increase_speed(initial_speed, increment):
    pwm.ChangeDutyCycle(initial_speed+increment)  


#Example app
dc_motor_init()
dc_motor_set_speed(initial_speed)
try:
    while True:
        dc_motor_move_forward()
        dc_motor_decrease_speed(initial_speed, 30)
        dc_motor_stop()
except KeyboardInterrupt:
    pass        

