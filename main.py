from machine import Pin, SoftI2C
import time
from ota import OTAUpdater

import ssd1306

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)
i2c.scan()
i2c.readfrom(0x3a, 4)   # read 4 bytes from device with address 0x3a
i2c.writeto(0x3a, '12') # write '12' to device with address 0x3a

buf = bytearray(10)     # create a buffer with 10 bytes
i2c.writeto(0x3a, buf)  # write the given buffer to the peripheral

led = Pin(12, Pin.OUT)

while True:
    for i in range(20):
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)
    ota_updater.download_and_install_update_if_available()