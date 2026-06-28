import time
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

time.sleep(5)

# Open terminal
kbd.press(Keycode.CONTROL, Keycode.ALT, Keycode.T)
kbd.release_all()

# IMPORTANT: give terminal time to fully open
time.sleep(5)

# Terminal Auto-enter Command

def run(cmd, delay=2):
    layout.write(cmd)
    kbd.press(Keycode.ENTER)
    kbd.release_all()
    time.sleep(delay)

# Terminal Commands
run("echo STARTING SESSION")

run('export AWS_SECRET_ACCESS_KEY="enter credentials"')
run('export AWS_ACCESS_KEY_ID="enter credentials"')
run('export AWS_REGION="ap-southeast-2"')

run("git clone https://github.com/sudoHades1/terraform-aws-1")
run("cd terraform-aws-1")
run("terraform init")

time.sleep(20)
run("terraform apply -auto-approve")
