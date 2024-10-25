from machine import Pin, PWM
import time
led = PWM(Pin(2), freq = 4000000, duty = 0) #PWM es SOLO salida
#usa el PWM como salida en el Pin 2 |
#duty es el porcentaje del tiempo del ciclo donde hay voltaje
#va de 0 a 1024
x = 0
while True:
    
    while x < 1019:
        led.duty(x)
        time.sleep(0.05)
        x += 20
        
    while x > 10:
        led.duty(x)
        time.sleep(0.05)
        x -= 20