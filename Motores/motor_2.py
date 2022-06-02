import RPi.GPIO as GPIO
from time import sleep

servo_pin = 17

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(servo_pin,GPIO.OUT)

servo_pwm = GPIO.PWM(servo_pin,50)
print("No hace nada ")
servo_pwm.start(0)	
while True :	
	
	for duty in range(0,20,1):
		servo_pwm.ChangeDutyCycle(duty)
		sleep(0.1)
		print(duty)
servo_pwm.stop()
GPIO.cleanup()
