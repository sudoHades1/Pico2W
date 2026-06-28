import time
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

time.sleep(5)  # Give yourself time to focus the terminal

command = (
    "git clone https://github.com/sudoHades1/Pico2W.git && "
    "cd Pico2W && "
    "linux_autorun_terraform.py"
)

layout.write(command)
kbd.press(Keycode.ENTER)
kbd.release_all()
