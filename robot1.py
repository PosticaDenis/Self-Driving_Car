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
    gpio.output(LEFT_1, True)
    gpio.output(LEFT_2, True)
    gpio.output(RIGHT_1, False)
    gpio.output(RIGHT_2, True)

    time.sleep(tf)
    gpio.cleanup()

def reverseRight(tf):
    init()
    gpio.output(LEFT_1, True)
    gpio.output(LEFT_2, True)
    gpio.output(RIGHT_1, True)
    gpio.output(RIGHT_2, False)

    time.sleep(tf)
    gpio.cleanup()

def left(tf):
    init()
    gpio.output(LEFT_1, False)
    gpio.output(LEFT_2, True)
    gpio.output(RIGHT_1, True)
    gpio.output(RIGHT_2, True)

    time.sleep(tf)
    gpio.cleanup()

def reverseLeft(tf):
    init()
    gpio.output(LEFT_1, True)
    gpio.output(LEFT_2, False)
    gpio.output(RIGHT_1, True)
    gpio.output(RIGHT_2, True)

    time.sleep(tf)
    gpio.cleanup()


def key_input(event):
    print "Key: ", event.char
    key_press = event.char
    st = 0.085

    if key_press.lower() == 'w':
        forward(st)
    elif key_press.lower() == 's':
        reverse(st)
    elif key_press.lower() == 'a':
        left(st)
    elif key_press.lower() == 'd':
        right(st)
    elif key_press.lower() == 'z':
        reverseLeft(st)
    elif key_press.lower() == 'x':
        reverseRight(st)
    else:
        print("Hell no to the no no ...")


try:
    command = tk.Tk()
    command.bind('<KeyPress>', key_input)
    command.mainloop()
except KeyboardInterrupt:
    gpio.cleanup()