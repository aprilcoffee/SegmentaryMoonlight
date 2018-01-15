import RPi.GPIO as GPIO
import time
import datetime
from random import randint

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
segmentLatch3 = 13
segmentClock3 = 19
segmentData3 = 26

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

def showNum(value,decimal,numbersToRun,clock,data,latch):
	numberHere = value
	for i in range(0,numbersToRun):
		if decimal==3:
			postNumber(numberHere,randint(0,2),clock,data)
		else:
			postNumber(numberHere,decimal,clock,data)
	GPIO.output(latch,GPIO.LOW)
	GPIO.output(latch,GPIO.HIGH)

def reset(num,decimal):
	showNum(num,0,14,segmentClock1,segmentData1,segmentLatch1)
	showNum(num,0,14,segmentClock2,segmentData2,segmentLatch2)
	showNum(num,0,14,segmentClock3,segmentData3,segmentLatch3)
	showNum(num,0,14,segmentClock4,segmentData4,segmentLatch4)
	
def blowShow(value,decimal,numbersToRun,clock,data,latch):
	#reset(10,0)
	showNum(value,3,3,clock,data,latch)
        time.sleep(0.05)
	showNum(value,3,4,clock,data,latch)
        time.sleep(0.05)
	showNum(value,3,3,clock,data,latch)
        time.sleep(0.05)
	showNum(value,3,4,clock,data,latch)
        time.sleep(0.2)
	showNum(10,3,3,clock,data,latch)
        time.sleep(0.05)
	showNum(10,3,4,clock,data,latch)
        time.sleep(0.05)
	showNum(10,3,3,clock,data,latch)
        time.sleep(0.05)
	showNum(10,3,4,clock,data,latch)
        time.sleep(0.05)


x=0
showNumber = 0
reset(10,0)


while True:
	
	reset(10,0)
	if x%4==0:
		blowShow(showNumber,1,14,segmentClock1,segmentData1,segmentLatch1)
	elif x%4==1:
		blowShow(showNumber,1,14,segmentClock2,segmentData2,segmentLatch2)
	elif x%4==2:
		blowShow(showNumber,1,14,segmentClock3,segmentData3,segmentLatch3)
	elif x%4==3:
		blowShow(showNumber,1,14,segmentClock4,segmentData4,segmentLatch4)
	
	#print(showNumber)
	showNumber+=1
	x+=1
	if showNumber>=10:
		showNumber=0
		for i in range(0,100):	
			showNumber+=1
			showNumber%=50
			showNum(showNumber,randint(0,2),4,segmentClock1,segmentData1,segmentLatch1)
	        	showNum(showNumber,randint(0,2),4,segmentClock2,segmentData2,segmentLatch2)
        		showNum(showNumber,randint(0,2),4,segmentClock3,segmentData3,segmentLatch3)
        		showNum(showNumber,randint(0,2),4,segmentClock4,segmentData4,segmentLatch4)
			time.sleep(0.1)
	
		for i in range(0,500):
			reset(10,0)
			date_time = datetime.datetime.now()
			dateNow = date_time.date()
			timeNow = date_time.time()
			
			reset(10,0)
			showNum(timeNow.hour/10,0,1,segmentClock2,segmentData2,segmentLatch2)
			showNum(10,0,4,segmentClock2,segmentData2,segmentLatch2)
			showNum(timeNow.hour%10,1,1,segmentClock2,segmentData2,segmentLatch2)
			showNum(10,0,8,segmentClock2,segmentData2,segmentLatch2)

			showNum(10,0,6,segmentClock1,segmentData1,segmentLatch1)
                	showNum(timeNow.minute/10,0,1,segmentClock1,segmentData1,segmentLatch1)
                        showNum(timeNow.minute%10,1,1,segmentClock1,segmentData1,segmentLatch1)
                        showNum(10,0,6,segmentClock1,segmentData1,segmentLatch1)

			showNum(10,0,10,segmentClock1,segmentData4,segmentLatch4)
                	showNum(timeNow.second/10,1,1,segmentClock4,segmentData4,segmentLatch4)
			showNum(10,0,2,segmentClock4,segmentData4,segmentLatch4)
			showNum(timeNow.second%10,0,1,segmentClock4,segmentData4,segmentLatch4)
			showNum(10,0,0,segmentClock1,segmentData4,segmentLatch4)

			showNum(10,0,10,segmentClock3,segmentData3,segmentLatch3)
                        showNum(timeNow.microsecond%10,1,1,segmentClock3,segmentData3,segmentLatch3)
			showNum(timeNow.microsecond%10,0,1,segmentClock3,segmentData3,segmentLatch3)
                        showNum(10,0,2,segmentClock3,segmentData3,segmentLatch3)
			
                	time.sleep(0.1)
			reset(10,0)
GPIO.cleanup()

