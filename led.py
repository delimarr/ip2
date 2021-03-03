#import RPi.GPIO as GPIO
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

#import time
#from random import randint

class Led():
    def __init__(self):
        self.pixelClock = 11
        self.pixelDout = 10
        self.pixels = None

    def configure(self, pixelCount = 56):        
        self.pixels = Adafruit_WS2801.WS2801Pixels(pixelCount, clk = self.pixelClock, do = self.pixelDout)
        
    def fill(self, red = 0, green = 0, blue = 0):
        self.pixels.clear()
        for i in range(self.pixelCount):
            self.pixels.set_pixel_rgb(i, red, green, blue)
        self.pixels.show()
        
    def light(self, pos = 0, red = 0, green = 0, blue = 0):
        self.pixels.set_pixel_rgb(pos, red, green, blue)
        self.pixels.show()

    # POST: takes a player object
    # PAST: lights LEDs according to visited street and map
    def lightMap(self, player):
        #TODO: light led according to visited street -> Parse player position to LED using a lookup table
        #check led example in main branch
        return




'''    def blink(self):
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
'''        
