import RPi.GPIO as gpio
import time


class Employee:
    port1=17
    port2=27
    port3=23
    port4=24

    def init(sefl):
    gpio.setmode(gpio.BCM)
    gpio.setup(port1, gpio.OUT)
    gpio.setup(port2, gpio.OUT)
    gpio.setup(port3, gpio.OUT)
    gpio.setup(port4, gpio.OUT)

    def left(self,distance):
        print ("move back:",distance)
        gpio.output(self.port1, False)
        gpio.output(self.port2, True)
        gpio.output(self.port1, False)
        gpio.output(self.port1, True)


    def right(self,distance):
        print ("move back:",distance)
        #gpio.output(LEFT_1, False)
        #gpio.output(LEFT_2, True)
        #gpio.output(RIGHT_1, False)
        #gpio.output(RIGHT_2, True)

    def forward(self,distance):
        print ("move back:",distance)
        gpio.output(self.port1, True)
        gpio.output(self, True)
        gpio.output(self, False)
        gpio.output(self, False)
        time.sleep(distance)
        gpio.cleanup()


    def back(self,distance):
        print ("move back:",distance)
        #gpio.output(LEFT_1, False)
        #gpio.output(LEFT_2, True)
        #gpio.output(RIGHT_1, False)
        #gpio.output(RIGHT_2, True)



try:

exec_command=Employee()
exec_command.forward(12)

except KeyboardInterrupt:
    gpio.cleanup()
