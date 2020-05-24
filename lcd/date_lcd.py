#!/usr/bin/env python3
#-- coding: utf-8 --

import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs
from RPLCD.gpio import CharLCD
import time


GPIO.setmode(GPIO.BOARD) #Définit le mode de numérotation (Board)
GPIO.setwarnings(False) #On désactive les messages d'alerte

lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

while True:
    lcd.cursor_pos = (0, 0)
    lcd.write_string("Date: %s" %time.strftime("%d/%m/%Y"))
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Heure: %s" %time.strftime("%H:%M:%S"))