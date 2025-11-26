import machine
import time

led = machine.Pin(12, machine.Pin.OUT)

for i in range(10):
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)