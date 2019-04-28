from RgbLed import RgbLed
from time import sleep
import board

class ledTest:
    led = RgbLed(17,27,22)
    print ("white")
    led.white()
    sleep(1)
    print ("red")
    led.red()
    sleep(1)
    print ("green")
    led.green()
    sleep(1)
    print ("blue")
    led.blue()
    sleep(1)
    led.turnOff
    
