from machine import Pin, UART
led = Pin(2, Pin.OUT)
serial = UART(2, 9600)

while True:
    if serial.any() > 0: 
        mensaje = serial.read() #manda un mensaje 
        print(mensaje)
        
        if mensaje == b'on':    #la b significa que el valor recibido es un byte
            led.on()
            serial.write("e");
            
        elif mensaje == b'off':
            led.off()
            serial.write("a")
            
        else:
            serial.write("Dato invalido\n")
                       
       