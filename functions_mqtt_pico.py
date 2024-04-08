import network
import socket
import json
from picozero import pico_temp_sensor, pico_led
import machine
from machine import Pin
from dht import DHT11
from utime import sleep, sleep_ms
from onewire import OneWire
from ds18x20 import DS18X20
from umqtt_simple import MQTTClient


#mqtt config
mqttBroker = "82.165.23.150" 
mqttClient = 'pico_w'
mqttUser = 'picow'
mqttPW = 'picow'
mqttTopic = 'serreLaafi2'

ldr = machine.ADC(27)

# Initialisierung GPIO und DHT11
sleep(1)
dht11_sensor = DHT11(Pin(14, Pin.IN, Pin.PULL_UP))

# Initialisierung GPIO, OneWire und DS18B20
one_wire_bus = Pin(16)
sensor_ds = DS18X20(OneWire(one_wire_bus))

# One-Wire-Geräte ermitteln
devices = sensor_ds.scan()
#print(devices)

#global
digitalTemp=""

#wlan connection credentials
ssid = "TP-LINK_1ACE"
password = 'JeanDenise55'


def connect(ssid, password):
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)#allow connection parmeter is interface id
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def mqttConnect():
    if mqttUser != '' and mqttPW != '':
        print("MQTT-Verbindung herstellen: %s mit %s als %s" % (mqttClient, mqttBroker, mqttUser))
        client = MQTTClient(mqttClient, mqttBroker, user=mqttUser, password=mqttPW)
    else:
        print("MQTT-Verbindung herstellen: %s mit %s" % (mqttClient, mqttBroker))
        client = MQTTClient(mqttClient, mqttBroker)
    client.connect()
    print()
    print('MQTT-Verbindung hergestellt')
    print()
    return client



def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def run_mqtt():
    # Funktion zur Taster-Auswertung
    while True:
        myValue  = pico_temp_sensor.temp
        #measure
        dht11_sensor.measure()
        # Werte lesen
        temp = dht11_sensor.temperature() 
        humi = dht11_sensor.humidity()
        # Temperatur messen
        sensor_ds.convert_temp()
        # Warten: min. 750 ms
        sleep_ms(750)
        
        # Sensoren abfragen
        for device in devices:
            digitalTemp =  sensor_ds.read_temp(device)
            
        iot_values = {
        "picoTemp" : myValue,
        "dht11Temp" : temp,
        "dht11Hum" : humi,
        "digitalTemp" : digitalTemp,
        "photoCell" : ldr.read_u16()
        }
        to_send = json.dumps(iot_values)
        try:
            client = mqttConnect()
            client.publish(mqttTopic, to_send)
            print("An Topic %s gesendet: %s" %  (mqttTopic, to_send))
            print()
            client.disconnect()
            print('MQTT-Verbindung beendet')
            print()
        except OSError:
            print()
            print('Fehler: Keine MQTT-Verbindung')
            print()
        # 60 Sekunden warten
        sleep(30)
    
    



