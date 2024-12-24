import RPi.GPIO as GPIO
import time

# Define motor pins
motor1_pins = [11, 13, 15]  # Motor 1: ENA, IN1, IN2
motor2_pins = [16, 18, 22]  # Motor 2: ENB, IN3, IN4
motor3_pins = [29, 31, 33]  # Motor 3: ENC, IN5, IN6
motor4_pins = [32, 36, 38]  # Motor 4: END, IN7, IN8


# Set up motor pins
def motors_init():
# Set GPIO mode
    GPIO.setmode(GPIO.BCM)

    for pins in [motor1_pins, motor2_pins, motor3_pins, motor4_pins]:
        GPIO.setup(pins[0], GPIO.OUT)  # Enable pin
        GPIO.setup(pins[1], GPIO.OUT)  # Input 1
        GPIO.setup(pins[2], GPIO.OUT)  # Input 2


# Set the initial car speed 
def car_set_speed(motor_pins, speed):
    GPIO.output(motor_pins[0], GPIO.HIGH)  # Enable motor
    pwm = GPIO.PWM(motor_pins[0], 100)  # Create PWM object
    pwm.start(speed)  # Start PWM with given speed
    return pwm


#set the car direction
def car_set_direction(motor_pins, direction):
    if direction == 'forward':
        GPIO.output(motor_pins[1], GPIO.HIGH)
        GPIO.output(motor_pins[2], GPIO.LOW)
    elif direction == 'backward':
        GPIO.output(motor_pins[1], GPIO.LOW)
        GPIO.output(motor_pins[2], GPIO.HIGH)


def stop_motor(pwm):
    pwm.stop()


# move the car forward with a specific initial speed
def car_move_forward(initial_speed):
    motors_pwm = []
    for pins in [motor1_pins, motor2_pins, motor3_pins, motor4_pins]:
        pwm = car_set_speed(pins, initial_speed)
        motors_pwm.append(pwm)
        car_set_direction(pins, 'forward')
    return motors_pwm


# Function to decrease speed gradually
def car_decrease_speed(motors_pwm, decrement):
    for pwm in motors_pwm:
        current_speed = pwm._get_pwm().get('duty_cycle')
        new_speed = max(0, current_speed - decrement)
        pwm.ChangeDutyCycle(new_speed)


# Function to move with gradual speed changes
def car_gradual_speed_change(initial_speed, final_speed, time_to_change):
    step = 1 if initial_speed < final_speed else -1
    change_steps = abs(final_speed - initial_speed)
    delay = time_to_change / change_steps
    current_speed = initial_speed

    motors_pwm = car_move_forward(current_speed)
    time.sleep(1)  # Initial delay before speed change

    for _ in range(change_steps):
        car_decrease_speed(motors_pwm, 1)
        current_speed += step
        time.sleep(delay)

    return motors_pwm


# Function to stop the car
def stop_car(motors_pwm):
    for pwm in motors_pwm:
        stop_motor(pwm)


# Example usage
if __name__ == "__main__":
    initial_speed = 50  # Set initial speed to 50%
    final_speed = 20  # Set final speed to 20%
    time_to_change = 3  # Time to change speed from initial to final (in seconds)

    motors_pwm = car_gradual_speed_change(initial_speed, final_speed, time_to_change)

    # Keep the car moving for 5 seconds
    time.sleep(5)

    # Stop the car
    stop_car(motors_pwm)

    # Clean up GPIO
    GPIO.cleanup()



