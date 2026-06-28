import time
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

print("Ready for Linux!")

# Wait for Linux to detect the Pico
time.sleep(5)

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

# Open Terminal (works on GNOME, Cinnamon, XFCE, etc.)
kbd.press(Keycode.CONTROL, Keycode.ALT, Keycode.T)
kbd.release_all()

time.sleep(2)

# Launch your application
layout.write(r'"/path/to/file"')
kbd.press(Keycode.ENTER)
kbd.release_all()

time.sleep(2)

# Open another terminal
kbd.press(Keycode.CONTROL, Keycode.ALT, Keycode.T)
kbd.release_all()

time.sleep(2)

# Launch Mozilla Firefox
layout.write("firefox")
kbd.press(Keycode.ENTER)
kbd.release_all()
