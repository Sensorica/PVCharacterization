import serial
import time

print "Opening serial port"

arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout = 1);
time.sleep(2);

command = "GX100"
arduino.write(command);

print (arduino.read(100))
