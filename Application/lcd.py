import os
import time

#path of device file
LCD_FILE = "/dev/lcd"

def write_to_lcd(data):

    with open(LCD_FILE, "w") as lcd_file:
        lcd_file.write(data)


def lcd_print_string(string):
     write_to_lcd(string)


def lcd_clear():
    write_to_lcd("0x01")

"""
# Example usage
if __name__ == "__main__":

    # Print a string on the LCD
    lcd_print_string("Hello, LCD!")

    # Wait for a while
    time.sleep(2)

    # Clear the LCD display
    lcd_clear()
"""