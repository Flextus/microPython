from machine import Pin, ADC, UART
from time import sleep
import esp32


x = ADC (Pin(13))
y = ADC (Pin(12))
joy = Pin(14, Pin.IN)

while True:
    x = x.read()
    y = y.read()
    R3 = joy.read()
    

    
    