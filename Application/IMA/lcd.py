import RPi.GPIO as GPIO
import time

# Define GPIO pins for the LCD
LCD_RS = 7
LCD_E  = 8
LCD_D0 = 25
LCD_D1 = 24
LCD_D2 = 23
LCD_D3 = 18
LCD_D4 = 17
LCD_D5 = 27
LCD_D6 = 22
LCD_D7 = 10

# Define commands for the LCD
LCD_CLEAR_DISPLAY = 0x01
LCD_RETURN_HOME = 0x02
LCD_ENTRY_MODE_SET = 0x04
LCD_DISPLAY_CONTROL = 0x08
LCD_CURSOR_SHIFT = 0x10
LCD_FUNCTION_SET = 0x20
LCD_SET_CGRAM_ADDR = 0x40
LCD_SET_DDRAM_ADDR = 0x80

# Define LCD constants
LCD_LINE_1 = 0x80  # Address for the first line
LCD_LINE_2 = 0xC0  # Address for the second line
LCD_WIDTH = 16     # Number of characters per line

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup([LCD_RS, LCD_E, LCD_D0, LCD_D1, LCD_D2, LCD_D3, LCD_D4, LCD_D5, LCD_D6, LCD_D7], GPIO.OUT)

def lcd_pulse_enable():
    GPIO.output(LCD_E, GPIO.HIGH)
    time.sleep(0.0005)  # Wait for a short duration
    GPIO.output(LCD_E, GPIO.LOW)
    time.sleep(0.0005)  # Wait for a short duration

def lcd_send_byte(byte, is_data=True):
    GPIO.output(LCD_RS, GPIO.HIGH if is_data else GPIO.LOW)
    GPIO.output(LCD_D0, (byte & 0x01) >> 0)
    GPIO.output(LCD_D1, (byte & 0x02) >> 1)
    GPIO.output(LCD_D2, (byte & 0x04) >> 2)
    GPIO.output(LCD_D3, (byte & 0x08) >> 3)
    GPIO.output(LCD_D4, (byte & 0x10) >> 4)
    GPIO.output(LCD_D5, (byte & 0x20) >> 5)
    GPIO.output(LCD_D6, (byte & 0x40) >> 6)
    GPIO.output(LCD_D7, (byte & 0x80) >> 7)
    lcd_pulse_enable()

def lcd_send_command(command):
    lcd_send_byte(command, False)

def lcd_send_data(data):
    for char in data:
        lcd_send_byte(ord(char))

def lcd_init():
    lcd_send_command(0x38)  # 8-bit mode, 2 lines, 5x7 font
    lcd_send_command(0x0C)  # Display ON, Cursor OFF, Blink OFF
    lcd_send_command(0x06)  # Entry mode, auto-increment cursor

def lcd_clear():
    lcd_send_command(LCD_CLEAR_DISPLAY)
    time.sleep(0.002)  # Wait for clear to complete

def lcd_set_cursor(line, position):
    address = LCD_LINE_1 if line == 1 else LCD_LINE_2
    address += position
    lcd_send_command(address)

