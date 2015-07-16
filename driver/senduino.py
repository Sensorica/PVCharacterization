import serial
import time
import sys

print "Opening serial port"
print ""

arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout = 1);
time.sleep(2);

for arg in sys.argv:
    command = arg

arduino.write(command);

print (arduino.read(100))

print ""
print "Finished"
