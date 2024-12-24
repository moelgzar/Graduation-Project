import Led

pin_no = 18
delay_sec = 5

Led.Led_init(pin_no)

while True:
    Led.Led_warning(pin_no, delay_sec)
    
