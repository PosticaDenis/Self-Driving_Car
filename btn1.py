import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

gpio.setup(11, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(12, gpio.OUT)
#gpio.add_event_detect(11, gpio.RISING)

try:
    while(True):
        inp = gpio.input(11)
       # time.sleep(0.1)
       # gpio.add_event_detect(11, gpio.RISING)
        if inp == False:
            print('button pressed')
            gpio.output(12, gpio.HIGH)
            time.sleep(4)
            gpio.output(12, gpio.LOW)
except KeyboardInterrupt:
    gpio.cleanup()



