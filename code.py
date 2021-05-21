# Cajita Chicarica
# NeoTrellis to select colors of NeoPixel strip
# NeoTrellis connected to Feather M4
# NeoPixel 136 strip connected to pin D5
# My version

import time
import board
from board import SCL, SDA
import busio
import neopixel
from adafruit_neotrellis.neotrellis import NeoTrellis
from digitalio import DigitalInOut, Direction

# adafruit animations
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.colorcycle import ColorCycle

# neotrellis buttons
button_LED = DigitalInOut(board.D13)
button_LED.direction = Direction.OUTPUT
button_LED.value = True

# assign board pin number to strip
pixel_pin = board.D5
# 31 each bar, 89 big strip = 279
num_pixels = 279

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False)
unpixel = pixels[1]
print(unpixel)

# create the i2c object for the trellis
i2c_bus = busio.I2C(SCL, SDA)

# create the trellis object
trellis = NeoTrellis(i2c_bus)
boton = 17
count = 0

# color definitions
# (r 0-255, g 0-255, b 0-255)
RED = (255, 0, 5)
YELLOW = (255, 150, 0)
ORANGE = (255, 40, 0)
GREEN = (0, 255, 0)
TEAL = (0, 255, 120)
CYAN = (0, 255, 240)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
MAGENTA = (255, 0, 20)
WHITE = (200, 200, 200)
GOLD = (255, 222, 30)
PINK = (242, 90, 255)
AQUA = (50, 255, 255)
JADE = (0, 240, 45)
AMBER = (255, 100, 0)
WARM_WHITE = (253, 245, 230) 
COLD_WHITE = (230, 245, 253)

OFF = (0, 0, 0)

ORDER = neopixel.GRB

pixels.fill(RED)  # este color es el default cuando se prende
pixels.show()


#No pide rescate - bpm=90, 0.667

npd_blink = Blink(pixels, speed=0.0667, color=PURPLE)
npd_sparkle_purple = Sparkle(pixels, speed=0.0667, color=PURPLE, num_sparkles=6)
npd_sparkle_jade = Sparkle(pixels, speed=0.0667, color=JADE, num_sparkles=6)
npd_comet = Comet(pixels, speed=0.0000000667, color=PURPLE, tail_length=60, bounce=True)

#Diamantes - bpm=80, 0.75
d_blink = Blink(pixels, speed=0.75, color=RED)
d_colorcycle = ColorCycle(pixels, speed=0.75, colors=((0, 255, 240), (255, 0, 0)), name=None)
d_colorcycle_half = ColorCycle(pixels, speed=0.075, colors=((0, 255, 240), (255, 0, 0)), name=None)

strobe = Blink(pixels, speed=0.0667, color=WHITE)

pulse = Pulse(pixels, speed=0.1, color=YELLOW, period=5)

sparkle = Sparkle(pixels, speed=0.01, color=PURPLE, num_sparkles=3)
comet = Comet(pixels, speed=0.001, color=PURPLE, tail_length=5, bounce=False)
colorcycle = ColorCycle(pixels, speed=1, colors=((255, 0, 0), (0, 255, 0)), name=None)


# listener DO NOT TOUCH
def blinkread(event):
    if event.number == 0:
        global boton
        boton = 0
    elif event.number == 1:
        global boton
        boton = 1
    elif event.number == 2:
        global boton
        boton = 2
    elif event.number == 3:
        global boton
        boton = 3
    elif event.number == 4:
        global boton
        boton = 4
    elif event.number == 5:
        global boton
        boton = 5
    elif event.number == 6:
        global boton
        boton = 6
    elif event.number == 7:
        global boton
        boton = 7
    elif event.number == 8:
        global boton
        boton = 8
    elif event.number == 9:
        global boton
        boton = 9
    elif event.number == 10:
        global boton
        boton = 10
    elif event.number == 11:
        global boton
        boton = 11
    elif event.number == 12:
        global boton
        boton = 12
    elif event.number == 13:
        global boton
        boton = 13
    elif event.number == 14:
        global boton
        boton = 14
    elif event.number == 15:
        global boton
        boton = 15

