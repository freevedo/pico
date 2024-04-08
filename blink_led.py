from machine import Pin
import time
led = Pin("LED", Pin.OUT)

while True:
    #Turn on led
    led.value(1)
    # led on for 1s
    time.sleep(1)
    # Turn led off
    led.value(0)
    # led off for 2s
    time.sleep(2)
