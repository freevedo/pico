from machine import Pin, ADC, PWM
from time import sleep

#dc motor
pwmPIN=16
cwPin=14 
acwPin=15

#joystick
VRX = ADC(Pin(27))
VRY = ADC(Pin(26))
SW = Pin(22,Pin.IN, Pin.PULL_UP)

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
      
      
while True:
    xAxis = VRX.read_u16()
    yAxis = VRY.read_u16()
    switch = SW.value()
    
    print("X-axis: " + str(xAxis) + ", Y-axis: " + str(yAxis) + ", Switch " + str(switch))
    if switch == 0:
        print("Push button pressed!")
        motorMove(50,0,pwmPIN,cwPin,acwPin)#stop the motor
    print(" ")
    if(xAxis < 4000): #step forward
        motorMove(50,-1,pwmPIN,cwPin,acwPin)
    elif(xAxis > 55000):
        motorMove(50,1,pwmPIN,cwPin,acwPin)
    sleep(0.75)