# 'connect' Module

### Overview
'connect' is a module for connecting to devices via a serial connection.
See 'tests' directory for some examples of use.

### Functions of the module


The following functions are included in the module:


```python
connect.getPort(device=None,deviceVID=None)
```

Returns the port name (if available) of the specified device.

Example:

```python
import connect as c

print(c.getPort(device="micro:bit")) # or device="microbit"
```

```python
connect.connect(device=None,deviceVID=None,**kwargs)
```

Connects to the specified device (if available) and returns a closed 'serial.Serial' object.

Example:

```python
import connect as c

kwargs = { # serial.Serial kwargs
}

c.connect(device="arduino",**kwargs) # Returns a closed serial.Serial object
c.open() # Open port
c.close() # Close port
```

```python
connect.reset()
```

Resets the device data



**The following functions are for internal use:**

```python
connect.get_names()
```

Reads the data file

```python
connect.openPort(port=None,**kwargs)
```

Opens the specified port name

```python
connect.setup()
```

Is called at the beginning to set up everything

```python
connect.export(devices=None)'
```

Exports data to the text file.

### How to use the functions:


connect.getPort(device=None,deviceVID=None)

  This function returns the port name of the specified device.  If parameter 'device' is specified, it will look in its data for this device, and then use the data to find the port.
  
  If no device is specified, or cannot be found in the list, it returns the port of the device with the specified deviceVID value.  If there was a device parameter, it will store the data in its text file so as it can use it next time.
  
  If neither parameter is specified, it returns 'None', as it does when it cannot find the specified device.



connect.connect(device=None,deviceVID=None,**kwargs)
  
  This function returns a closed Serial object of the specfified device, using the port name given by the 'connect.getPort' function.
  It will, if no timeout value is specified, set a timeout value of '1'
  
  Methods:
    
The methods of 'connect' function are those of the standard 'serial.Serial' methods, since it returns a 'serial.Serial' object, and is not a inherentent class.



`connect.reset()`

  This function, quite simply, resets all device data.
  
  
### How to find your device's VID Value

##### Windows:

1. Go to Control Panel >> Hardware and Sound >> Devices and Printers, and then at the bottom are the USB devices.
2. By then double-clicking on the one wanted, a dialogue box opens. then went 'Hardware >> [Device] >> Properties', which opens up another dialogue box.
3. In this one, in the dropdown menu, there is the 'Device Instance Path', which gives a value similar to 'USB\VID_0D28&PID_0204&MI_01\9900023432044E45004A80190000002000000000CFCF28BD' (for a microbit), of which needs to be extracted 'VID_0D28&PID_0204', and then turned into the format of 'VID:PID=0D28:0204'.  This is the 'deviceVID' value.

### Package Information

The package is currently in development stage.

### Installation Instructions


Unfortunately, connect is not available on PyPI, so you will have to install it manually.  Please do not just run the 'setup.py' file with Python IDLE or suchlike, as this will not install it properly.  You must use 'pip' or similar.

To install:

1)  Download (if you haven't already) pip.
2)  Download the module as a zip.
3)  Extract the files.
4)  Open up a terminal window, and type "cd [the directory path of the setup.py file]" (excluding the quotation marks)
5)  Then type "pip install ." (again, excluding the quotation marks)

