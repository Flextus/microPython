from machine import Pin, PWM, UART
led = PWM(Pin(2), freq = 4000000, duty = 0) 
serial = UART(2, 9600)

while True:
    if serial.any() > 0: 
        mensaje = serial.read()
        mensaje = int(mensaje)
        print(mensaje)
        mensaje = int(mensaje)
        led.duty(mensaje)
        
    