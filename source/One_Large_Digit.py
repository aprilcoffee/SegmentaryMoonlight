import RPi.GPIO as GPIO
import time

#GPIO declarations
#RightUp - A
segmentLatch1 = 23
segmentClock1 = 24
segmentData1 = 25

#LeftUp - B
segmentLatch2 = 17
segmentClock2 = 27
segmentData2 = 22

#RightDown - C
segmentLatch3 = 5
segmentClock3 = 6
segmentData3 = 13

#LeftDown - D
segmentLatch4 = 16
segmentClock4 = 20
segmentData4 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(segmentClock1,GPIO.OUT)
GPIO.setup(segmentLatch1,GPIO.OUT)
GPIO.setup(segmentData1,GPIO.OUT)

GPIO.output(segmentClock1,GPIO.LOW)
GPIO.output(segmentLatch1,GPIO.LOW)
GPIO.output(segmentData1,GPIO.LOW)

GPIO.setup(segmentClock2,GPIO.OUT)
GPIO.setup(segmentLatch2,GPIO.OUT)
GPIO.setup(segmentData2,GPIO.OUT)

GPIO.output(segmentClock2,GPIO.LOW)
GPIO.output(segmentLatch2,GPIO.LOW)
GPIO.output(segmentData2,GPIO.LOW)

GPIO.setup(segmentClock3,GPIO.OUT)
GPIO.setup(segmentLatch3,GPIO.OUT)
GPIO.setup(segmentData3,GPIO.OUT)

GPIO.output(segmentClock3,GPIO.LOW)
GPIO.output(segmentLatch3,GPIO.LOW)
GPIO.output(segmentData3,GPIO.LOW)

GPIO.setup(segmentClock4,GPIO.OUT)
GPIO.setup(segmentLatch4,GPIO.OUT)
GPIO.setup(segmentData4,GPIO.OUT)

GPIO.output(segmentClock4,GPIO.LOW)
GPIO.output(segmentLatch4,GPIO.LOW)
GPIO.output(segmentData4,GPIO.LOW)

def postNumber(nuber, decimal):
	#    -  A
	#   / / F/B
	#    -  G
	#   / / E/C
	#    -. D/DP
	a = 1<<0
	b = 1<<6
	c = 1<<5
	d = 1<<4
	e = 1<<3
	f = 1<<1
	g = 1<<2
	dp = 1<<7
	
	segments = 0;
	
	if(nuber == 1):
		segments = b | c
	elif(nuber == 2):
		segments = a | b | d | e | g
	elif(nuber == 3):
		segments = a | b | c | d | g
	elif(nuber == 4):
		segments = f | g | b | c
	elif(nuber == 5):
		segments = a | f | g | c | d
	elif(nuber == 6):
		segments = a | f | g | e | c | d
	elif(nuber == 7):
		segments = a | b | c
	elif(nuber == 8):
		segments = a | b | c | d | e | f | g
	elif(nuber == 9):
		segments = a | b | c | d | f | g
	elif(nuber == 0):
		segments = a | b | c | d | e | f
	else:
		segments = 0
		
	if (decimal):
		segments |= dp
	#Clock these bits out to the drivers
	n = 0
	while(n < 8):
		GPIO.output(segmentClock1,GPIO.LOW)
		GPIO.output(segmentData1,segments & 1 << (7 - n))
                GPIO.output(segmentClock1,GPIO.HIGH)

		GPIO.output(segmentClock2,GPIO.LOW)
                GPIO.output(segmentData2,segments & 1 << (7 - n))
                GPIO.output(segmentClock2,GPIO.HIGH)
		
		GPIO.output(segmentClock3,GPIO.LOW)
		GPIO.output(segmentData3,segments & 1 << (7 - n))
                GPIO.output(segmentClock3,GPIO.HIGH)
		
		GPIO.output(segmentClock4,GPIO.LOW)
                GPIO.output(segmentData4,segments & 1 << (7 - n))
                GPIO.output(segmentClock4,GPIO.HIGH)

                n+=1
x = 0
while(True):
	if(x == 9):
                postNumber(x, 1) #Show decimal
        else:
                postNumber(x, 0)
	
	GPIO.output(segmentLatch1,GPIO.LOW)
        GPIO.output(segmentLatch1,GPIO.HIGH)
	GPIO.output(segmentLatch2,GPIO.LOW)
        GPIO.output(segmentLatch2,GPIO.HIGH)
	GPIO.output(segmentLatch3,GPIO.LOW)
        GPIO.output(segmentLatch3,GPIO.HIGH)
	GPIO.output(segmentLatch4,GPIO.LOW)
	GPIO.output(segmentLatch4,GPIO.HIGH) #Register moves storage register on the rising edge of RCK
	time.sleep(0.5)
	
	x+=1
	x %= 10 #Reset x after 9
	
	print(x)

GPIO.cleanup()
