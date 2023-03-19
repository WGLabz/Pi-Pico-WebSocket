# main.py -- put your code here!
from machine import Pin

# The used lib from http://bit.ly/3n2t9il
import uwebsockets.ws_client
import os
import wifi

print(uwebsockets.client)
def hello():
    with uwebsockets.ws_client.connect('ws://192.168.0.103:1880/test/esp32') as websocket:

        uname = os.uname()
        name = '{sysname} {release} {version} {machine}'.format(
            sysname=uname.sysname,
            release=uname.release,
            version=uname.version,
            machine=uname.machine,
        )
        websocket.send(name)
        print("> {}".format(name))

        greeting = websocket.recv()
        print("< {}".format(greeting))

status_led = Pin("LED",Pin.OUT)

# Wi-Fi creds
wifi_ssid = 'MIFI_D094'
wifi_password = '1234567890'

wifi.connect_wifi(wifi_ssid,wifi_password,status_led)


hello()

