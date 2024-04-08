from machine import Pin, PWM
from time import sleep

pwmPIN=16
cwPin=14 
acwPin=15

def motorMove(speed,direction,speedGP,cwGP,acwGP):
    if speed > 100: speed=100
    if speed < 0: speed=0
    Speed = PWM(Pin(speedGP))
    Speed.freq(50)
    cw = Pin(cwGP, Pin.OUT)
    acw = Pin(acwGP, Pin.OUT)
    Speed.duty_u16(int(speed/100*65536))
    if direction < 0:
      cw.value(0)
      acw.value(1)
    if direction == 0:
      cw.value(0)
      acw.value(0)
    if direction > 0:
      cw.value(1)
      acw.value(0)
      
motorMove(50,-1,pwmPIN,cwPin,acwPin)
sleep(5)
motorMove(50,0,pwmPIN,cwPin,acwPin)