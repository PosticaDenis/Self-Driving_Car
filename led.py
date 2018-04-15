import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(18, gpio.OUT)

try:
    while(True):
        print "LED on"
        gpio.output(18, gpio.HIGH)
        time.sleep(0.5)
        gpio.output(18, gpio.LOW)
        time.sleep(0.5)
        print "LED off"
except KeyboardInterrupt:
    gpio.cleanup()
