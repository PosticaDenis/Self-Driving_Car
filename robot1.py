import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk

FRIGHT_1 = 17
FRIGHT_2 = 27

BRIGHT_2 = 23
BRIGHT_1 = 24

FLEFT_1 = 5
FLEFT_2 = 6

BLEFT_1 = 20
BLEFT_2 = 21

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

def forward(tf):
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
    
def one(tf):
    init()
    gpio.output(FRIGHT_1, True)
    gpio.output(FRIGHT_2, False)

    time.sleep(tf)
    gpio.cleanup()

def two(tf):
    init()
    gpio.output(BRIGHT_1, True)
    gpio.output(BRIGHT_2, False)

    time.sleep(tf)
    gpio.cleanup()

def three(tf):
    init()
    gpio.output(FLEFT_1, True)
    gpio.output(FLEFT_2, False)

    time.sleep(tf)
    gpio.cleanup()

def four(tf):
    init()
    gpio.output(BLEFT_1, True)
    gpio.output(BLEFT_2, False)

    time.sleep(tf)
    gpio.cleanup()



def reverse(tf):
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

def right(tf):
    init()
    gpio.output(FRIGHT_1, True)
    gpio.output(FRIGHT_2, True)
    gpio.output(BRIGHT_1, False)
    gpio.output(BRIGHT_2, True)

    time.sleep(tf)
    gpio.cleanup()

def reverseRight(tf):
    init()
    gpio.output(FRIGHT_1, True)
    gpio.output(FRIGHT_2, True)
    gpio.output(BRIGHT_1, True)
    gpio.output(BRIGHT_2, False)

    time.sleep(tf)
    gpio.cleanup()

def left(tf):
    init()
    gpio.output(FRIGHT_1, False)
    gpio.output(FRIGHT_2, True)
    gpio.output(BRIGHT_1, True)
    gpio.output(BRIGHT_2, True)

    time.sleep(tf)
    gpio.cleanup()

def reverseLeft(tf):
    init()
    gpio.output(FRIGHT_1, True)
    gpio.output(FRIGHT_2, False)
    gpio.output(BRIGHT_1, True)
    gpio.output(BRIGHT_2, True)

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
    elif key_press.lower() == '1':
        one(st)
    elif key_press.lower() == '2':
        two(st)
    elif key_press.lower() == '3':
        three(st)
    elif key_press.lower() == '4':
        four(st)
    else:
        print("Hell no to the no no ...")


try:
    command = tk.Tk()
    command.bind('<KeyPress>', key_input)
    command.mainloop()
except KeyboardInterrupt:
    gpio.cleanup()