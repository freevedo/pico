from cumulocity_pico import connect,run_mqtt
#,open_socket,


#wlan connection credentials
# ssid = "Bbox-6DDA6FB5"
# password = 'v461CkSY62tvR7SPZL'
ssid = "TP-LINK_1ACE"
password = 'JeanDenise55'

try:
     ip = connect(ssid,password)
     #connection = open_socket(ip)
     run_mqtt()
except KeyboardInterrupt:
    machine.reset()