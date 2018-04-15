from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from time import sleep
import sys
import Tkinter as tk

# ///////////////// Define Motor Driver GPIO Pins /////////////////
# Motor A, Left Side GPIO CONSTANTS
PWM_DRIVE_LEFT = 21  # ENA - H-Bridge enable pin
FORWARD_LEFT_PIN = 26  # IN1 - Forward Drive
REVERSE_LEFT_PIN = 19  # IN2 - Reverse Drive
# Motor B, Right Side GPIO CONSTANTS
PWM_DRIVE_RIGHT = 5  # ENB - H-Bridge enable pin
FORWARD_RIGHT_PIN = 13  # IN1 - Forward Drive
REVERSE_RIGHT_PIN = 6  # IN2 - Reverse Drive

# Initialise objects for H-Bridge GPIO PWM pins
# Set initial duty cycle to 0 and frequency to 1000
driveLeft = PWMOutputDevice(PWM_DRIVE_LEFT, True, 0, 1000)
driveRight = PWMOutputDevice(PWM_DRIVE_RIGHT, True, 0, 1000)

# Initialise objects for H-Bridge digital GPIO pins
forwardLeft = PWMOutputDevice(FORWARD_LEFT_PIN)
reverseLeft = PWMOutputDevice(REVERSE_LEFT_PIN)
forwardRight = PWMOutputDevice(FORWARD_RIGHT_PIN)
reverseRight = PWMOutputDevice(REVERSE_RIGHT_PIN)


def allStop():
    forwardLeft.value = False
    reverseLeft.value = False
    forwardRight.value = False
    reverseRight.value = False
    driveLeft.value = 0
    driveRight.value = 0


def forwardDrive(st):
    forwardLeft.value = True
    reverseLeft.value = False
    forwardRight.value = True
    reverseRight.value = False
    driveLeft.value = 1.0
    driveRight.value = 1.0

    sleep(st)
    allStop()


def reverseDrive(st):
    forwardLeft.value = False
    reverseLeft.value = True
    forwardRight.value = False
    reverseRight.value = True
    driveLeft.value = 1.0
    driveRight.value = 1.0

    sleep(st)
    allStop()

def spinLeft(st):
    forwardLeft.value = True
    reverseLeft.value = False
    forwardRight.value = False
    reverseRight.value = True
    driveLeft.value = 1.0
    driveRight.value = 0.4

    sleep(st)
    allStop()


def spinRight(st):
    forwardLeft.value = False
    reverseLeft.value = True
    forwardRight.value = True
    reverseRight.value = False
    driveLeft.value = 0.4
    driveRight.value = 1.0

    sleep(st)
    allStop()


def forwardTurnLeft(st):
    forwardLeft.value = True
    reverseLeft.value = False
    forwardRight.value = True
    reverseRight.value = False
    driveLeft.value = 0.6
    driveRight.value = 0.8

    sleep(st)
    allStop()


def forwardTurnRight(st):
    forwardLeft.value = True
    reverseLeft.value = False
    forwardRight.value = True
    reverseRight.value = False
    driveLeft.value = 0.8
    driveRight.value = 0.6

    sleep(st)
    allStop()


def reverseTurnLeft(st):
    forwardLeft.value = False
    reverseLeft.value = True
    forwardRight.value = False
    reverseRight.value = True
    driveLeft.value = 0.6
    driveRight.value = 0.8

    sleep(st)
    allStop()


def reverseTurnRight(st):
    forwardLeft.value = False
    reverseLeft.value = True
    forwardRight.value = False
    reverseRight.value = True
    driveLeft.value = 0.8
    driveRight.value = 0.6

    sleep(st)
    allStop()


'''def main():
    allStop()
    forwardDrive()
    sleep(5)
    reverseDrive()
    sleep(5)
    spinLeft()
    sleep(5)
    SpinRight()
    sleep(5)
    forwardTurnLeft()
    sleep(5)
    forwardTurnRight()
    sleep(5)
    reverseTurnLeft()
    sleep(5)
    reverseTurnRight()
    sleep(5)
    allStop()'''

def key_input(event):
    print "Key: ", event.char
    key_press = event.char
    st = 0.085

    if key_press.lower() == 'w':
        forwardDrive(st)
    elif key_press.lower() == 's':
        reverseDrive(st)
    elif key_press.lower() == 'a':
        spinLeft(st)
    elif key_press.lower() == 'd':
        spinRight(st)
    elif key_press.lower() == 'q':
        forwardTurnLeft(st)
    elif key_press.lower() == 'e':
        forwardTurnRight(st)
    elif key_press.lower() == 'z':
        reverseTurnLeft(st)
    elif key_press.lower() == 'x':
        reverseTurnRight(st)
    else:
        print("Hell no to the no no ...")


try:
    command = tk.Tk()
    command.bind('<KeyPress>', key_input)
    command.mainloop()
except KeyboardInterrupt:
    allStop()