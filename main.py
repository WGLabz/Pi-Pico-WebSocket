# main.py -- put your code here!
from machine import Pin
import wsclient
import os
from wifi import connect_wifi

status_led = Pin("LED",Pin.OUT)

# Wi-Fi creds
wifi_ssid = 'MIFI_D094'
wifi_password = '1234567890'

# wi_fi = wifi.WiFiConnection()
connect_wifi(wifi_ssid,wifi_password,status_led)

socket = wsclient.wsclient()
socket.initialize('ws://192.168.0.103:1880/test/esp32')

socket.send("Hello World")

