from machine import Pin
import time
from dht import DHT11

sensor = DHT11(Pin(2, Pin.OUT,Pin.PULL_DOWN))

while True:
    temp = sensor.temperature
    humidity = sensor.humidity
    print("TEMP: {}: ºC Humidity: {:.0f}%".format(temp,humidity))
    time.sleep(2)
    