#! /usr/bin/python3
#-*-coding:Utf-8 -*

import RPi.GPIO as GPIO
import time
from RPLCD.gpio import CharLCD

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 


def distance(affichage=False,console=False,stockage=False):
    lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23]) #BOARD
    GPIO_TRIGGER = 40
    GPIO_ECHO = 38
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
   # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
    print(StartTime)
    print(StartTime)
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        time.sleep(1)
        print(GPIO.input(GPIO_ECHO))
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    print(TimeElapsed)
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    print(distance)
    return distance
 
"""
    while True:
        if console == True:
            print('Distance : ', sensor.distance, 'm')
            sleep(0.2)
        if affichage == True:
            lcd.cursor_pos = (0, 0)
            lcd.write_string("Distance : ")
            lcd.cursor_pos = (1, 0)
            lcd.write_string(sensor.distance + 'm')
"""
distance(False,True,True)