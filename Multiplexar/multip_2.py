
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

rows = [5,6,12,13,19,16,26,20]
cols = [4,15,18,22,23,14,25,21]
fig1 =[(1,1,0,0,0,0,1,1),
	  (1,1,0,0,0,0,1,1),
	  (1,1,0,0,0,0,1,1),
	  (1,1,1,0,0,1,0,1),
	  (1,1,0,0,0,0,1,1),
	  (1,0,1,0,0,1,1,1),
	  (1,1,1,0,0,1,1,1),
	  (1,1,0,1,0,1,1,1)] 

fig2 =[(1,1,0,0,0,0,1,1),
	  (1,1,0,0,0,0,1,1),
	  (1,1,0,0,0,0,1,1),
	  (1,0,1,0,0,1,1,1),
	  (1,1,0,0,0,0,1,1),
	  (1,1,1,0,0,1,0,1),
	  (1,1,1,0,0,1,1,1),
	  (1,1,1,0,1,0,1,1)]

for pin in rows:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,0)
for pin in cols:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,1)
	
def pintar_mono(fig1):
    for row in range(8):
            for col in range(8):
            	GPIO.output(rows[row],1)
            	time.sleep(0.00001)
            	GPIO.output(cols[col],fig1[row][col])
            	time.sleep(0.00001)
            	GPIO.output(rows[row],0)
            	GPIO.output(cols[col],1)
    
while True:
    try:	
        for i in range(30):
            pintar_mono(fig1)
        time.sleep(0.001)
        for i in range(30):
            pintar_mono(fig2)
    except KeyboardInterrupt:
        GPIO.cleanup()C