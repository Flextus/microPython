from machine import Pin
import time

led_pins = [15, 2, 4, 5, 18, 19, 21, 22]
leds = [Pin(pin, Pin.OUT) for pin in led_pins]

while True:
    for led in leds:
        led.value(1)         
        time.sleep(.1)        
        led.value(0)        
    
    for led in reversed(leds):
        led.value(1)         
        time.sleep(.1)        
        led.value(0)         