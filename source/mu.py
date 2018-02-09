import RPi.GPIO as GPIO
import time
import datetime
import random
from random import randint

lFL1 = [[-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1], [3, 4], [3, 4, 5, 13], [3, 4, 5, 6, 13], [1, 2, 3, 4, 5, 6, 13], [1, 2, 3, 4, 5, 6, 12, 13], [0, 1,2, 3, 4, 5, 6, 7, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]  # A
lFL2 = [[10], [9, 10], [7, 9, 10, 11], [7, 8, 9, 10, 11], [0, 7, 8, 9, 10, 11, 12], [0, 1, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 3, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]
lFL3 = [[-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1], [11], [3, 4, 11], [2, 3, 4, 6, 11], [2, 3, 4, 5, 6, 11, 13], [1, 2, 3, 4, 5, 6, 11, 12, 13], [0, 1, 2, 3, 4,5, 6, 7, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]  # C
lFL4 = [[-1], [10, 11], [9, 10, 11], [7, 8, 9, 10, 11, 12], [7, 8, 9, 10, 11, 12, 13], [2, 6, 7, 8, 9, 10, 11, 12, 13], [0, 2, 6, 7, 8, 9, 10, 11, 12, 13], [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]  # D

BlFL1 = [[-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1], [3, 4],
         [5, 13], [6], [1, 2], [12], [0, 7], [11], [8, 9], [10]]  # A
BlFL2 = [[10], [9], [7, 11], [8], [0, 12], [1, 6, 13], [3], [2, 5],
         [4], [-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1]]  # B
BlFL3 = [[-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1], [11],
         [3, 4], [2, 6], [5, 13], [1, 12], [0, 7], [8, 9], [10], [-1]]  # C
BlFL4 = [[-1], [10, 11], [9], [7, 8, 12], [13], [2, 6], [0], [3, 4, 5],
         [1], [-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1]]  # D

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
    """
    if number==1:
        segments = a
    elif number==2:
        segments = b
    elif number==3:
        segments = c
    elif number==4:
        segments = d
    elif number==5:
        segments = e
    elif number==6:
        segments = f
    elif number==7:
        segments = g
    elif number==8:
        segments = dp
    elif number==9:
        segments = 0
    """
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
def showNumWithLatchaSeg(value, decimal, numbersToRun, seg):

    if seg == 0:
        clock = segmentClock1
        data = segmentData1
        latch = segmentLatch1
    elif seg ==1:
        clock = segmentClock2
        data = segmentData2
        latch = segmentLatch2
    elif seg ==2:
        clock = segmentClock3
        data = segmentData3
        latch = segmentLatch3
    elif seg ==3:
        clock = segmentClock4
        data = segmentData4
        latch = segmentLatch4

    GPIO.output(latch, GPIO.LOW)
    numberHere = value
    for i in range(0, numbersToRun):
        if decimal == 3:
            postNumber(numberHere, randint(0, 2), clock, data)
        else:
            postNumber(numberHere, decimal, clock, data)
    GPIO.output(latch, GPIO.HIGH)



def reset(num, decimal):
    showNumWithLatch(num, decimal, 14, segmentClock1, segmentData1, segmentLatch1)
    showNumWithLatch(num, decimal, 14, segmentClock2, segmentData2, segmentLatch2)
    showNumWithLatch(num, decimal, 14, segmentClock3, segmentData3, segmentLatch3)
    showNumWithLatch(num, decimal, 14, segmentClock4, segmentData4, segmentLatch4)

def rhythm():
    flag = randint(0,6)
    lightFlag = randint(13,18)
    blowShow(lightFlag,0,0,randint(0,6))
    
def blowShow(value, decimal, numbersToRun, which):
    # reset(10,0)
    if which < 4:
        showNumWithLatchaSeg(value, 3, 3, which)
        time.sleep(0.05)
        showNumWithLatchaSeg(value, 3, 4, which)
        time.sleep(0.05)
        showNumWithLatchaSeg(value, 3, 3, which)
        time.sleep(0.05)
        showNumWithLatchaSeg(value, 3, 4, which)
        time.sleep(0.2)
        value = 10
        showNumWithLatchaSeg(value, 0, 3, which)
        time.sleep(0.05)
        showNumWithLatchaSeg(value, 0, 4, which)
        time.sleep(0.05)
        showNumWithLatchaSeg(value, 0, 3, which)
        time.sleep(0.05)
        showNumWithLatchaSeg(value, 0, 4, which)    
        time.sleep(0.05)
    elif which <= 5:
        day = 0
        if which == 4:
            day = 0
        elif which == 5:
            day = 2
    
        showNumWithLatchaSeg(value, 3, 3, day)
        showNumWithLatchaSeg(value, 3, 3, day+1)
        time.sleep(0.05)
        showNumWithLatchaSeg(value, 3, 4, day)
        showNumWithLatchaSeg(value, 3, 4, day+1)
        time.sleep(0.05)
        showNumWithLatchaSeg(value, 3, 3, day)
        showNumWithLatchaSeg(value, 3, 3, day+1)
        time.sleep(0.05)
        showNumWithLatchaSeg(value, 3, 4, day)
        showNumWithLatchaSeg(value, 3, 4, day+1)
        time.sleep(0.2)
        value = 10
        showNumWithLatchaSeg(value, 0, 3, day)
        showNumWithLatchaSeg(value, 0, 3, day+1)
        time.sleep(0.05)
        showNumWithLatchaSeg(value,0, 4, day)
        showNumWithLatchaSeg(value,0, 4, day+1)
        time.sleep(0.05)
        showNumWithLatchaSeg(value,0, 3, day)
        showNumWithLatchaSeg(value,0, 3, day+1)
        time.sleep(0.05)
        showNumWithLatchaSeg(value,0, 4, day)
        showNumWithLatchaSeg(value,0, 4, day+1)    
        time.sleep(0.05)
    elif which <= 7:
        day = 0
        if which == 6:
            day = 0
        elif which == 7:
            day = 1
        
        showNumWithLatchaSeg(value, 3, 3, day)
        showNumWithLatchaSeg(value, 3, 3, day+2)
        time.sleep(0.05)
        showNumWithLatchaSeg(value, 3, 4, day)
        showNumWithLatchaSeg(value, 3, 4, day+2)
        time.sleep(0.05)
        showNumWithLatchaSeg(value, 3, 3, day)
        showNumWithLatchaSeg(value, 3, 3, day+2)
        time.sleep(0.05)
        showNumWithLatchaSeg(value, 3, 4, day)
        showNumWithLatchaSeg(value, 3, 4, day+2)
        time.sleep(0.2)
        value = 10
        showNumWithLatchaSeg(value, 0, 3, day)
        showNumWithLatchaSeg(value, 0, 3, day+2)
        time.sleep(0.05)
        showNumWithLatchaSeg(value,0, 4, day)
        showNumWithLatchaSeg(value,0, 4, day+2)
        time.sleep(0.05)
        showNumWithLatchaSeg(value,0, 3, day)
        showNumWithLatchaSeg(value,0, 3, day+2)
        time.sleep(0.05)
        showNumWithLatchaSeg(value,0, 4, day)
        showNumWithLatchaSeg(value,0, 4, day+2)
        time.sleep(0.05)

    
def showNumLtoR(sec,lastRow, row, count, clock, data, latch, mode):
    GPIO.output(latch, GPIO.LOW)
    for i in range(0, 14):
        check = -1
        flagForLastRow = 0
        for element in lastRow:
            if element == i:
                flagForLastRow = 1
        if flagForLastRow == 0:
            check = 2
        for element in row:
            if element == i:
                check = 1

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
                postNumber(10,0,clock,data)
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
    numberOrNot = 1    #1for Not
    
    if mode == 0 and numberOrNot==1:
        randTime = 160
    elif mode == 0 and numberOrNot==0:
        randTime = 24
    elif mode==1 and numberOrNot==1:
        randTime = 160
    elif mode==1 and numberOrNot==0:
        randTime = 24
    elif mode == 3:
        randTime = 1
    elif mode == 4:
        randTime = 2
    else:
        randTime = 8

    for row in range(17,-1,-1):
        k = row
        if mode == 1:
            for now in range(randTime-1, -1, -1):
                if numberOrNot ==1:
                    showNumLtoR(1,lFL1[k],BlFL1[row], int(now/int(randTime/8))+11, segmentClock1, segmentData1, segmentLatch1, mode)
                    showNumLtoR(2,lFL2[k],BlFL2[row], int(now/int(randTime/8))+11, segmentClock2, segmentData2, segmentLatch2, mode)
                    showNumLtoR(3,lFL3[k],BlFL3[row], int(now/int(randTime/8))+11, segmentClock3, segmentData3, segmentLatch3, mode)
                    showNumLtoR(4,lFL4[k],BlFL4[row], int(now/int(randTime/8))+11, segmentClock4, segmentData4, segmentLatch4, mode)
                    time.sleep(0.15)
                else:
                    showNumLtoR(1,lFL1[k],BlFL1[row], randint(0,9), segmentClock1, segmentData1, segmentLatch1, mode)
                    showNumLtoR(2,lFL2[k],BlFL2[row], randint(0,9), segmentClock2, segmentData2, segmentLatch2, mode)
                    showNumLtoR(3,lFL3[k],BlFL3[row], randint(0,9), segmentClock3, segmentData3, segmentLatch3, mode)
                    showNumLtoR(4,lFL4[k],BlFL4[row], randint(0,9), segmentClock4, segmentData4, segmentLatch4, mode)
                    time.sleep(1)
        else:
            for now in range(0, randTime):
                if numberOrNot ==1:
                    showNumLtoR(1,lFL1[k],BlFL1[row], int(now/int(randTime/8))+11, segmentClock1, segmentData1, segmentLatch1, mode)
                    showNumLtoR(2,lFL2[k],BlFL2[row], int(now/int(randTime/8))+11, segmentClock2, segmentData2, segmentLatch2, mode)
                    showNumLtoR(3,lFL3[k],BlFL3[row], int(now/int(randTime/8))+11, segmentClock3, segmentData3, segmentLatch3, mode)
                    showNumLtoR(4,lFL4[k],BlFL4[row], int(now/int(randTime/8))+11, segmentClock4, segmentData4, segmentLatch4, mode)
                    time.sleep(0.15)
                else:
                    showNumLtoR(1,lFL1[k],BlFL1[row], randint(0,9), segmentClock1, segmentData1, segmentLatch1, mode)
                    showNumLtoR(2,lFL2[k],BlFL2[row], randint(0,9), segmentClock2, segmentData2, segmentLatch2, mode)
                    showNumLtoR(3,lFL3[k],BlFL3[row], randint(0,9), segmentClock3, segmentData3, segmentLatch3, mode)
                    showNumLtoR(4,lFL4[k],BlFL4[row], randint(0,9), segmentClock4, segmentData4, segmentLatch4, mode)
                    time.sleep(1)

def starShine(duration):
    for i in range(0, duration*10):
        showNumber = 8
        showNumWithLatch(showNumber, randint(0, 2), 4,
                segmentClock1, segmentData1, segmentLatch1)
        showNumWithLatch(showNumber, randint(0, 2), 4,
                segmentClock2, segmentData2, segmentLatch2)
        showNumWithLatch(showNumber, randint(0, 2), 4,
                segmentClock3, segmentData3, segmentLatch3)
        showNumWithLatch(showNumber, randint(0, 2), 4,
                segmentClock4, segmentData4, segmentLatch4)
        time.sleep(0.1)

def showTime():
    date_time = datetime.datetime.now()
    dateNow = date_time.date()
    timeNow = date_time.time()

    GPIO.output(segmentLatch2, GPIO.LOW)
    showNum(int(timeNow.hour / 10), 0, 1, segmentClock2,segmentData2, segmentLatch2)
    showNum(10, 0, 4, segmentClock2, segmentData2, segmentLatch2)
    showNum(timeNow.hour % 10, 1, 1, segmentClock2,segmentData2, segmentLatch2)
    showNum(10, 0, 8, segmentClock2, segmentData2, segmentLatch2)
    GPIO.output(segmentLatch2, GPIO.HIGH)

    GPIO.output(segmentLatch1, GPIO.LOW)
    showNum(10, 0, 6, segmentClock1, segmentData1, segmentLatch1)
    showNum(int(timeNow.minute / 10), 0, 1, segmentClock1,segmentData1, segmentLatch1)
    showNum(timeNow.minute % 10, 1, 1, segmentClock1,segmentData1, segmentLatch1)
    showNum(10, 0, 6, segmentClock1, segmentData1, segmentLatch1)
    GPIO.output(segmentLatch1, GPIO.HIGH)

    GPIO.output(segmentLatch4, GPIO.LOW)
    showNum(10, 0, 10, segmentClock4, segmentData4, segmentLatch4)
    showNum(int(timeNow.second/10), 0, 1, segmentClock4,segmentData4,segmentLatch4)
    showNum(10, 0, 2, segmentClock4, segmentData4, segmentLatch4)
    showNum(timeNow.second%10, 1, 1, segmentClock4,segmentData4, segmentLatch4)
    GPIO.output(segmentLatch4, GPIO.HIGH)

    GPIO.output(segmentLatch3, GPIO.LOW)
    showNum(10, 0, 10, segmentClock3, segmentData3, segmentLatch3)
    showNum(int(timeNow.microsecond/100)%10, 0, 1, segmentClock3, segmentData3, segmentLatch3)
    showNum(timeNow.microsecond%10, 1, 1, segmentClock3, segmentData3, segmentLatch3)
    showNum(10, 0, 2, segmentClock3, segmentData3, segmentLatch3)
    GPIO.output(segmentLatch3, GPIO.HIGH)

    time.sleep(0.1)

def showLeftToRight():
    reset(10,0)
    
    for i in range(0,1):
        reset(10,0)
        time.sleep(4)
        leftToRight(0)  # 0 light to right
        reset(8, 1)
        time.sleep(10)
        starShine(20)
        reset(8,1)
        time.sleep(10)
        leftToRight(1)  # 2 lights off
        reset(10,0)
        time.sleep(4)


