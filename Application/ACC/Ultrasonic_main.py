import Ultrasonic

trig_pin = 13
echo_pin = 11

Ultrasonic.ultrasonic_init(trig_pin, echo_pin)

while True:
    distance = Ultrasonic.ultrasonic_calc_distance(trig_pin, echo_pin)
    print (f"Distance: {distance} cm") 