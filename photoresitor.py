from machine import Pin
import time
 
ldr = machine.ADC(27)
 
while True:
     print(ldr.read_u16())
     time.sleep(2)