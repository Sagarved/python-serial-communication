#!/usr/bin/python
import serial
import time
import sys

def read(endpoint):
   port = '/dev/tty.usbserial-'+str(endpoint)
   print port
   port_r = serial.Serial(port, baudrate=115200)
   while True:
       data = port_r.read_until()
       data = data.strip('\n')
       time_date = (time.strftime('%d/%m/%Y %H:%M:%S'))
       
       print ("<{0}> {1}").format(time_date,data)

#port.close()
if __name__ == "__main__":
    read(sys.argv[1])

