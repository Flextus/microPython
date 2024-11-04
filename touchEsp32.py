from machine import Pin, TouchPad, PWM
import time

Led = PWM(Pin(2), freq = 4000, duty = 0)
touch1 = TouchPad(Pin(15))
touch2 = TouchPad(Pin(12))

ciclo = 0

while True:
    aux1 = touch1.read()
    aux2 = touch2.read()
    print("Ciclo en Bits", ciclo)
    print("Sensor 1", aux1)
    print("Sensor 2", aux2, "\n")
    Led.duty(ciclo)
    
    if aux1 < 300:
        ciclo += 50
        if ciclo > 1024:
            ciclo = 1023
    elif aux2 < 300:
        ciclo -= 50
        if ciclo < 0:
            ciclo = 0
    
    time.sleep(0.01)