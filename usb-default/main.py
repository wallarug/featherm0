# Feather Basic IO demo
# Welcome to CircuitPython! :)

import time
import simpleio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogOut, AnalogIn
import touchio
import neopixel
import board

# Built in red LED
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# Analog output on A0
aout = AnalogOut(board.A0)

# Analog input on A1
analog1in = AnalogIn(board.A1)

# Capacitive touch on A5
touch = touchio.TouchIn(board.A5)

# Digital input with pullup on D5
button = DigitalInOut(board.D5)
button.direction = Direction.INPUT
button.pull = Pull.UP

# NeoPixel strip (of 16 LEDs) connected on D6
NUMPIXELS = 16
neopixels = neopixel.NeoPixel(board.D6, NUMPIXELS, brightness=0.2, auto_write=False)

# Servo on D9
servo = simpleio.Servo(board.D9)


# Used if we do HID output, see below
kbd = Keyboard()

######################### HELPERS ##############################

# Helper to convert analog input to voltage
def getVoltage(pin):
    return (pin.value * 3.3) / 65536

# Helper to give us a nice color swirl
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0) or (pos > 255):
        return (0, 0, 0)
    if pos < 85:
        return (int(255 - pos*3), int(pos*3), 0)
    elif pos < 170:
        pos -= 85
        return (0, int(255 - (pos*3)), int(pos*3))
    else:
        pos -= 170
        return (int(pos*3), 0, int(255 - pos*3))

######################### MAIN LOOP ##############################

i = 0
while True:
  # make the neopixels swirl around
  for p in range(NUMPIXELS):
      idx = int ((p * 256 / NUMPIXELS) + i)
      neopixels[p] = wheel(idx & 255)
  neopixels.show()

  # set analog output to 0-3.3V (0-65535 in increments)
  aout.value = i * 256

  # Read analog voltage on A1
  print("A1: %0.2f" % getVoltage(analog1in))

  # use A5 as capacitive touch to turn on internal LED
  if touch.value:
      print("A5 touched!")
  led.value = touch.value

  if not button.value:
      print("Button on D5 pressed!")
      # optional! uncomment below & save to have it sent a keypress
      #kbd.press(Keycode.A)
      #kbd.release_all()

  # sweep a servo from 0-180 degrees (map from 0-255)
  servo.angle = simpleio.map_range(i, 0, 255, 0, 180)

  i = (i+1) % 256  # run from 0 to 255
  #time.sleep(0.01) # make bigger to slow down
