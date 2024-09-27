from machine import Pin
from time import sleep

a = Pin(2, Pin.OUT)
b = Pin(15, Pin.OUT)
c = Pin(22, Pin.OUT)
d = Pin(21, Pin.OUT)
e = Pin(19, Pin.OUT)
f = Pin(4, Pin.OUT)
g = Pin(5, Pin.OUT)

boton = Pin(18, Pin.IN, pull=Pin.PULL_UP)

t = 0.5

tabla = [
    '1111110',  # 0
    '0110000',  # 1
    '1101101',  # 2
    '1111001',  # 3
    '0110011',  # 4 
    '1011011',  # 5
    '1011111',  # 6
    '1110000',  # 7
    '1111111',  # 8
    '1111011'   # 9
]

cuenta = False
pasado = boton.value() 

def despliega(n):
    a.value(int(tabla[n][0]))
    b.value(int(tabla[n][1]))
    c.value(int(tabla[n][2]))
    d.value(int(tabla[n][3]))
    e.value(int(tabla[n][4]))
    f.value(int(tabla[n][5]))
    g.value(int(tabla[n][6]))

contador = 0

while True:
    actual = boton.value()

    if pasado == 1 and actual == 0:
        cuenta = not cuenta
        sleep(0.2) 

    pasado = actual  

    if cuenta:
        despliega(contador)
        sleep(t)
        contador -= 1
        if contador < 0:
            contador = 9
    else:
        despliega(contador)
        sleep(t)
        contador += 1
        if contador > 9:
            contador = 0
