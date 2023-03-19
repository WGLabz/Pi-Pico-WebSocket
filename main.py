# main.py -- put your code here!
from machine import Pin, Timer
import wsclient
import os
from wifi import connect_wifi
import gc
from telemetry import get_data
import utime
from uwebsockets.protocol import AsyncWebsocketClient
import uasyncio as a

def send_data():
    print('Hello')
    data = get_data()
    socket.send('Hello Workd')


status_led = Pin("LED",Pin.OUT)

# Wi-Fi creds
wifi_ssid = 'MIFI_D094'
wifi_password = '1234567890'

# wi_fi = wifi.WiFiConnection()
connect_wifi(wifi_ssid,wifi_password,status_led)

websocket = AsyncWebsocketClient(200)

async def check():  
    print("hel")

    if not await websocket.connect("{}{}".format('ws://192.168.0.103:1880/test/esp32', randint(1, 100))):
            raise Exception('Handshake error.')
    print("...handshaked.")
# .connect('ws://192.168.0.103:1880/test/esp32')

# socket = wsclient.wsclient('ws://192.168.0.103:1880/test/esp32')
# socket.initialize('ws://192.168.0.103:1880/test/esp32')

# Data send
# data_send_timer = Timer()
# data_send_timer.init(period=10000, callback=send_data)

# while True:
#     if not websocket.open:
#         websocket = uwebsockets.ws_client.connect('ws://192.168.0.103:1880/test/esp32')

#     resp = websocket.recv()
#     print(resp)
#     # print(uwebsockets.ws_client.open)
    
#     data = get_data()
#     websocket.send(data)
    
#     utime.sleep(5) 

check()