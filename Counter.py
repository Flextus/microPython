from machine import Pin 
from time import sleep

a=Pin(2,Pin.OUT)
b=Pin(15,Pin.OUT)
c=Pin(22,Pin.OUT)
d=Pin(21,Pin.OUT)
e=Pin(19,Pin.OUT)
f=Pin(4,Pin.OUT)
g=Pin(5,Pin.OUT)
t=(0.5)

tabla = ['1111110','0110000','1101101','1111001','01100111','1011011','1011111','1110000','1111111','1111011']

def despliega (n):
    a.value(int(tabla[n][0]))
    b.value(int(tabla[n][1]))
    c.value(int(tabla[n][2]))
    d.value(int(tabla[n][3]))
    e.value(int(tabla[n][4]))
    f.value(int(tabla[n][5]))
    g.value(int(tabla[n][6]))
  
contador=0
while (1):
    despliega(contador)
    sleep(t)
    contador=contador+1
    if (contador > 9 ):
        contador = 0