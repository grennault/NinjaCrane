import time
import board
import digitalio
import storage, usb_cdc
import usb_hid
import usb_midi
from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_fr import KeyboardLayout # Clavier FR
from adafruit_hid.mouse import Mouse

# Instanciate Keyboard
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayout(keyboard)

# Instanciate Mouse
mouse = Mouse(usb_hid.devices)

time.sleep(5)
layout.write("I possess your keyboard and your mouse :) ")

def move_mouse_along(dir, step, repeat):
    if dir == "x":
        for _ in range(repeat):
            mouse.move(x=step)
    else:
        for _ in range(repeat):
            mouse.move(y=step)

for _ in range(5):
    move_mouse_along("x", 1, 20)
    move_mouse_along("y", 1, 20)
    move_mouse_along("x", -1, 20)
    move_mouse_along("y", -1, 20)
        

        