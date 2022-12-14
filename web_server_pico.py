from functions import connect,run_mqtt
#,open_socket,


#wlan connection credentials
ssid = "TP-LINK_1ACE"
password = 'JeanDenise55'

try:
     ip = connect(ssid,password)
     #connection = open_socket(ip)
     run_mqtt()
except KeyboardInterrupt:
    machine.reset()