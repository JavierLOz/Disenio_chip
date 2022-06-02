import RPi.GPIO as GPIO

Led_Pin = 17
while True:
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(Led_Pin,GPIO.OUT)
	GPIO.output(Led_Pin, GPIO.HIGH)	
