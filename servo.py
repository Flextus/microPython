from machine import Pin, PWM
import time

class servo:
    #Atributos
    Pinx = 0
    Ciclo = 0
    
    #Metodos
    def __init__ (self, pin): #Pin es el pin donde se trabajara
        self.Pinx = PWM(Pin(pin), freq = 50, duty = 0)
        
    def set_Angle (self, angulo):
        self.Ciclo = int((angulo - 0) * (120 - 20) / (100 - 0))
        self.Pinx.duty(self.Ciclo)
        
        
        
