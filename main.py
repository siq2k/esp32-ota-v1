import machine
import time
from ota import OTAUpdater

import ssd1306

i2c = machine.I2C(scl=machine.Pin(22),sda=machine.Pin(21))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Hello-World_1',0,0)

oled.show()

led = machine.Pin(12, machine.Pin.OUT)

while True:
    for i in range(100):
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)
    ota_updater.download_and_install_update_if_available()