import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk


LEFT_1 = 17
LEFT_2 = 27

RIGHT_2 = 23
RIGHT_1 = 24

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(LEFT_1, gpio.OUT)
    gpio.setup(LEFT_2, gpio.OUT)

def forward(tf):
    init()
    gpio.output(LEFT_1, False)
    gpio.output(LEFT_2, True)

    time.sleep(tf)
    gpio.cleanup()

def forward2(tf):
    init()
    gpio.output(LEFT_1, True)
    gpio.output(LEFT_2, False)

    time.sleep(tf)
    gpio.cleanup()

def forward3(tf):
    init()
    gpio.output(LEFT_1, False)
    gpio.output(LEFT_2, True)

    time.sleep(tf)
    gpio.cleanup()

def forward4(tf):
    init()
    gpio.output(LEFT_1, False)
    gpio.output(LEFT_2, True)

    time.sleep(tf)
    gpio.cleanup()


def key_input(event):
    print "Key: ", event.char
    key_press = event.char
    st = 0.085

    if key_press.lower() == 'w':
        forward(st)
    elif key_press.lower() == 'a':
        forward2(st)
    elif key_press.lower() == 's':
        forward3(st)
    elif key_press.lower() == 'd':
        forward4(st)
    else:
        print("Hell no to the no no ...")


try:
    command = tk.Tk()
    command.bind('<KeyPress>', key_input)
    command.mainloop()
except KeyboardInterrupt:
    gpio.cleanup()