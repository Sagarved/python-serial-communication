#!/usr/bin/python2.7
import sys
import glob
import serial
print 'hello World'

def serial_intro():
    """ Detect serial port and get logs

        :
    """
    if sys.platform.startswith('win'):
        print 'windows'
    elif sys.platform.startswith('darwin'):
        print 'mac'
        ports = glob.glob('/dev/tty.*')
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    print result




if __name__ == "__main__":
    serial_intro()
