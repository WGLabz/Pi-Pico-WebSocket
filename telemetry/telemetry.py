import gc
import os
from machine import ADC,unique_id
import ujson
import ubinascii

def get_data():
    sensor_temp = ADC(4)
    conversion_factor = 3.3 / (65535)
    reading = sensor_temp.read_u16() * conversion_factor

    temperature = 27 - (reading - 0.706)/0.001721
    
    s = os.statvfs('//')

    F = gc.mem_free()
    A = gc.mem_alloc()
    T = F+A
    P = '{0:.2f}%'.format(F/T*100)

    # Cretae a JSON string
    return ujson.dumps({
        "ID": ubinascii.hexlify(unique_id()).decode('utf-8'),
        "sensors":[{
            "type": "temperature",
            "value":temperature,
            "unit":"C"
        }],
        "memory":{
            "RAM":{
                "total":(s[0]*s[2])/1048576,
                "used":(s[0]*s[3])/1048576,
                "unit": "MB"
            },
            "DISK":{
                "used":F,
                "total": T,
                "unit": "B"
            }
        }
    })