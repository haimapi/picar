# filename: demo1.py
# function: realize basic control of motor

import RPi.GPIO as gpio
from time import sleep


in_pin1 = 17
in_pin2 = 18

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

gpio.setup(in_pin1, gpio.OUT)
gpio.setup(in_pin2, gpio.OUT)

gpio.output(in_pin1, True)
gpio.output(in_pin2, False)

sleep(4)

gpio.output(in_pin1, False)
gpio.output(in_pin2, True)

sleep(4)

gpio.cleanup()
