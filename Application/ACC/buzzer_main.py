import buzzer

buzzer_pin = 23
delay_sec = 5

buzzer.buzzer_init(buzzer_pin)


buzzer.buzzer_warning(buzzer_pin, delay_sec)