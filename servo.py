from machine import Pin,PWM
import time

class Servo:
    #Atributos de la clase
    Pinx = 0
    Ciclo = 0
    inmin = 0
    inmax = 180
    outmin = 20
    outmax = 120
    
    #Constructor de la clase
    def __init__(self,pin):
        self.Pinx = PWM(Pin(pin), freq = 50, duty = 20)
    #Metodo de la clase
    def setAngle(self, angulo):
        self.Ciclo = int((angulo-self.inmin)*(self.outmax - self.outmin)/(self.inmax-self.inmin)+ self.outmin)
        self.Pinx.duty(self.Ciclo)


