from gpiozero import PWMOutputDevice
import Tkinter as tk
import time

PWM_DRIVE_FRIGHT = 26
FRIGHT_1 = 23
FRIGHT_2 = 24

PWM_DRIVE_BRIGHT = 12
BRIGHT_1 = 27
BRIGHT_2 = 17

PWM_DRIVE_FLEFT = 22
FLEFT_1 = 6
FLEFT_2 = 5

PWM_DRIVE_BLEFT = 25
BLEFT_1 = 21
BLEFT_2 = 20

# Initialise objects for H-Bridge GPIO PWM pins
# Set initial duty cycle to 0 and frequency to 1000
driveLeft1 = PWMOutputDevice(PWM_DRIVE_FLEFT, True, 0, 1000)
driveLeft2 = PWMOutputDevice(PWM_DRIVE_BLEFT, True, 0, 1000)

driveRight1 = PWMOutputDevice(PWM_DRIVE_FRIGHT, True, 0, 1000)
driveRight2 = PWMOutputDevice(PWM_DRIVE_BRIGHT, True, 0, 1000)

# Initialise objects for H-Bridge digital GPIO pins
forwardLeft1 = PWMOutputDevice(FLEFT_1)
forwardLeft2 = PWMOutputDevice(FLEFT_2)

reverseLeft1 = PWMOutputDevice(BLEFT_1)
reverseLeft2 = PWMOutputDevice(BLEFT_2)

forwardRight1 = PWMOutputDevice(FRIGHT_1)
forwardRight2 = PWMOutputDevice(FRIGHT_2)

reverseRight1 = PWMOutputDevice(BRIGHT_1)
reverseRight2 = PWMOutputDevice(BRIGHT_2)

def forwardDrive(tf):
    forwardLeft1.value = True
    forwardLeft2.value = False
    reverseLeft1.value = True
    reverseLeft2.value = False
    forwardRight1.value = True
    forwardRight2.value = False
    reverseRight1.value = True
    reverseRight2.value = False
    driveRight1.value = 1.0
    driveRight2.value = 1.0
    driveLeft1.value = 0.7
    driveLeft2.value = 0.7
    time.sleep(tf)
    allStop()

def allStop():
    forwardLeft1.value = False
    forwardLeft2.value = False
    reverseLeft1.value = False
    reverseLeft2.value = False
    forwardRight1.value = False
    forwardRight2.value = False
    reverseRight1.value = False
    reverseRight2.value = False
    driveRight1.value = 0.0
    driveRight2.value = 0.0
    driveLeft1.value = 0.0
    driveLeft2.value = 0.0

def key_input(event):
    print "Key: ", event.char
    key_press = event.char
    key_set = ['w']

    if key_press.lower() in key_set:
        forwardDrive(0.03)
    else:
        print("Hell no to the no no ...")

command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()