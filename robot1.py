import RPi.GPIO as gpio
import time

class Motors:
    LEFT_1 = 17
    LEFT_2 = 27

    RIGHT_1 = 23
    RIGHT_2 = 24

    def init(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(self.LEFT_1, gpio.OUT)
        gpio.setup(self.LEFT_2, gpio.OUT)
        gpio.setup(self.RIGHT_1, gpio.OUT)
        gpio.setup(self.RIGHT_2, gpio.OUT)

    def forward(self, tf):
        self.init()
        gpio.output(self.LEFT_1, False)
        gpio.output(self.LEFT_2, True)
        gpio.output(self.RIGHT_1, False)
        gpio.output(self.RIGHT_2, True)

        time.sleep(tf)
        gpio.cleanup()

    def reverse(self, tf):
        self.init()
        gpio.output(self.LEFT_1, True)
        gpio.output(self.LEFT_2, False)
        gpio.output(self.RIGHT_1, True)
        gpio.output(self.RIGHT_2, False)

        time.sleep(tf)
        gpio.cleanup()

    def right(self, tf):
        self.init()
        gpio.output(self.LEFT_1, gpio.HIGH)
        gpio.output(self.LEFT_2, gpio.HIGH)
        gpio.output(self.RIGHT_1, gpio.LOW)
        gpio.output(self.RIGHT_2, gpio.HIGH)

        time.sleep(tf)
        gpio.cleanup()

    def left(self, tf):
        self.init()
        gpio.output(self.LEFT_1, gpio.LOW)
        gpio.output(self.LEFT_2, gpio.HIGH)
        gpio.output(self.RIGHT_1, gpio.HIGH)
        gpio.output(self.RIGHT_2, gpio.HIGH)

        time.sleep(tf)
        gpio.cleanup()

try:
    motor = Motors()

except KeyboardInterrupt:
    gpio.cleanup()
