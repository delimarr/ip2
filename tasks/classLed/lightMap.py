# author:
# General conventions:
#       - functions, variables: firstLetterLowerCase
#       - class: FirstLetterCapital
#       - constant: CAPITAL
#############################################################################

'''
Doc: your remarks, ideas
'''

import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI
# import RPi.GPIO as GPIO

# POST: takes a player object
# PAST: lights LEDs according to visited street and map

def lightMap(self, player):
    #TODO: light led according to visited street -> Parse player position to LED using a lookup table
    #check led example in main branch
    return