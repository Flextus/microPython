from machine import Pin, UART, ADC
import time
led = Pin(2, Pin.OUT)
serial = UART(2, 9600)
controladorPotencia = ADC(Pin(32))


while True:
    
    x = controladorPotencia.read() // 16 #divide solo enteros
    print(x)
    serial.write(x.to_bytes(2, "big"))
    time.sleep(0.01)