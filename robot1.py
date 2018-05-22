import RPi.GPIO as gpio
import time
import Tkinter as tk

FRIGHT_1 = 23
FRIGHT_2 = 24
FRIGHT_PWM = 16

BRIGHT_1 = 27
BRIGHT_2 = 17
BRIGHT_PWM = 18

FLEFT_1 = 6
FLEFT_2 = 5
FLEFT_PWM = 13

BLEFT_1 = 21
BLEFT_2 = 20
BLEFT_PWM = 19


gpio.setmode(gpio.BCM)

gpio.setup(FRIGHT_PWM, gpio.OUT)
gpio.setup(BRIGHT_PWM, gpio.OUT)
gpio.setup(FLEFT_PWM, gpio.OUT)
gpio.setup(BLEFT_PWM, gpio.OUT)

gpio.setup(FRIGHT_1, gpio.OUT)
gpio.setup(FRIGHT_2, gpio.OUT)
gpio.setup(BRIGHT_1, gpio.OUT)
gpio.setup(BRIGHT_2, gpio.OUT)
gpio.setup(FLEFT_1, gpio.OUT)
gpio.setup(FLEFT_2, gpio.OUT)
gpio.setup(BLEFT_1, gpio.OUT)
gpio.setup(BLEFT_2, gpio.OUT)

pwmfr = gpio.PWM(FRIGHT_PWM, 100)
pwmbr = gpio.PWM(BRIGHT_PWM, 100)
pwmfl = gpio.PWM(FLEFT_PWM, 100)
pwmbl = gpio.PWM(BLEFT_PWM, 100)

pwmbr.start(0)
pwmfr.start(0)
pwmbl.start(0)
pwmfl.start(0)

def stop():
    pwmbl.ChangeDutyCycle(0)
    pwmfl.ChangeDutyCycle(0)
    pwmfr.ChangeDutyCycle(0)
    pwmbr.ChangeDutyCycle(0)

    gpio.output(FRIGHT_1, True)
    gpio.output(FRIGHT_2, True)
    gpio.output(BRIGHT_1, True)
    gpio.output(BRIGHT_2, True)

    gpio.output(FLEFT_1, True)
    gpio.output(FLEFT_2, True)
    gpio.output(BLEFT_1, True)
    gpio.output(BLEFT_2, True)

def reverse(tf, dc1, dc2, dc3, dc4):
    pwmbl.ChangeDutyCycle(100)
    pwmfl.ChangeDutyCycle(100)
    pwmfr.ChangeDutyCycle(100)
    pwmbr.ChangeDutyCycle(100)

    gpio.output(FRIGHT_1, False)
    gpio.output(FRIGHT_2, True)
    gpio.output(BRIGHT_1, False)
    gpio.output(BRIGHT_2, True)

    gpio.output(FLEFT_1, False)
    gpio.output(FLEFT_2, True)
    gpio.output(BLEFT_1, False)
    gpio.output(BLEFT_2, True)

    time.sleep(tf)
    stop()

def forward(tf, dc1, dc2, dc3, dc4):
    pwmbl.ChangeDutyCycle(dc1)
    pwmfl.ChangeDutyCycle(dc2)
    pwmfr.ChangeDutyCycle(dc3)
    pwmbr.ChangeDutyCycle(dc4)

    gpio.output(FRIGHT_1, True)
    gpio.output(FRIGHT_2, False)
    gpio.output(BRIGHT_1, True)
    gpio.output(BRIGHT_2, False)

    gpio.output(FLEFT_1, True)
    gpio.output(FLEFT_2, False)
    gpio.output(BLEFT_1, True)
    gpio.output(BLEFT_2, False)

    time.sleep(tf)
    stop()

def fullright(tf):
    pwmbl.ChangeDutyCycle(100)
    pwmfl.ChangeDutyCycle(100)
    pwmfr.ChangeDutyCycle(50)
    pwmbr.ChangeDutyCycle(50)

    gpio.output(FRIGHT_1, False)
    gpio.output(FRIGHT_2, True)
    gpio.output(BRIGHT_1, False)
    gpio.output(BRIGHT_2, True)

    gpio.output(FLEFT_1, True)
    gpio.output(FLEFT_2, False)
    gpio.output(BLEFT_1, True)
    gpio.output(BLEFT_2, False)

    time.sleep(tf)
    stop()

def fullleft(tf):
    pwmbl.ChangeDutyCycle(50)
    pwmfl.ChangeDutyCycle(50)
    pwmfr.ChangeDutyCycle(100)
    pwmbr.ChangeDutyCycle(100)

    gpio.output(FRIGHT_1, True)
    gpio.output(FRIGHT_2, False)
    gpio.output(BRIGHT_1, True)
    gpio.output(BRIGHT_2, False)

    gpio.output(FLEFT_1, False)
    gpio.output(FLEFT_2, True)
    gpio.output(BLEFT_1, False)
    gpio.output(BLEFT_2, True)

    time.sleep(tf)
    stop()

def key_input(event):
    print "Key: ", event.char
    key_press = event.char
    st = 0.05

    if key_press.lower() == 'w':
        forward(st, 100, 100, 100, 100)
    elif key_press.lower() == 's':
        reverse(st, 100, 100, 100, 100)
    elif key_press.lower() == 'a':
        forward(st, 40, 40, 100, 100)
    elif key_press.lower() == 'd':
        forward(st, 100, 100, 40, 40)
    elif key_press.lower() == 'z':
        reverse(st, 40, 40, 100, 100)
    elif key_press.lower() == 'x':
        reverse(st, 100, 100, 40, 40)
    else:
        print("Hell no to the no no ...")


try:
    command = tk.Tk()
    command.bind('<KeyPress>', key_input)
    command.mainloop()
except KeyboardInterrupt:
    gpio.cleanup()