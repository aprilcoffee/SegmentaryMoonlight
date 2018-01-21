import RPi.GPIO as GPIO
import time

#GPIO declarations
segmentClock = 23
segmentLatch = 24
segmentData = 25

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(segmentClock,GPIO.OUT)
GPIO.setup(segmentLatch,GPIO.OUT)
GPIO.setup(segmentData,GPIO.OUT)

GPIO.output(segmentClock,GPIO.LOW)
GPIO.output(segmentLatch,GPIO.LOW)
GPIO.output(segmentData,GPIO.LOW)

def postNumber(number,decimal):
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
		GPIO.output(segmentClock,GPIO.LOW)
		GPIO.output(segmentData,segments & 1 << (7-n))
		GPIO.output(segmentClock,GPIO.HIGH)
		n+=1

def showNum(value):
	numberHere = value
	for i in range(0,2):
		reminder = numberHere%10
		postNumber(reminder,1)
		numberHere/=10
	GPIO.output(segmentLatch,GPIO.LOW)
	GPIO.output(segmentLatch,GPIO.HIGH)

x=0
showNumber = 0
while True:
	
	showNum(showNumber)

	print(showNumber)

	time.sleep(0.1)
	showNumber+=1
	showNumber%=100
GPIO.cleanup()





