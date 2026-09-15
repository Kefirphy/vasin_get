import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds=[16,12,25,17,27,23,22,24]

GPIO.setup(leds,GPIO.OUT)

GPIO.output(leds,0)

buttonUp=9
buttonDown=10

GPIO.setup(buttonUp,GPIO.IN)
GPIO.setup(buttonDown,GPIO.IN)

num=0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time=0.1

while True:
    if GPIO.input(buttonUp) and GPIO.input(buttonDown):
        num=255
        print(num,dec2bin(num))
        time.sleep(sleep_time)
    elif GPIO.input(buttonUp):
        num+=1
        if num > 255:
            num=0
        print(num,dec2bin(num))
        time.sleep(sleep_time)
    elif GPIO.input(buttonDown):
        num-=1
        if num<0:
            num=0
        print(num,dec2bin(num))
        time.sleep(sleep_time)
    GPIO.output(leds,dec2bin(num))