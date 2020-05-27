#! /usr/bin/python3
# # -*-coding:Utf-8 -*

import RPi.GPIO as GPIO
import os
import time
from RPLCD.gpio import CharLCD

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 

def test_boutons(affichage = False):
    listeB = [22,18,16]
    lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
    GPIO.setup(listeB[0],GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(listeB[1],GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(listeB[2],GPIO.IN, pull_up_down=GPIO.PUD_UP)
    lcd.clear()
    lcd.cursor_pos= (0,0)
    while True:
        lcd.cursor_pos = (0, 0)
        lcd.write_string("Boutons :      ")
        lcd.cursor_pos = (1, 0)
        lcd.write_string("1: o  2: o  3: o")
        bouton1 = GPIO.input(listeB[0])
        if bouton1 == False:
            print('Button 1 Pressed')
            lcd.cursor_pos = (1, 3)
            lcd.write_string("X")
        bouton2 = GPIO.input(listeB[1])
        if bouton2 == False:
            print('Button 2 Pressed')
            lcd.cursor_pos = (1, 9)
            lcd.write_string("X")
        bouton3 = GPIO.input(listeB[2])
        if bouton3 == False:
            print('Button 3 Pressed')
            lcd.cursor_pos = (1, 15)
            lcd.write_string("X")
        time.sleep(0.2)


test_boutons()