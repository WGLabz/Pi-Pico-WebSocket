import network

def connect_wifi(ssid,password,status_led):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    # Try to connect to wifi network
    max_connection_retry = 10
    while max_connection_retry > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_connection_retry -= 1
        print('waiting for connection...')
        time.sleep(1)

    # Connection status
    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
        status_led.value(0)
        return False;
    else:
        print('connected')
        status = wlan.ifconfig()
        print( 'ip = ' + status[0] )
        status_led.value(1)
        return True;


