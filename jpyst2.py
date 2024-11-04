from machine import Pin, ADC
import time

xp = ADC(Pin(15))
xp.atten(xp.ATTN_11DB)
yp = ADC(Pin(2))
yp.atten(yp.ATTN_11DB)


while True:
    
    x = xp.read()
    y = yp.read()
    
    print("x = ", x)
    print("y = ", y)
    time.sleep_ms(200)
    