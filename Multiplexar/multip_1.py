2
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
        #   A  B  C  D  E  F  G  DP
segments = [21,20,16,26,19,13,12,6]
    #  t1 t2 t3 t4 
pwr = [4,17,27,22]

row_k = [2,3,14,15]

col_k = [18,23,24,25]

letr = [[1,0,0,0,0,1,1,1],
        [0,0,0,1,0,0,0,1],
        [1,0,0,0,0,0,1,1],
        [1,0,0,1,1,1,1,1]]

for seg in segments:
	GPIO.setup(segments,GPIO.OUT)
	GPIO.output(segments,1)
for p in pwr:
	GPIO.setup(p,GPIO.OUT)
	GPIO.output(p,0)

while True:
    try:
        ind =0        
        for index in range(len(letr)):
            GPIO.output(pwr[ind],1)
            for ltr in range(8):
                GPIO.output(segments[ltr],letr[index][ltr])
            time.sleep(0.001)    
            GPIO.output(pwr[ind],0)
            
            if index >= 3 and ind >= 3:
                ind = 0

            else:
                ind += 1
            
    except KeyboardInterrupt:
        GPIO.cleanup()
