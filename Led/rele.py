import RPi.GPIO as GPIO
from time import sleep

rele_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(rele_pin,GPIO.OUT)

while True:
	GPIO.output(rele_pin,GPIO.HIGH)
	print("High")
	sleep(1)
	GPIO.output(rele_pin,GPIO.LOW)
	print("Low")
