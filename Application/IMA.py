import time
import threading
import lcd 
import buzzer 
import carmotors
import gps  

#Initialize system components
def IMA_init():

    carmotors.motors_init()


class GPS:
    def get_location(self):
        # Simulate GPS data
        return (latitude, longitude)

class LCD:
    def display_message(self, message):
        # Display message on LCD
        print("warning")

class Buzzer:
    def emit_sound(self):
        # Activate buzzer
        print("Beep!")
        

    def update_location(self, latitude, longitude):
        self.location = (latitude, longitude)

def compare_speed(vehicle1, vehicle2):
    if vehicle1.speed < vehicle2.speed:
        return f"Vehicle {vehicle1.id} is traveling slower than Vehicle {vehicle2.id}"
    elif vehicle1.speed > vehicle2.speed:
        return f"Vehicle {vehicle1.id} is traveling faster than Vehicle {vehicle2.id}"
    else:
        return f"Vehicle {vehicle1.id} and Vehicle {vehicle2.id} are traveling at the same speed"

def intersection_movement_assist(vehicle1, vehicle2, gps, lcd, buzzer):
    while True:
        # Get GPS data
        lat1, long1 = gps.get_location()
        lat2, long2 = gps.get_location()

        # Update vehicle locations
        vehicle1.update_location(lat1, long1)
        vehicle2.update_location(lat2, long2)

        # Compare speeds
        speed_comparison = compare_speed(vehicle1, vehicle2)
        lcd.display_message(speed_comparison)

        # If speeds are significantly different, emit sound alert
        if abs(vehicle1.speed - vehicle2.speed) > threshold:
            buzzer.emit_sound()

        time.sleep(1)  # Update every second

# Initialize hardware components
gps = GPS()
lcd = LCD()
buzzer = Buzzer()

# Initialize vehicles
vehicle1 = Vehicle(id=1, speed=15)  # Vehicle 1 traveling at 15 m/s
vehicle2 = Vehicle(id=2, speed=20)  # Vehicle 2 traveling at 20 m/s

# Set up intersection movement assist thread
ima_thread = threading.Thread(target=intersection_movement_assist, args=(vehicle1, vehicle2, gps, lcd, buzzer))
ima_thread.start()