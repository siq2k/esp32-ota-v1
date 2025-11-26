import machine
import time

led = machine.Pin(12, machine.Pin.OUT)

for i in range(5):
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)