import control_lcd
import machine
from lcd_api import LcdApi
import time
from i2c_lcd import I2cLcd

"""
def log(missatge):
    print(missatge)
"""

def log(missatge):
    pin_sda = machine.Pin(21)
    pin_scl = machine.Pin(22)

    adreca_i2c = 0x27
    num_files = 2
    num_columnes = 16

    i2c = machine.SoftI2C(scl = pin_scl, sda = pin_sda, freq = 10000)

    lcd = I2cLcd(i2c, adreca_i2c, num_files, num_columnes)

    control_lcd.escriure_lcd(missatge, lcd)