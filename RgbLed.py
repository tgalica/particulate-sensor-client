import board
from digitalio import DigitalInOut, Direction

class RgbLed:
    def __init__(self, redPin, greenPin, bluePin):
        self.redPin = DigitalInOut(redPin)
        self.redPin.direction = Direction.OUTPUT
        self.bluePin = DigitalInOut(bluePin)
        self.bluePin.direction = Direction.OUTPUT
        self.greenPin = DigitalInOut(greenPin)
        self.greenPin.direction = Direction.OUTPUT


    def turnOn(self, red=False, green=False, blue=False):
            self.greenPin.value(green)
            self.bluePin.value(blue)
            self.redPin.value(red)
        
    def turnOff(self):
        self.bluePin.value(0)
        self.greenPin.value(0)
        self.redPin.value(0)