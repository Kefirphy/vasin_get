import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led=26
photo = 6

GPIO.setup(led,GPIO.OUT)
GPIO.setup(photo,GPIO.IN)

while True:
    sensor_state=GPIO.input(photo)
    GPIO.output(led,not sensor_state)
    time.sleep(0.05)