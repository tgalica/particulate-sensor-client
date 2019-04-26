from RgbLed import RgbLed
from time import sleep
import board

class ledTest:
    led = RgbLed(15,13,11)
    print ("white")
    led.turnOn(red=True, green=True, blue=True)
    sleep(1)
    print ("red")
    led.turnOn(red=True, green=False, blue=False)
    sleep(1)
    print ("green")
    led.turnOn(red=False, green=True, blue=False)
    sleep(1)
    print ("blue")
    led.turnOn(red=False, green=False, blue=True)
    sleep(1)
    led.turnOff
    
