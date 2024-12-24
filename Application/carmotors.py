import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)


IN1_A = 14  # Input 1
IN2_A= 15  # Input 2
ENA = 18  # Enable A (PWM)

IN1_B = 23  # Input 1
IN2_B = 24  # Input 2
ENB = 25

IN1_C = 8  # Input 1
IN2_C = 7  # Input 2
ENC = 1
 
IN1_D = 16  # Input 1
IN2_D = 20  # Input 2
END = 12 

def motor_init():
#Initialize the GPIO pins
    GPIO.setup(IN1_A, GPIO.OUT)
    GPIO.setup(IN2_A, GPIO.OUT)
    GPIO.setup(ENA, GPIO.OUT)

    GPIO.setup(IN1_B, GPIO.OUT)
    GPIO.setup(IN2_B, GPIO.OUT)
    GPIO.setup(ENB, GPIO.OUT)

    GPIO.setup(IN1_C, GPIO.OUT)
    GPIO.setup(IN2_C, GPIO.OUT)
    GPIO.setup(ENC, GPIO.OUT)

    GPIO.setup(IN1_D, GPIO.OUT)
    GPIO.setup(IN2_D, GPIO.OUT)
    GPIO.setup(END, GPIO.OUT)
#pwm
# Set the PWM frequency and initial duty cycle
    global pwm_A
    pwm_A = GPIO.PWM(ENA, 100)  # 100 Hz frequency
    pwm_A.start(0)  # 0% duty cycle

    global pwm_B
    pwm_B = GPIO.PWM(ENB, 100)  
    pwm_B.start(0)  

    global pwm_C
    pwm_C = GPIO.PWM(ENC, 100)  
    pwm_C.start(0)  

    global pwm_D
    pwm_D = GPIO.PWM(END, 100)  
    pwm_D.start(0)  



def set_motor_speed(speed):
    """
    Set the speed of the motor.
    :param speed: Speed in the range of 0 to 100.
    """
    if speed > 100:
        speed = 100
    elif speed < 0:
        speed = 0

    pwm_A.ChangeDutyCycle(speed)
    pwm_B.ChangeDutyCycle(speed)
    pwm_C.ChangeDutyCycle(speed)
    pwm_D.ChangeDutyCycle(speed)

def move_forward(speed):
    """
    Move the motor forward.
    :param speed: Speed in the range of 0 to 100.
    """
    GPIO.output(IN1_A, GPIO.HIGH)
    GPIO.output(IN2_A, GPIO.LOW)

    GPIO.output(IN1_B, GPIO.HIGH)
    GPIO.output(IN2_B, GPIO.LOW)

    GPIO.output(IN1_C, GPIO.HIGH)
    GPIO.output(IN2_C, GPIO.LOW)

    GPIO.output(IN1_D, GPIO.HIGH)
    GPIO.output(IN2_D, GPIO.LOW)
    set_motor_speed(speed)


def stop_motor():
    """
    Stop the motor.
    """
    pwm_A.stop()
    pwm_B.stop()
    pwm_C.stop()
    pwm_D.stop()

#def decrease_speed(speed, decrement):
   #pwm.ChangeDutyCycle(speed-decrement)

    
"""
# Example usage:
try:
    #motor_init()
    move_forward(50)  # Move forward at 50% speed
    time.sleep(2)     # Wait for 2 seconds
    set_motor_speed(30) #decrease speed from initial speed:50 to 30
    stop_motor()      # Stop the motor
    #time.sleep(1)     # Wait for 1 second
    #time.sleep(2)     # Wait for 2 seconds
    #stop_motor()      # Stop the motor

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    GPIO.cleanup()
"""



