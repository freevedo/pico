# importing the required libraries
from machine import Pin
from machine import PWM
import time

from rotary import Rotary

# GPIOs zum Rotary Encoder
pin_dt = 18
pin_clk = 19
pin_sw = 17

# initial varibale declaratins
frequency = 0
duty_cycle = 0



# pin declarations
pwmPin = Pin(15) # declare the pin for PWM output
pwmOutput = PWM(pwmPin) # define a PWM object


# Initialiserung Rotary Encoder
rotary = Rotary(pin_dt, pin_clk, pin_sw)
value = 0

# Funktion
def rotary_changed(change):
    global value
    if change == Rotary.ROT_CW:
        value = value + 1
        if(value >= 180):
            value = 180
    elif change == Rotary.ROT_CCW:
        value = value - 1
        if(value <= 0):
            value = 0
    elif change == Rotary.SW_PRESS:
        print('Gedrückt')
    elif change == Rotary.SW_RELEASE:
        print('Losgelassen')

# Wenn der Encoder bedient wird


# ask user for frequency
while True:
   frequency = float(input("Enter pwm frequency in Hz : "))#set the PWM frequency only once at the beginning
   if frequency >= 0:
    pwmOutput.freq(int(frequency))
    break
   else:
    print("frequency cannot be negative. Enter again ")
    continue
    



# function for asking duty_cycle input
def duty():
    duty_cycle = float(input("Enter duty_cycle in percentage : "))
    # crash when character is input
    # convert duty cycle % to micropython range 0 - 65025
    duty_cycle = int( duty_cycle * 65025 / 100  )
    print("duty_cycle = ", duty_cycle)
    return duty_cycle # returns the duty cycle (in integer)
    
  
  
  

# define function for PWM generation
def pwmGenerate(duty_cycle):
    duty_cycle = duty_cycle
    pwmOutput.duty_u16(duty_cycle)


rotary.add_handler(rotary_changed)
 
# generate the PWM signal with variable duty cycle 
while True:
    pwmOutput.freq(int(frequency))
    
    duty_cycle = duty() # duty cycle in integer
    # check user input for discrepancy
    if duty_cycle >= 0 and duty_cycle <= 65025:
        pwmGenerate(duty_cycle)
            
    else:
        print("Unsuitable range, please enter again")
        continue
    
    
    
    




