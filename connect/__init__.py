import serial
import sys
import os
from serial.tools.list_ports import comports as list_serial_ports

default = {
    'ARDUINO':"VID:PID=2341:0043", # Works for Uno R3, untested on anything else
    'MICRO:BIT':"VID:PID=0D28:0204",'MICROBIT':"VID:PID=0D28:0204" # Now can use both 'micro:bit' and 'microbit'
    }

default = str(default)

filename = os.path.join(os.path.dirname(__file__),'data.txt')

def export(devices=None):
    if devices == None:
        return

    text = '{'
    for name,vid in devices.items():
        text += '"{}":"{}",'.format(name,vid)
    text =  text[0:len(text)-1]
    text += '}'

    file = open(filename,mode='w')
    file.write(text)
    file.close()

def getPort(device=None,deviceVID=None):
    devices = setup()
    if device != None:
        device = device.upper()
        try:
            name = devices[device]
        except:
            if deviceVID != None:
                devices[device] = deviceVID.upper()
            else:
                return None
            
    elif deviceVID == None:
        return None
    
    if deviceVID != None:
        name = deviceVID
        
    export(devices)
    
    ports = list_serial_ports()
    for port in ports:
        if name in port[2].upper():
            return port[0]
            
    return None

def connect(device=None,deviceVID=None,**kwargs):
    s = serial.Serial(getPort(device,deviceVID),**kwargs)
    s.close()
    return s

def reset():
    file = open(filename,mode='w')
    file.write(default)
    file.close()

def get_names():
    file = open(filename)
    text = file.read().splitlines()[0]
    file.close()
    devices = eval(text)
    return devices    

def openPort(port=None,**kwargs):
    try:
        kwargs['timeout']
    except:
        kwargs['timeout'] = 1
    
    s = serial.Serial(port,**kwargs)
    s.close()
    return s

def setup():
    while True:
        try:
            devices = get_names()
        except:
            reset()
            continue
        break

    return devices
