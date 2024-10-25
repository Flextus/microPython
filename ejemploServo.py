from machine import Pin, PWM
import time
from servo import servo

servo1 = servo(23)
servo1.set_Angle(35)

while True:
    servo1.set_Angle(0)
    time.sleep(.5)
    print("0")
    servo1.set_Angle(45)
    time.sleep(.5)
    print("45")
    servo1.set_Angle(90)
    time.sleep(.5)
    print(90)
    servo1.set_Angle(135)
    time.sleep(.5)
    print(135)
    servo1.set_Angle(180)
    time.sleep(.5)
    print(180)