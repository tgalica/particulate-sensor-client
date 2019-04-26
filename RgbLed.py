import board
import RPI.GPIO as GPIO

class RgbLed:
    def __init__(self, redPin, greenPin, bluePin):
        self.redPin = redPin
        self.bluePin = bluePin
        self.greenPin = greenPin
        GPIO.setmode(GPIO.BOARD)
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