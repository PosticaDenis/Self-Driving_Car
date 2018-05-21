import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk

FRIGHT_1 = 23
FRIGHT_2 = 24

BRIGHT_1 = 27
BRIGHT_2 = 17

FLEFT_1 = 6
FLEFT_2 = 5

BLEFT_1 = 21
BLEFT_2 = 20

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(FRIGHT_1, gpio.OUT)
    gpio.setup(FRIGHT_2, gpio.OUT)
    gpio.setup(BRIGHT_1, gpio.OUT)
    gpio.setup(BRIGHT_2, gpio.OUT)
    gpio.setup(FLEFT_1, gpio.OUT)
    gpio.setup(FLEFT_2, gpio.OUT)
    gpio.setup(BLEFT_1, gpio.OUT)
    gpio.setup(BLEFT_2, gpio.OUT)

def reverse(tf):
    init()
    gpio.output(FRIGHT_1, False)
    gpio.output(FRIGHT_2, True)
    gpio.output(BRIGHT_1, False)
    gpio.output(BRIGHT_2, True)

    gpio.output(FLEFT_1, False)
    gpio.output(FLEFT_2, True)
    gpio.output(BLEFT_1, False)
    gpio.output(BLEFT_2, True)

    time.sleep(tf)
    gpio.cleanup()

def forward(tf):
    init()
    gpio.output(FRIGHT_1, True)
    gpio.output(FRIGHT_2, False)
    gpio.output(BRIGHT_1, True)
    gpio.output(BRIGHT_2, False)

    gpio.output(FLEFT_1, True)
    gpio.output(FLEFT_2, False)
    gpio.output(BLEFT_1, True)
    gpio.output(BLEFT_2, False)

    time.sleep(tf)
    gpio.cleanup()

def fullright(tf):
    init()
    gpio.output(FRIGHT_1, False)
    gpio.output(FRIGHT_2, True)
    gpio.output(BRIGHT_1, False)
    gpio.output(BRIGHT_2, True)

    gpio.output(FLEFT_1, True)
    gpio.output(FLEFT_2, False)
    gpio.output(BLEFT_1, True)
    gpio.output(BLEFT_2, False)

    time.sleep(tf)
    gpio.cleanup()

def right(tf):
    init()
    gpio.output(FRIGHT_1, True)
    gpio.output(FRIGHT_2, True)
    gpio.output(BRIGHT_1, True)
    gpio.output(BRIGHT_2, True)

    gpio.output(FLEFT_1, True)
    gpio.output(FLEFT_2, False)
    gpio.output(BLEFT_1, True)
    gpio.output(BLEFT_2, False)

    time.sleep(tf)
    gpio.cleanup()

def fullleft(tf):
    init()
    gpio.output(FRIGHT_1, True)
    gpio.output(FRIGHT_2, False)
    gpio.output(BRIGHT_1, True)
    gpio.output(BRIGHT_2, True)

    gpio.output(FLEFT_1, True)
    gpio.output(FLEFT_2, True)
    gpio.output(BLEFT_1, False)
    gpio.output(BLEFT_2, True)

    time.sleep(tf)
    gpio.cleanup()

def left(tf):
    init()
    gpio.output(FRIGHT_1, True)
    gpio.output(FRIGHT_2, False)
    gpio.output(BRIGHT_1, True)
    gpio.output(BRIGHT_2, False)

    gpio.output(FLEFT_1, True)
    gpio.output(FLEFT_2, True)
    gpio.output(BLEFT_1, True)
    gpio.output(BLEFT_2, True)

    time.sleep(tf)
    gpio.cleanup()

def key_input(event):
    print "Key: ", event.char
    key_press = event.char
    st = 0.05

    if key_press.lower() == 'w':
        forward(st)
    elif key_press.lower() == 's':
        reverse(st)
    elif key_press.lower() == 'a':
        fullleft(st)
    elif key_press.lower() == 'd':
        fullright(st)
    elif key_press.lower() == 'q':
        left(st)
    elif key_press.lower() == 'e':
        right(st)
    else:
        print("Hell no to the no no ...")


try:
    command = tk.Tk()
    command.bind('<KeyPress>', key_input)
    command.mainloop()
except KeyboardInterrupt:
    gpio.cleanup()