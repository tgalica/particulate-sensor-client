from RgbLed import RgbLed
from time import sleep
import board

class ledTest:
    led = RgbLed(board.D17,board.D27,board.D22)
    led.turnOn(red=True, green=True, blue=True)
    sleep(1)
    led.turnOn(red=True, green=False, blue=False)
    sleep(1)
    led.turnOn(red=False, green=True, blue=False)
    sleep(1)
    led.turnOn(red=False, green=False, blue=True)
    sleep(1)
    led.turnOff
    