from machine import ADC, Pin, UART
import time

serial = UART(2, 9600)
xAxis = ADC(Pin(15, Pin.IN)) # create an ADC object acting on a pin
xAxis.atten(xAxis.ATTN_11DB)
yAxis = ADC(Pin(2, Pin.IN)) # create an ADC object acting on a pin
yAxis.atten(yAxis.ATTN_11DB)
press = Pin(4, Pin.IN, Pin.PULL_UP)

while True:
    xValue = int(xAxis.read() // 16) 
    yValue = int(yAxis.read() // 16)  
    pressValue = press.value()
    time.sleep(0.1)
    
    if xValue > 116:
        serial.write(1)
        print("X Negativa")
    elif xValue < 116:
        serial.write(2)
        print("X Positiva")
    else:
        print("X NULL")
        
    if yValue < 91:
        serial.write(3)
        print("Y Negativa")
    elif yValue > 91:
        serial.write(4)
        print("Y Positiva")
    else:
        print("Y NULL")
        
    if (pressValue != 1):
        serial.write(5)
        print("RESET")
        
    if(True):
        print(f"X:{xValue}, Y:{yValue}, Button:{pressValue}")
        time.sleep(0.1)


        