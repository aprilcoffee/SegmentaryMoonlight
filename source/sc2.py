import RPi.GPIO as GPIO
import time
import datetime
from random import randint
# GPIO declarations
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
#Clock - E
segmentLatch5 = 5
segmentClock5 = 6
segmentData5 = 12

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(segmentClock1, GPIO.OUT)
    GPIO.setup(segmentLatch1, GPIO.OUT)
    GPIO.setup(segmentData1, GPIO.OUT)

    GPIO.output(segmentClock1, GPIO.LOW)
    GPIO.output(segmentLatch1, GPIO.LOW)
    GPIO.output(segmentData1, GPIO.LOW)

    GPIO.setup(segmentClock2, GPIO.OUT)
    GPIO.setup(segmentLatch2, GPIO.OUT)
    GPIO.setup(segmentData2, GPIO.OUT)

    GPIO.output(segmentClock2, GPIO.LOW)
    GPIO.output(segmentLatch2, GPIO.LOW)
    GPIO.output(segmentData2, GPIO.LOW)

    GPIO.setup(segmentClock3, GPIO.OUT)
    GPIO.setup(segmentLatch3, GPIO.OUT)
    GPIO.setup(segmentData3, GPIO.OUT)

    GPIO.output(segmentClock3, GPIO.LOW)
    GPIO.output(segmentLatch3, GPIO.LOW)
    GPIO.output(segmentData3, GPIO.LOW)

    GPIO.setup(segmentClock4, GPIO.OUT)
    GPIO.setup(segmentLatch4, GPIO.OUT)
    GPIO.setup(segmentData4, GPIO.OUT)

    GPIO.output(segmentClock4, GPIO.LOW)
    GPIO.output(segmentLatch4, GPIO.LOW)
    GPIO.output(segmentData4, GPIO.LOW)

    GPIO.setup(segmentClock5, GPIO.OUT)
    GPIO.setup(segmentLatch5, GPIO.OUT)
    GPIO.setup(segmentData5, GPIO.OUT)
    
    GPIO.output(segmentClock5, GPIO.LOW)
    GPIO.output(segmentLatch5, GPIO.LOW)
    GPIO.output(segmentData5, GPIO.LOW)

def postNumber(number, decimal, clock, data):
    # -A
                        # //F/B
    # -G
    # //E/C
    # -.D/DP
    a = 1 << 0
    b = 1 << 6
    c = 1 << 5
    d = 1 << 4
    e = 1 << 3
    f = 1 << 1
    g = 1 << 2
    dp = 1 << 7

    segments = 0
    if number == 1:
        segments = b | c
    elif number == 2:
        segments = a | b | d | e | g
    elif number == 3:
        segments = a | b | c | d | g
    elif number == 4:
        segments = f | g | b | c
    elif number == 5:
        segments = a | f | g | c | d
    elif number == 6:
        segments = a | f | g | e | c | d
    elif number == 7:
        segments = a | b | c
    elif number == 8:
        segments = a | b | c | d | e | f | g
    elif number == 9:
        segments = a | b | c | d | f | g
    elif number == 0:
        segments = a | b | c | d | e | f


    elif number > 10:
        s = random.sample(range(0,9),number%10)
        for i in s:
            flag = 1 << i
            segments = segments | flag
    elif number == 10:
        segments = 0
    
    if(decimal):
        segments |= dp

    # clock these bits out to the drivers
    n = 0
    while n < 8:
        GPIO.output(clock, GPIO.LOW)
        GPIO.output(data, segments & 1 << (7 - n))
        GPIO.output(clock, GPIO.HIGH)
        n += 1


def showNum(value, decimal, numbersToRun, clock, data, latch):
    #GPIO.output(latch, GPIO.LOW)
    numberHere = value
    for i in range(0, numbersToRun):
        if decimal == 3:
            postNumber(numberHere, randint(0, 2), clock, data)
        else:
            postNumber(numberHere, decimal, clock, data)
    #GPIO.output(latch, GPIO.HIGH)

def showNumWithLatch(value, decimal, numbersToRun, clock, data, latch):
    GPIO.output(latch, GPIO.LOW)
    numberHere = value
    for i in range(0, numbersToRun):
        if decimal == 3:
            postNumber(numberHere, randint(0, 2), clock, data)
        else:
            postNumber(numberHere, decimal, clock, data)
    GPIO.output(latch, GPIO.HIGH)


def reset(num, decimal):
    showNumWithLatch(num, decimal, 12, segmentClock1, segmentData1, segmentLatch1)
    showNumWithLatch(num, decimal, 12, segmentClock2, segmentData2, segmentLatch2)
    showNumWithLatch(num, decimal, 13, segmentClock3, segmentData3, segmentLatch3)
    showNumWithLatch(num, decimal, 13, segmentClock4, segmentData4, segmentLatch4)
    #showNumWithLatch(num, decimal, 6, segmentClock5, segmentData5, segmentLatch5)
def resetlight(num, decimal):
    showNumWithLatch(num, decimal, 6, segmentClock5, segmentData5, segmentLatch5)

def blowShow(value, decimal, numbersToRun, clock, data, latch):
    # reset(10,0)
    showNumWithLatch(value, 3, 3, clock, data, latch)
    time.sleep(0.05)
    showNumWithLatch(value, 3, 4, clock, data, latch)
    time.sleep(0.05)
    showNumWithLatch(value, 3, 3, clock, data, latch)
    time.sleep(0.05)
    showNumWithLatch(value, 3, 4, clock, data, latch)
    time.sleep(0.2)
    showNumWithLatch(10, 3, 3, clock, data, latch)
    time.sleep(0.05)
    showNumWithLatch(10, 3, 4, clock, data, latch)
    time.sleep(0.05)
    showNumWithLatch(10, 3, 3, clock, data, latch)
    time.sleep(0.05)
    showNumWithLatch(10, 3, 4, clock, data, latch)
    time.sleep(0.05)


