import gc
import os
from machine import ADC,unique_id
import ujson
import ubinascii

def get_data():
    
    #  Get on-board temperature sensor details
    sensor_temp = ADC(4)
    conversion_factor = 3.3 / (65535)
    reading = sensor_temp.read_u16() * conversion_factor

    temperature = 27 - (reading - 0.706)/0.001721

    # Get disk info
    disk_info = os.statvfs('//')

    # Get RAM info
    free_ram = gc.mem_free()
    used_ram = gc.mem_alloc()
    total_ram= free_ram+used_ram

    # Cretae a JSON string
    return ujson.dumps({
        "ID": ubinascii.hexlify(unique_id()).decode('utf-8'),
        "sensors":[{
            "type": "temperature",
            "value":temperature,
            "unit":"C"
        }],
        "memory":{
            "DISK":{
                "total":(disk_info[0]*disk_info[2])/1048576,
                "used":(disk_info[0]*disk_info[3])/1048576,
                "unit": "MB"
            },
            "RAM":{
                "used":used_ram,
                "total": total_ram,
                "unit": "B"
            }
        }
    })