# Bibliotheken laden
from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20
from utime import sleep, sleep_ms

# Initialisierung GPIO, OneWire und DS18B20
one_wire_bus = Pin(16)
sensor_ds = DS18X20(OneWire(one_wire_bus))

# One-Wire-Geräte ermitteln
devices = sensor_ds.scan()
#print(devices)

while True:
    # Temperatur messen
    sensor_ds.convert_temp()
    # Warten: min. 750 ms
    sleep_ms(750)
    # Sensoren abfragen
    for device in devices:
        print('Sensor:', device)
        print('Temperatur:', sensor_ds.read_temp(device), '°C')
    print()
    sleep(3)