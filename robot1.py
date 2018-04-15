import RPi.GPIO as gpio
import time

LEFT_1 = 17
LEFT_2 = 27

RIGHT_1 = 23
RIGHT_2 = 24
def init():
    gpio.setmode(gpio.BCM)
    #gpio.cleanup()
    gpio.setup(LEFT_1, gpio.OUT)
    gpio.setup(LEFT_2, gpio.OUT)
    gpio.setup(RIGHT_1, gpio.OUT)
    gpio.setup(RIGHT_2, gpio.OUT)

def forward(tf):
    init()
    gpio.output(LEFT_1, False)
    gpio.output(LEFT_2, True)
    gpio.output(RIGHT_1, False)
    gpio.output(RIGHT_2, True)

    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):
    init()
    gpio.output(LEFT_1, True)
    gpio.output(LEFT_2, False)
    gpio.output(RIGHT_1, True)
    gpio.output(RIGHT_2, False)

    time.sleep(tf)
    gpio.cleanup()

def right(tf):
    init()
    gpio.output(LEFT_1, gpio.HIGH)
    gpio.output(LEFT_2, gpio.HIGH)
    gpio.output(RIGHT_1, gpio.LOW)
    gpio.output(RIGHT_2, gpio.HIGH)

    time.sleep(tf)
    gpio.cleanup()

def left(tf):
    init()
    gpio.output(LEFT_1, gpio.LOW)
    gpio.output(LEFT_2, gpio.HIGH)
    gpio.output(RIGHT_1, gpio.HIGH)
    gpio.output(RIGHT_2, gpio.HIGH)

    time.sleep(tf)
    gpio.cleanup()

try:
    print "forward"
#    forward(3)
    print "back"
#    reverse(3)
    print "left"
    left(1)
    print "right"
    right(1)
except KeyboardInterrupt:
    gpio.cleanup()
