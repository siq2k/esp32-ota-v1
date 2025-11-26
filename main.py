from machine import Pin, I2C
import time
from ota import OTAUpdater

import ssd1306

i2c = I2C(scl=Pin(22),sda=Pin(21))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.text('Hello-World_1', 0, 0, 1)
display.show()

led = Pin(12, Pin.OUT)

while True:
    for i in range(20):
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)
    ota_updater.download_and_install_update_if_available()