import RPi.GPIO as gpio
from time import sleep

class Wheel():
    def __init__(self, in_pin1, in_pin2,):
        self.in_pin1 = in_pin1
        self.in_pin2 = in_pin2

        gpio.setup(in_pin1, gpio.OUT)
        gpio.setup(in_pin2, gpio.OUT)

    def roar_p(self):
	gpio.output(in_pin1, True)
	gpio.output(in_pin2, False)

    def roar_n(self):
	gpio.output(in_pin1, False)
	gpio.output(in_pin2, True)

    def roar_stop(sefl):
	gpio.output(in_pin1, False)
	gpio.output(in_pin2, False)


class Car():
    def __init__(self, left_pin1, left_pin2, right_pin1, right_pin2):
	gpio.setmode(gpio.BCM)
	gpio.setwarnings(False)

	self.left_wheel = Wheel(left_pin1, left_pin2)
	self.right_wheel = Wheel(right_pin1, right_pin2)

    def car_forward(self):
	self.left_wheel.roar_p()
	self.right_wheel.roar_p()

    def car_backward(self):
	self.left_wheel.roar_n()
	self.right_wheel.roar_n()

    def car_left_turn(self):
	self.left_wheel.roar_stop()
	self.right_wheel.roar_p()

    def car_right_turn(self):
	self.left_wheel.roar_p()
        self.right_wheel.roar_stop()

    def car_stop(self):
        self.left_wheel.roar_stop()
	self.right_wheel.roar_stop()

    def shutdown(self):
	self.car_stop()
	gpio.cleanup()

if __name__ == '__main__':
    mycar = Car(16, 19, 20, 26)

    mycar.car_forward()
    sleep(2)
    mycar.car_left_turn()
    sleep(1)
    mycar.car_forward()
    mycar.car_right_turn()
    sleep(1)
