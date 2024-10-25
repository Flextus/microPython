from machine import Pin, PWM
import time

R = PWM (Pin (23), freq = 50, duty = 0)
G = PWM (Pin (22), freq = 50, duty = 0)
B = PWM (Pin (2), freq = 50, duty = 0)

while True:
    
    for r in range (0, 1024, 150):         #for de 0 a 1024, en pasos de 150
        for g in range (0, 1024, 100):
            for b in range (0, 1024, 50):
                
                R.duty(r)
                G.duty(g)
                B.duty(b)
                time.sleep(0.01)
    