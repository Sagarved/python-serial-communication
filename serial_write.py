#!/usr/bin/python
import serial
import time
port = serial.Serial("/dev/tty.usbserial-5b3aa1dc3", baudrate=115200)
while True:
    data = port.write(b'tis 90')

    kl_response = port.read(999)
    time.sleep(10)
    print 'sleeping:'+ kl_response
    #data = port.write('tis 0')

port.close()

