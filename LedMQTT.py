from machine import Pin
import time
import WLAN
from umqtt.simple import MQTTClient

led = Pin(2, PIN.OUT)

#Tema y Broker
identificador = "1"
broker = "test.mosquitto.org" #Servidor Broker MQTT
tema = b'Luz_esp32'

#Conexion Wifi
ssid = "AMERIKE-ALUMNOS" #Nombre de la Red a conectar
password = "Alumnos123" #Contraseña de la red a conectar
WLAN.do_connect(ssid, password)

#Funcion para realizar el protocolo MQTT
def controlLed(topico, mensaje):
    print (mensaje [0])
    if (mensaje[0] == b'OFF'):
        led.off()
        cliente.publish(b'Luz_esp_conf',  b'OFF')
    elif(mensaje[0] == b'ON'):
        led.on()
        cliente.publish(b'Luz_esp_conf', b'ON')
        
#Suscripcion MQTT a Broker y Tema
cliente = MQTTClient(identificador, Broker)
cliente.setcallback(controlLed) #Funcion a llamar al recibir el mensaje
cliente.connect()
cliente.subscribe(tema)


#Funcion Principal checar mensaje cada 50ms
while True:
    cliente.check_msg()
    time.sleep_ms(50)







