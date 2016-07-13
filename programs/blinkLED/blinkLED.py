# simple program which blinks LED infinitely

# hardware setup: connect LED to pin 18 and resistor 220 Ohm in serial and then to GND

import RPi.GPIO as GPIO
from time import sleep

pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

while True:
    GPIO.output(pin, GPIO.HIGH)
    sleep(1)
    GPIO.output(pin, GPIO.LOW)
    sleep(1)

GPIO.cleanup()
