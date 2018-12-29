from RPLCD.gpio import CharLCD
from RPi import GPIO

lcd = CharLCD(pin_rs=6, pin_rw=15, pin_e=9, pins_data=[19, 16, 26, 20],
              numbering_mode=GPIO.BCM)
lcd.write_string('Hello world')
print 'Test'
