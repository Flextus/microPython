from machine import ADC,Pin
import time

xAxis = ADC(Pin(15, Pin.IN)) # create an ADC object acting on a pin
xAxis.atten(xAxis.ATTN_11DB)
yAxis = ADC(Pin(2, Pin.IN)) # create an ADC object acting on a pin
yAxis.atten(yAxis.ATTN_11DB)
press = Pin(4, Pin.IN, Pin.PULL_UP)

while True:
    xValue = int(xAxis.read() // 16) # read a raw analog value in the range 0-4095
    yValue = int(yAxis.read() // 16)  # read a raw analog value in the range 0-4095
    pressValue = press.value()
    time.sleep(0.01)
    
    if (True):
            print(f"X:{xValue}, Y:{yValue}, Button:{pressValue}")
            time.sleep(0.1)
