from machine import Pin, UART, ADC
import time

serial = UART(2, 9600)
joyx = ADC(Pin(15))
# joyy = ADC(Pin(2))
# joyp = ADC(Pin(4))
#int x1, y1, p1

while True:
    
    x = int(joyx.read() // 32)
    
    if (True):
        print(x)
        time.sleep(0.1)