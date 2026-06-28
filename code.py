import time
import usb_hid

print("Ready for your application!")

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Wait for Windows to recognize the device
time.sleep(5)

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

# Open Run dialog
kbd.press(Keycode.WINDOWS, Keycode.R)
kbd.release_all()

time.sleep(1)

# Launch Application
layout.write(r'"/path/to/file"')
kbd.press(Keycode.ENTER)
kbd.release_all()

time.sleep(2)

# Open Run dialog again
kbd.press(Keycode.WINDOWS, Keycode.R)
kbd.release_all()

time.sleep(1)

# Launch Microsoft Edge
layout.write("msedge")
kbd.press(Keycode.ENTER)
kbd.release_all()