# effectOS DE LAS BARRITAS
def blinkwrite(boton):
    '''
    if boton == 14:
        print("zero")
        # ARCOIRIS
        def wheel(pos):

            if pos < 0 or pos > 255:
                r = g = b = 0
            elif pos < 85:
                r = int(pos * 3)
                g = int(255 - pos*3)
                b = 0
            elif pos < 170:
                pos -= 85
                r = int(255 - pos*3)
                g = 0
                b = int(pos*3)
            else:
                pos -= 170
                r = 0
                g = int(pos * 3)
                b = int(255 - pos*3)
            return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)

        def rainbow_cycle(wait):
            global count
            for j in range(255):
                if count < num_pixels:
                    pixel_index = (count * 256 // num_pixels) + j
                    pixels[count] = wheel(pixel_index & 255)
                    count += 1
                    if count >= num_pixels:
                        count = 0
                pixels.show()
                time.sleep(wait)
        rainbow_cycle(0.01)    # rainbow cycle with 1ms delay per step
    '''
    if boton == 0:
        pixels.fill(JADE)
        pixels.show()

    elif boton == 1:
        npd_sparkle_purple.animate()

    elif boton == 2:
        npd_blink.animate()

    elif boton == 3:
        pixels.fill(PURPLE)
        pixels.show()

    elif boton == 4:
        npd_sparkle_jade.animate()

    elif boton == 5:
        pixels.fill(CYAN)
        pixels.show()

    elif boton == 6:
        pixels.fill(RED)
        pixels.show()
        """
        def gradient(color_one, color_two, blend_weight):
            
            #Blend between two colors with a given ratio.
            #:param color_one:  first color, as an (r,g,b) tuple
            #:param color_two:  second color, as an (r,g,b) tuple
            #:param blend_weight: Blend weight (ratio) of second color, 0.0 to 1.0
            
            if blend_weight < 0.0:
                blend_weight = 0.0
            elif blend_weight > 1.0:
                blend_weight = 1.0
            initial_weight = 1.0 - blend_weight
            return (int(color_one[0] * initial_weight + color_two[0] * blend_weight),
                    int(color_one[1] * initial_weight + color_two[1] * blend_weight),
                    int(color_one[2] * initial_weight + color_two[2] * blend_weight))
        gradient(RED, CYAN, 0.1)
        """
    elif boton == 7:
        d_colorcycle.animate()

    elif boton == 8:
        d_colorcycle_half.animate()

    elif boton == 9:
        d_blink.animate()

    elif boton == 10:
        pixels.fill(ORANGE)
        pixels.show()

    elif boton == 11:
        pixels.fill(PINK)
        pixels.show()

    elif boton == 12:
        pixels.fill(MAGENTA)
        pixels.show()

    elif boton == 13:
        pixels.fill(WARM_WHITE)
        pixels.show()

    elif boton == 14:
        strobe.animate()

    elif boton == 15:
        pixels.fill(OFF)
        pixels.show()

# el brillo de todos los botones en la cajita, puede ser de 0 a 1
trellis.pixels.brightness = 0.5

for i in range(16):
    trellis.activate_key(i, NeoTrellis.EDGE_RISING)
    trellis.activate_key(i, NeoTrellis.EDGE_FALLING)
    # print(trellis.callbacks[i])
    trellis.callbacks[i] = blinkread
    # estos son los colores de los botones (no las barritas)
    trellis.pixels[0] = JADE
    trellis.pixels[1] = PURPLE
    trellis.pixels[2] = JADE
    trellis.pixels[3] = PURPLE
    trellis.pixels[4] = JADE
    trellis.pixels[5] = CYAN
    trellis.pixels[6] = RED
    trellis.pixels[7] = CYAN
    trellis.pixels[8] = RED
    trellis.pixels[9] = CYAN
    trellis.pixels[10] = ORANGE
    trellis.pixels[11] = PINK
    trellis.pixels[12] = MAGENTA
    trellis.pixels[13] = WARM_WHITE
    trellis.pixels[14] = COLD_WHITE
    trellis.pixels[15] = OFF
    time.sleep(.05)

print("Cajita Chicarica is on")

while True:
    trellis.sync()
    blinkwrite(boton)
    time.sleep(.02)
