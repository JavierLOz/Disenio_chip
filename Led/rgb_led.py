import RPi.GPIO as GPIO 
import time 

R = 17
G = 27
B = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(R,GPIO.OUT)
GPIO.setup(G,GPIO.OUT)
GPIO.setup(B,GPIO.OUT)

pwm_R = GPIO.PWM(R,1000)
pwm_G = GPIO.PWM(G,1000)
pwm_B = GPIO.PWM(B,1000)

pwm_R.start(100)
pwm_G.start(0)
pwm_B.start(100)		
while True :
	for duty in range(0,100,1):
		pwm_R.ChangeDutyCycle(duty)
		time.sleep(0.05)
