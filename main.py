import machine
import time
from ota import OTAUpdater

led = machine.Pin(12, machine.Pin.OUT)

while True:
    for i in range(100):
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)
    ota_updater.download_and_install_update_if_available()