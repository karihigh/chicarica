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
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.solid import Solid

# neotrellis buttons
button_LED = DigitalInOut(board.D13)
button_LED.direction = Direction.OUTPUT
button_LED.value = True

# assign board pin number to strip
pixel_pin = board.D5
# 31 each bar, 89 big strip = 271
num_pixels = 271

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
RED = (255, 0, 5)
YELLOW = (255, 150, 0)
ORANGE = (255, 40, 0)
GREEN = (0, 255, 0)
TEAL = (0, 255, 120)
CYAN = (0, 255, 240)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 240)
MAGENTA = (255, 0, 20)
WHITE = (200, 200, 200)
GOLD = (255, 222, 30)
PINK = (242, 90, 255)
AQUA = (50, 255, 255)
JADE = (0, 255, 60)
AMBER = (255, 100, 0)
WARM_WHITE = (253, 245, 230) 
COLD_WHITE = (230, 245, 253)
OFF = (0, 0, 0)

ORDER = neopixel.GRB

pixels.fill(BLUE) # este color es el default cuando se prende
pixels.show()

#set strip groups
def set_bar1(color):
    for index in range(31):
        pixels[index] = color
    pixels.show()

def set_bar2(color):
    for index in range(31, 62):
        pixels[index] = color
    pixels.show()

def set_bar3(color):
    for index in range(62, 93):
        pixels[index] = color
    pixels.show()

def set_strip1(color):
    for index in range(93, 182):
        pixels[index] = color
    pixels.show()

def set_strip2(color):
    for index in range(182, 271):
        pixels[index] = color
    pixels.show()

#hermoso final - bpm=89, 0.6742
hf_solid = Solid(pixels, color=ORANGE)
hf_pulse1 = Pulse(pixels, speed=0.00001, color=PINK, period=6.742)
hf_pulse2 = Pulse(pixels, speed=0.00001, color=ORANGE, period=6.742)
hf_pulse = AnimationSequence(hf_pulse1, hf_pulse2, advance_on_cycle_complete=True, auto_reset=True, auto_clear=True)

#dale mami - bpm=98, 0.6122
dm_solid = Solid(pixels, color=RED)

#arde lento - bpm=130, 0.4615
al_comet = Comet(pixels, speed=0.04615, color=RED, tail_length=31, bounce=True)
al_cycle = ColorCycle(pixels, 0.04615, colors=[ORANGE, RED])

#ay tentacion - bpm=142, 0.4225 (fast = 0.1056)
at_solid = Solid(pixels, color=PURPLE)

#diamantes - bpm=80, 0.75
d_chase = Chase(pixels, speed=0.075, size=3, spacing=10, color=WHITE)
d_pulse1 = Pulse(pixels, speed=0.00001, color=BLUE, period=0.75)
d_pulse2 = Pulse(pixels, speed=0.00001, color=WHITE, period=0.75)
d_pulse = AnimationSequence(d_pulse1, d_pulse2, advance_on_cycle_complete=True, auto_reset=True, auto_clear=True)

#mirada bella - bpm=114, 0.4225
mb_pulse = Pulse(pixels, speed=0.00001, color=AQUA, period=4.225)

#invierno - bpm=137, 0.438
i_solid = Solid(pixels, color=CYAN)
i_comet = Comet(pixels, speed=0.0438, color=ORANGE, tail_length=31, bounce=True)

#no pide rescate - bpm=90, 0.667
np_pulse1 = Pulse(pixels, speed=0.00001, color=PURPLE , period=1.3333)
np_pulse2 = Pulse(pixels, speed=0.00001, color=JADE , period=1.3333)
np_pulse = AnimationSequence(np_pulse1, np_pulse2, advance_on_cycle_complete=True, auto_reset=True, auto_clear=True)

#saico - bpm=80, 0.5
s_colorcycle = ColorCycle(pixels, 0.5, colors=[JADE, MAGENTA])


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

# effectos
def blinkwrite(boton):

    if boton == 0:
        hf_solid.animate()

    elif boton == 1:
        hf_pulse.animate()

    elif boton == 2:
        dm_solid.animate()

    elif boton == 5:
        al_comet.animate()

    elif boton == 6:
        al_cycle.animate()

    elif boton == 3:
        at_solid.animate()

    elif boton == 4:
        pixels.fill(OFF)
        set_bar1(PURPLE)
        time.sleep(0.1056)
        pixels.fill(OFF)
        set_bar2(ORANGE)
        time.sleep(0.1056)
        pixels.fill(OFF)
        set_bar3(PURPLE)
        time.sleep(0.1056)
        pixels.fill(OFF)
        set_strip1(ORANGE)
        time.sleep(0.1056)
        pixels.fill(OFF)
        set_strip2(PURPLE)
        time.sleep(0.1056)

    elif boton == 7:
        d_chase.animate()

    elif boton == 8:
        d_pulse.animate()

    elif boton == 9:
        mb_pulse.animate()

    elif boton == 10:
        i_solid.animate()

    elif boton == 11:
        i_comet.animate()

    elif boton == 12:
        np_pulse.animate()

    elif boton == 13:
        pixels.fill(OFF)
        set_bar1(WHITE)
        time.sleep(0.0667)
        pixels.fill(OFF)
        set_bar2(WHITE)
        time.sleep(0.0667)
        pixels.fill(OFF)
        set_bar3(WHITE)
        time.sleep(0.0667)
        pixels.fill(OFF)
        set_strip1(WHITE)
        time.sleep(0.0667)
        pixels.fill(OFF)
        set_strip2(WHITE)
        time.sleep(0.0667)

    elif boton == 14:
        s_colorcycle.animate()

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
    trellis.pixels[0] = MAGENTA
    trellis.pixels[1] = MAGENTA
    trellis.pixels[2] = RED
    trellis.pixels[3] = PURPLE
    trellis.pixels[4] = PURPLE
    trellis.pixels[5] = ORANGE
    trellis.pixels[6] = ORANGE
    trellis.pixels[7] = WHITE
    trellis.pixels[8] = WHITE
    trellis.pixels[9] = AQUA
    trellis.pixels[10] = ORANGE
    trellis.pixels[11] = ORANGE
    trellis.pixels[12] = JADE
    trellis.pixels[13] = JADE
    trellis.pixels[14] = MAGENTA
    trellis.pixels[15] = OFF
    time.sleep(.05)

print("Cajita Chicarica is on")

while True:
    trellis.sync()
    blinkwrite(boton)
    time.sleep(.02)
