import time
import board, digitalio
import touchio
import storage
import usb_cdc
import usb_midi
import neopixel
import usb_hid

print("--- Log sent from boot.py to boout_out.txt ---") 

touch1in = touchio.TouchIn(board.RX)
touch2in = touchio.TouchIn(board.TX)

if touch1in.raw_value > 900 and touch2in.raw_value > 900:
    print("RX & TX touched. Keeping ON USB devices")
    # or enable just certain HID devices
    #
    #usb_hid.enable(devices=(usb_hid.Device.MOUSE,))
    #usb_hid.enable(devices=(usb_hid.Device.KEYBOARD))
    #usb_hid.enable(devices=(usb_hid.Device.CONSUMER_CONTROL,))
else:
    print("RX & TX not touched. Turning OFF USB devices")
    storage.disable_usb_drive()  # disable CIRCUITPY
    usb_cdc.disable()            # disable REPL
    usb_midi.disable()           # disable MIDI