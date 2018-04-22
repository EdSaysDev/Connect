import connect as c

# You can always add your own devices.  You just need to know their P/V IDs

# ---------- You can use:

microbit = c.connect('micro-bit','VID:PID=0D28:0204',baudrate=115200)

microbit.open()

try:
    while True:
        print(microbit.read().decode(),end='')
except:
    microbit.close()


# ------------------------ OR ------------------------ #


port = c.getPort('micro-bit','VID:PID=0D28:0204')
microbit = c.openPort(port,baudrate=115200)

microbit.open()

try:
    while True:
        print(microbit.read().decode(),end='')
except:
    microbit.close()