def showNumLtoR(sec,lastRow, row, count, clock, data, latch, mode):
    GPIO.output(latch, GPIO.LOW)
    for i in range(0, 14):
        check = -1
        for element in row:
            if element == i:
                check = 1
        for element in lastRow:
            if element == i:
                check = 2

        if mode == 0:
            if check == 1:
                postNumber(count, 0, clock, data)
            elif check ==2:
                postNumber(8,1,clock,data)
            else:
                postNumber(10, 0, clock, data)

        elif mode == 1:
            if check == 1 :
                postNumber(count, 1, clock, data)
            elif check==2:
                postNumber(10,1,clock,data)
            else:
                postNumber(8, 1, clock, data)

        elif mode == 2:
            if check == 2:
                postNumber(10, 0, clock, data)
            else:
                postNumber(10, randint(0,2), clock, data)
        elif mode == 3:
            if check == 1:
                postNumber(10,1,clock,data)
            else:
                postNumber(8,1,clock,data)
        elif mode ==4:
            if check == 1:
                postNumber(10,0,clock,data)
            else :
                postNumber(10,1,clock,data)
    GPIO.output(latch, GPIO.HIGH)

def leftToRight(mode):
    if mode == 0:
        randTime = 20
    elif mode==1:
        randTime = 20
    elif mode == 3:
        randTime = 1
    elif mode == 4:
        randTime = 2
    else:
        randTime = 8
        
    for row in range(1, 18):
        for now in range(0, randTime):
            if row > 0:
                showNumLtoR(1,lFL1[row-1],BlFL1[row], randint(0, 9), segmentClock1, segmentData1, segmentLatch1, mode)
                showNumLtoR(2,lFL2[row-1],BlFL2[row], randint(0, 9), segmentClock2, segmentData2, segmentLatch2, mode)
                showNumLtoR(3,lFL3[row-1],BlFL3[row], randint(0, 9), segmentClock3, segmentData3, segmentLatch3, mode)
                showNumLtoR(4,lFL4[row-1],BlFL4[row], randint(0, 9), segmentClock4, segmentData4, segmentLatch4, mode)
                time.sleep(0.01)


def starShine(duration):
    for i in range(0, duration*10):
        showNumber = 10
        showNumWithLatch(showNumber, randint(0, 2), 4,
                segmentClock1, segmentData1, segmentLatch1)
        showNumWithLatch(showNumber, randint(0, 2), 4,
                segmentClock2, segmentData2, segmentLatch2)
        showNumWithLatch(showNumber, randint(0, 2), 4,
                segmentClock3, segmentData3, segmentLatch3)
        showNumWithLatch(showNumber, randint(0, 2), 4,
                segmentClock4, segmentData4, segmentLatch4)
        showTime()
        time.sleep(0.1)

def showTime():
    date_time = datetime.datetime.now()
    dateNow = date_time.date()
    timeNow = date_time.time()
    if timeNow.second % 2==0:
        de = 1
    else:
        de = 0


    GPIO.output(segmentLatch5, GPIO.LOW)
    showNum(timeNow.second%10, de, 1, segmentClock5,segmentData5, segmentLatch5)
    showNum(int(timeNow.second/10), de, 1, segmentClock5,segmentData5,segmentLatch5)

    showNum(timeNow.minute % 10, de, 1, segmentClock5,segmentData5, segmentLatch5)
    showNum(int(timeNow.minute / 10), de, 1, segmentClock5,segmentData5, segmentLatch5)
    
    showNum(timeNow.hour % 10,de, 1, segmentClock5,segmentData5, segmentLatch5)
    showNum(int(timeNow.hour / 10),de, 1, segmentClock5,segmentData5, segmentLatch5)
    
    GPIO.output(segmentLatch5, GPIO.HIGH)
    time.sleep(0.01)

def countDown():
    sec = 59
    millisec = 99
    microsec = 99
    while sec > 0:
        print ("%d:%d:%d" % (sec,millisec,microsec))
    
        GPIO.output(segmentLatch5, GPIO.LOW)
        showNum(randint(0,9), 0, 1, segmentClock5,segmentData5, segmentLatch5)
        showNum(randint(0,9), 0, 1, segmentClock5,segmentData5,segmentLatch5)

        showNum(millisec%10, 0, 1, segmentClock5,segmentData5, segmentLatch5)
        showNum(int(millisec / 10), 0, 1, segmentClock5,segmentData5, segmentLatch5)
    
        showNum(sec % 10,0, 1, segmentClock5,segmentData5, segmentLatch5)
        showNum(int(sec / 10),0, 1, segmentClock5,segmentData5, segmentLatch5)
        GPIO.output(segmentLatch5, GPIO.HIGH)
        millisec = millisec - 1
        if millisec < 0:
            millisec = 59
            sec = sec - 1
        time.sleep(0.01)
    print("out")    
def showLeftToRight():
    for i in range(0,3):
        leftToRight(0)  # 0 light to right
        reset(8, 1)
        for k in range(0,5):
            leftToRight(3)
        leftToRight(1)  # 1 dark to right
        for k in range(0,5):
            leftToRight(4)
        starShine(15)
        leftToRight(2)  # 2 lights off
        reset(10,0)
        time.sleep(3)

