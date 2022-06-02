import I2C_LCD_driver
from time import *
mylcd = I2C_LCD_driver.lcd()
while True:
    mylcd.lcd_display_string("Ponganos 100", 1)
    sleep(5)
    mylcd.lcd_clear()
    
    mylcd.lcd_display_string("O si no...", 2)
    sleep(1.5)
    mylcd.lcd_clear()
    