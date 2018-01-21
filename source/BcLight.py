import RPi.GPIO as GPIO
import time
import datetime
from random import randint
import sc
lFL1 = [[-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1], [3, 4], [3, 4, 5, 13], [3, 4, 5, 6, 13], [1, 2, 3, 4, 5, 6, 13], [1, 2, 3, 4, 5, 6, 12, 13], [0, 1,
                                                                                                                                                            2, 3, 4, 5, 6, 7, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]  # A
lFL2 = [[10], [9, 10], [7, 9, 10, 11], [7, 8, 9, 10, 11], [0, 7, 8, 9, 10, 11, 12], [0, 1, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 3, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]
lFL3 = [[-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1], [11], [3, 4, 11], [2, 3, 4, 6, 11], [2, 3, 4, 5, 6, 11, 13], [1, 2, 3, 4, 5, 6, 11, 12, 13], [0, 1, 2, 3, 4,
                                                                                                                                                            5, 6, 7, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]  # C
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
    else:
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
    showNumWithLatch(num, decimal, 14, segmentClock1, segmentData1, segmentLatch1)
    showNumWithLatch(num, decimal, 14, segmentClock2, segmentData2, segmentLatch2)
    showNumWithLatch(num, decimal, 14, segmentClock3, segmentData3, segmentLatch3)
    showNumWithLatch(num, decimal, 14, segmentClock4, segmentData4, segmentLatch4)


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


def showNumLtoR(sec, row, count, clock, data, latch, mode):
    GPIO.output(latch, GPIO.LOW)
    for i in range(0, 14):
        check = -1
        for element in row:
            if element == i:
                check = 1

        if mode == 0:
            if check == 1:
                postNumber(count, 1, clock, data)
            else:
                postNumber(10, 0, clock, data)

        elif mode == 1:
            if check == 1:
                postNumber(10, 1, clock, data)
            else:
                postNumber(8, 1, clock, data)

        elif mode == 2:
            if check == 1:
                postNumber(10, 0, clock, data)
            else:
                postNumber(10, 1, clock, data)
    GPIO.output(latch, GPIO.HIGH)

def leftToRight(mode):
    if mode == 0:
        randTime = 5
    else:
        randTime = 1
    for row in range(0, 18):
        for now in range(0, randTime):
            showNumLtoR(1, lFL1[row], randint(
                0, 9), segmentClock1, segmentData1, segmentLatch1, mode)
            showNumLtoR(2, lFL2[row], randint(
                0, 9), segmentClock2, segmentData2, segmentLatch2, mode)
            showNumLtoR(3, lFL3[row], randint(
                0, 9), segmentClock3, segmentData3, segmentLatch3, mode)
            showNumLtoR(4, lFL4[row], randint(
                0, 9), segmentClock4, segmentData4, segmentLatch4, mode)
            time.sleep(0.05)
x = 0
showNumber = 0

while True:
    sc.showLeftToRight()
        
GPIO.cleanup()
