import connect as c

# ---------- You can use:

microbit = c.connect('microbit',baudrate=115200)

if microbit.port != None:

    microbit.open()

    try:
        while True:
            print(microbit.read().decode(),end='')
    except:
        microbit.close()


# ------------------------ OR ------------------------ #


port = c.getPort('microbit')

if port != None:
    microbit = c.openPort(port,baudrate=115200)

    microbit.open()

    try:
        while True:
            print(microbit.read().decode(),end='')
    except:
        microbit.close()
