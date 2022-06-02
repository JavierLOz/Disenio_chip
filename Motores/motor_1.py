import RPi.GPIO as GPIO
import time
import serial

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

    
ard_js = serial.Serial("/dev/ttyACM0",baudrate=115200,timeout=1.0)
motor_1 = [19,26]
motor_2 = [16,20]

for i in range(2):
	GPIO.setup(motor_1[i], GPIO.OUT)
	GPIO.output(motor_1[i],0)
	GPIO.setup(motor_2[i], GPIO.OUT)
	GPIO.output(motor_2[i],0)


#20 en 1 motor 2 adelante
	#19 en motor 2 adelante
def return_val(val):
    if val == '1':
               #1 1 2 2
        return [0,1,1,0]
    elif val == '2':
        return [1,0,0,1]
    elif val == '3':
        return [0,1,0,1]
    elif val == '4':
        return [1,0,1,0]
    else:
        return [0,0,0,0]

def move_mtr(lst):
    for i in range(2):
        GPIO.output(motor_1[i],lst[i])
    for i in range(2,4):
        GPIO.output(motor_2[i-2],lst[i])    
    time.sleep(0.0001)
        
while True:
    lect = ard_js.read()
    val = str(lect,'UTF-8',errors='ignore')
    print(val)
    motor_lst = return_val(val)
    print(motor_lst)
    move_mtr(motor_lst)