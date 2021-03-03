import RPi.GPIO as GPIO
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI
import time
from random import randint

class LedStripe():
    def __init__(self):
        self.pixelClock = 11
        self.pixelDout = 10
        self.pixelCount = 40
        self.pixels = None

    def makePixels(self):        
        self.pixels = Adafruit_WS2801.WS2801Pixels(self.pixelCount, clk = self.pixelClock, do = self.pixelDout)
        
    def fill(self, r = 0, g = 0, b = 0):
        self.pixels.clear()
        self.pixels.show()
        for i in range(self.pixelCount):
            self.pixels.set_pixel_rgb(i, r, g, b)
        self.pixels.show()
        
    def light(self, p = 0, r = 0, g = 0, b = 0):
        self.pixels.set_pixel_rgb(p, r, g, b)
        self.pixels.show()

    def blink(self):
        while True:
            for i in range(self.pixelCount):
                self.light(i, r = 255)
                #time.sleep(1)
                self.light(i, g = 255)
               # time.sleep(1)
                self.light(i, b = 255)
            #time.sleep(1)
                
    def ecal(self):
        while True:
            self.light(randint(0,39), r = randint(0,255), g=randint(0,255), b=randint(0, 255))
