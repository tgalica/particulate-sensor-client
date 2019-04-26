from RgbLed import RgbLed
from time import sleep
import board

class ledTest:
    led = RgbLed(board.D2,board.D3,board.D4)
    led.turnOn(red=True, green=True, blue=True)
    sleep(1)
    led.turnOn(red=True, green=False, blue=False)
    sleep(1)
    led.turnOn(red=False, green=True, blue=False)
    sleep(1)
    led.turnOn(red=False, green=False, blue=True)
    sleep(1)
    led.turnOff
    