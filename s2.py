import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)
TRIG = 26

ECHO = 19

print "Distance Measurement In Progress"
GPIO.setup(TRIG,GPIO.OUT)

GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(18, GPIO.OUT)



try:
    while(True):
        GPIO.output(TRIG, False)

        print "Waiting For Sensor To Settle"

        time.sleep(2)
        GPIO.output(TRIG, True)

        time.sleep(0.00001)

        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:

            pulse_start = time.time()
        while GPIO.input(ECHO)==1:

            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration*17150
        distance = round(distance, 2)
        print "Distance:",distance,"cm"

	if distance >= 5:
            print('motor run')
            GPIO.output(18, GPIO.HIGH)
        else:
            GPIO.output(18, GPIO.LOW)
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
