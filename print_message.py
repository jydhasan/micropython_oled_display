# Complete project details at https://RandomNerdTutorials.com

from machine import Pin, SoftI2C
import ssd1306
from time import sleep

# ESP32 Pin assignment 
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

# ESP8266 Pin assignment
#i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

def print_text(msg,x,y,clr):
    if clr:
        oled.fill(0)
    oled.text(msg, x, y)
    oled.show()