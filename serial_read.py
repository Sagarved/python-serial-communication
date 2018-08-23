#!/usr/bin/python
import serial
import time
import sys

"""This read.py stores logs with date and timestamp of host machine
   :param
         serial endpoint e.g: 5ae1119c2 from /dev/tty.usbserial-5ae1119c2
         new file name where logs needs to be stored
"""

def read(endpoint,new_file):
   port = '/dev/tty.usbserial-'+str(endpoint)
   print port
   port_r = serial.Serial(port, baudrate=115200)
   while True:
       data = port_r.read_until()
       time_date = (time.strftime('%d/%m/%Y %H:%M:%S')) 
       logs_data=("<{0}> {1}").format(time_date,data)
       write_file(new_file,logs_data)
       logs_data = logs_data.strip('\n')
       print logs_data
def write_file(new_file,logs_data):
    with open (new_file,'a') as fp:
        fp.write(logs_data)
#port.close()
if __name__ == "__main__":
    read(sys.argv[1],sys.argv[2])

