# simple program which blinks LED infinitely

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
