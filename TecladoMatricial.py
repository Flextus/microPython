from machine import Pin
from kb4x4 import kb4x4
import time
teclado = kb4x4()
while True:
    boton = teclado.readkey()
    print("el boton es",boton)