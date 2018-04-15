import RPi.GPIO as gpio
import time

def dist(measure='cm'):
    gpio.setmode(gpio.BOARD)
    gpio.setup(12, gpio.OUT)
    gpio.setup(16, gpio.IN)

    gpio.output(12, False)
    while gpio.input(16) == 0:
        nosig = time.time()

    while gpio.input(16) == 1:
        sig = time.time()

    tl = sig - nosig

    if measure == 'cm':
        dist = tl / 0.000058
    elif measure == 'in':
        dist = tl / 0.000148
    else:
        print 'fuck you'
        dist = None

    gpio.cleanup()
    return dist

print(dist('cm'))

