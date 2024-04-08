# Bibliotheken laden
from rotary import Rotary

# GPIOs zum Rotary Encoder
pin_dt = 18
pin_clk = 19
pin_sw = 17

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
        print('Rechts (', value, ')')
    elif change == Rotary.ROT_CCW:
        value = value - 1
        if (value <= 0):
            value = 0
        print('Links (', value, ')')
    elif change == Rotary.SW_PRESS:
        print('Gedrückt')
    elif change == Rotary.SW_RELEASE:
        print('Losgelassen')

# Wenn der Encoder bedient wird
rotary.add_handler(rotary_changed)