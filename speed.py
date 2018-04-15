import RPi.GPIO as gpio
import time


LEFT_1 = 17
LEFT_2 = 27
RIGHT_1 = 23
RIGHT_2 = 24
EN = 26
tf = 3

gpio.setmode(gpio.BCM)
gpio.setup(LEFT_1, gpio.OUT)
gpio.setup(LEFT_2, gpio.OUT)
gpio.setup(RIGHT_1, gpio.OUT)
gpio.setup(RIGHT_2, gpio.OUT)
gpio.setup(EN, gpio.OUT)
try:
    p = gpio.PWM(EN, 1000)
    p.start(5)
    gpio.output(LEFT_1, False)
    gpio.output(LEFT_2, True)
    gpio.output(RIGHT_1, False)
    gpio.output(RIGHT_2, True)
    time.sleep(tf)
except KeyboardInterrupt:
    gpio.cleanup()