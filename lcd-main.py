from RPLCD.i2c import CharLCD
import time

lcd = CharLCD('PCF8574', 0x27)


lcd.write_string('juanjuanjuanjuanjuanjuanjuanjuanjuan')
time.sleep(5)
lcd.clear()
lcd.write_string('Hola Hola!')
time.sleep(1)
lcd.clear()
