import RPi.GPIO as GPIO
import time

#GPIO declarations
segmentLatch1 = 23
segmentClock1 = 24
segmentData1 = 25

segmentLatch2 = 17
segmentClock2 = 27
segmentData2 = 22

segmentLatch3 = 5
segmentClock3 = 6
segmentData3 = 13

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

def postNumber(number,decimal,clock,data):
	# -A
	# //F/B
	# -G
	# //E/C
	# -.D/DP
	a = 1<<0
	b = 1<<6
	c = 1<<5
	d = 1<<4
	e = 1<<3
	f = 1<<1
	g = 1<<2
	dp = 1<<7

	segments = 0
	if number==1:
		segments = b|c
	elif number==2:
		segments = a|b|d|e|g
	elif number==3:
		segments = a|b|c|d|g
	elif number==4:
		segments = f|g|b|c
	elif number==5:	
		segments = a|f|g|c|d
	elif number==6:
		segments = a|f|g|e|c|d
	elif number==7:
		segments = a|b|c
	elif number==8:
		segments = a|b|c|d|e|f|g
	elif number==9:
		segments = a|b|c|d|f|g
	elif number==0:
		segments = a|b|c|d|e|f
	else:
		segments = 0

	if(decimal):
		segments |= dp
	#clock these bits out to the drivers
	n = 0
	while n<8:
		GPIO.output(clock,GPIO.LOW)
		GPIO.output(data,segments & 1 << (7-n))
		GPIO.output(clock,GPIO.HIGH)
		n+=1

def showNum(value,clock,data,latch):
	numberHere = value
	for i in range(0,2):
		reminder = numberHere%10
		postNumber(reminder,1,clock,data)
		numberHere/=10
	GPIO.output(latch,GPIO.LOW)
	GPIO.output(latch,GPIO.HIGH)
x=0
showNumber = 0

while True:

	showNum(showNumber,segmentClock1,segmentData1,segmentLatch1)
	showNum(showNumber,segmentClock2,segmentData2,segmentLatch2)
	showNum(showNumber,segmentClock3,segmentData3,segmentLatch3)
	showNum(showNumber,segmentClock4,segmentData4,segmentLatch4)
	print(showNumber)

	time.sleep(0.1)
	showNumber+=1
	showNumber%=100
GPIO.cleanup()

