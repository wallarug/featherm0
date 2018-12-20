Welcome to CircuitPython!
#############################

Visit the Feather M0 product page here for more info: 
                              https://adafruit.com/product/2772

To get started with CircuitPython, which comes built into your Feather, visit:
    https://learn.adafruit.com/welcome-to-circuitpython

#############################

The Feather Basic has a very tiny disk drive so we have disabled Mac OS X 
indexing which could take up that valuable space. 

So *please* do not remove the empty .fseventsd/no_log, .metadata_never_index 
or .Trashes files! 

#############################

The pre-loaded demo shows off what your Feather M0 can do with CircuitPython:

  * Pin A0 is a true analog output, you will see the voltage slowly rise

  * Pin A1 is an analog input, the REPL will display the voltage on this pin 
    (0-3.3V is the max range)

  * Pin A5 is a capacitive input, when touched, it will turn on the red LED. 

  * Pin D5 is a digital input with a pull-up, you can touch this pad to GND
    to activate the button (or wire up a tactile button or switch!)
    If you update main.py to uncomment the relevant lines, it will act as a 
    mini keyboard and emulate an 'a' key-press whenever D5 is grounded.

  * Pin D6 is a NeoPixel output, you can wire up a strip of NeoPixels to this
    pin (power from USB and GND). The first 16 NeoPixel will rainbow swirl

  * Pin D9 can be connected to a servo which will sweep back and forth. Power
    the servo from 5V and GND.

For more details on how to use CircuitPython, visit 
https://adafruit.com/product/2772 and check out all the tutorials we have!

#############################
CircuitPython Quick Start:

Changing the code is as easy as editing main.py in your favorite text editor. 

Our recommended editor is Mu, which is great for simple projects, and comes
with a built in REPL serial viewer! It is available for Mac, Windows & Linux
https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor

After the file is saved, CircuitPython will automatically reload the latest 
code. Try enabling the single-button keyboard!
         (HINT: look for the "# optional! uncomment below..." text)

Connecting to the serial port will give you access to sensor information, 
better error messages and an interactive CircuitPython (known as the REPL). 
On Windows we recommend Mu, Tera Term or PuTTY. 
On Mac OSX and Linux, use Mu or 'screen' can be used from a terminal.