from simple import MQTTClient
import ssl
from time import sleep


class sslWrap:
    def __init__(self):
        self.wrap_socket = ssl.wrap_socket


def connect_mqtt(mqtt_server, mqtt_user, mqtt_pass):
    client = MQTTClient(
        client_id="pico",
        server= mqtt_server,
        port=8883,
        user=mqtt_user,
        password=mqtt_pass,
        keepalive=3000, 
        ssl=sslWrap()     
    )
    print(client)
    client.connect()
    print("connected to MQTT")
    return client


import network


def connect_internet(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    # Disconnect due to connection issue
    # wlan.disconnect()
    if not wlan.isconnected():
        wlan.active(True)
        if not password:
            wlan.connect(ssid)
        else:
            wlan.connect(ssid, password)
        while wlan.isconnected() == False:
           # print(wlan.status(), network.STAT_CONNECTING, network.STAT_CONNECT_FAIL, network.STAT_WRONG_PASSWORD, network.STAT_NO_AP_FOUND)
            print('Waiting for connection...')
            sleep(1)
            
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip
