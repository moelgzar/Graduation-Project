import gpsd

# Connect to the local GPSD daemon
gpsd.connect()

# Example usage: Read GPS data
try:
    # Get the GPS data
    packet = gpsd.get_current()

    # Check if the GPS data is valid
    if packet.mode >= 2:  # 2 means 2D fix, 3 means 3D fix
        # Retrieve the latitude and longitude
        latitude = packet.position()[0]
        longitude = packet.position()[1]
        print("Latitude:", latitude)
        print("Longitude:", longitude)

        # Retrieve the speed in meters per second
        speed = packet.speed()
        print("Speed:", speed, "m/s")

    else:
        print("No GPS fix available.")

except KeyboardInterrupt:
    pass

finally:
    # Close the GPSD connection
    gpsd.close()