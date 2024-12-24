from RPLCD import CharLCD
import RPi.GPIO as GPIO

# Define LCD column and row size for 16x2 LCD
lcd_columns = 16
lcd_rows = 2

# Initialize LCD
lcd = CharLCD(
    pin_rs=7, pin_e=8,
    pins_data=[25, 24, 23, 18, 22, 27, 17, 4],
    numbering_mode=GPIO.BCM,
    cols=lcd_columns,
    rows=lcd_rows
)

# Write a message to the LCD
lcd.write_string('Hello, World!')

# Position the cursor on the second line
lcd.cursor_pos = (1, 0)

# Write another message
lcd.write_string('LCD with RPi B+')

# Clean up GPIO on exit
GPIO.cleanup()