import board
import RPi.GPIO as GPIO

class RgbLed:
    def __init__(self, redPin, greenPin, bluePin):
        self.redPin = redPin
        self.bluePin = bluePin
        self.greenPin = greenPin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.redPin, GPIO.OUT)
        GPIO.setup(self.greenPin, GPIO.OUT)
        GPIO.setup(self.bluePin, GPIO.OUT)


    def turnOn(self, red=False, green=False, blue=False):
        if red:
            GPIO.output(self.redPin, GPIO.LOW)
        else:
            GPIO.output(self.redPin, GPIO.HIGH)
        if blue:
            GPIO.output(self.bluePin, GPIO.LOW)
        else:
            GPIO.output(self.bluePin, GPIO.HIGH)
        if green:
            GPIO.output(self.greenPin, GPIO.LOW)
        else:
            GPIO.output(self.greenPin, GPIO.HIGH)
        
            
    def turnOff(self):
        GPIO.output(self.greenPin, GPIO.HIGH)
        GPIO.output(self.bluePin, GPIO.HIGH)
        GPIO.output(self.redPin, GPIO.HIGH)

    def red(self):
        self.turnOn(True, False, False)
    
    def blue(self): 
        self.turnOn(False, False, True)

    def green(self):
        self.turnOn(False, True, False)
    
    def yellow(self):
        self.turnOn(True, True, False)
    
    def cyan(self): 
        self.turnOn(False, True, True)

    def magenta(self):
        self.turnOn(True, False, True)
    
    def white(self):
        self.turnOn(True, True, True)
