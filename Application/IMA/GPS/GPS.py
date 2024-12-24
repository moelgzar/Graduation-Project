import gpsd
import time

# Connect to the local gpsd
gpsd.connect()

# Function to get GPS data
def get_gps_data():
    packet = gpsd.get_current()
    if packet.mode >= 2:  # Check if GPS fix is available
        return packet
    else:
        return None

# Example usage
while True:
    vehicle1_data = get_gps_data()  # Get GPS data for vehicle 1
    vehicle2_data = get_gps_data()  # Get GPS data for vehicle 2

    if vehicle1_data and vehicle2_data:
        # Assuming you have latitude, longitude, and speed attributes in the GPS data
        print("Vehicle 1 - Latitude: {}, Longitude: {}, Speed: {} m/s".format(vehicle1_data.lat, vehicle1_data.lon, vehicle1_data.speed))
        print("Vehicle 2 - Latitude: {}, Longitude: {}, Speed: {} m/s".format(vehicle2_data.lat, vehicle2_data.lon, vehicle2_data.speed))

    time.sleep(1)  # Wait for 1 second before getting the next GPS data