import serial
import time
import sys
import fnmatch


def auto_detect_serial_unix(preferred_list=['*']):
    '''try to auto-detect serial ports on win32'''
    import glob
    glist = glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyACM*')
    ret = []

    # try preferred ones first
    for d in glist:
        for preferred in preferred_list:
            if fnmatch.fnmatch(d, preferred):
                ret.append(d)
    if len(ret) > 0:
        return ret
    # now the rest
    for d in glist:
        ret.append(d)
    return ret

def main():

    print "Opening serial port"
    print ""

    available_ports = auto_detect_serial_unix()
    port = serial.Serial(available_ports[0], 9600,timeout=1)
    print port.name


    arduino = serial.Serial(port.name, 9600, timeout = 1);
    time.sleep(2);

    for arg in sys.argv:
        command = arg

    arduino.write(command);

    print (arduino.read(100))

    print ""
    print "Finished"

    return 0

main()
