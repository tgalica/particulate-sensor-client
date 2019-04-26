from RgbLed import RgbLed
from time import sleep
import board

class ledTest:
    led = RgbLed(board.D2,board.D3,board.D4)
    led.turnOn(True, True, True)
    sleep(1)
    led.turnOn(True, False, False)
    sleep(1)
    led.turnOn(False, True, False)
    sleep(1)
    led.turnOn(False, False, True)
    sleep(1)
    led.turnOff
    