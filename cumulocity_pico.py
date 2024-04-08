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
mqttBroker = "eu-latest.cumulocity.com"
clientId = "pico_w"
deviceName = "Raspberry pi pico w"
tenant = "t1447328366"
userIot = "freddy.guigma@softwareag.com"
username = tenant + "/" + userIot
userPwd = "W0rkStud3ntAtS@G2023"
mqttClient = 'pico_w'
mqttUser = 'picow'
mqttPW = 'picow'
mqttTopic = 'greenhouse_pico'

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

# publish a message
def publish(client,topic, message, wait_for_ack = False):
    QoS = 2 if wait_for_ack else 0
    client.publish(topic, message, QoS)
    if wait_for_ack:
        print(" > awaiting ACK for {}")
        client.wait_msg()
        print(" < received ACK for {}")

def mqttConnect():
    print("MQTT-Verbindung herstellen: %s mit %s als %s" % (mqttClient, mqttBroker, userIot))
    client = MQTTClient(clientId, mqttBroker, user=username, password=userPwd)
    client.connect()
    print()
    print('MQTT-Verbindung hergestellt')
    publish(client,"s/us", "100," + deviceName + ",c8y_MQTTDevice", wait_for_ack = True)
    publish(client,"s/us", "110,S123456789,MQTT test model,Rev0.1")
    publish(client,"s/us", "114,c8y_Restart")
    print("Device registered successfully!")
    print()
    return client


# send temperature measurement
    

def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def run_mqtt():
    try:
        client = mqttConnect()
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
           
            publish(client,"s/us", "211,{}".format(myValue))
            publish(client,"s/us", "200,c8y_Temperature_dht11,T,{}".format(temp))
            publish(client,"s/us", "200,c8y_Temperature_ds18b20,T,{}".format(digitalTemp))
            publish(client,"s/us", "200,c8y_Humidity,%,{}".format(humi))
            sleep(5)
    except OSError:
            print()
            print('Fehler: Keine MQTT-Verbindung')
            print()
        # 60 Sekunden warten
   
    
    




