import serial
import time


ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
time.sleep(0.1)
string = ("par angleOffsetPitch")
print(string)
ser.write(bytearray(string, 'ascii'))
time.sleep(1)

ser.flushInput()
incoming = ser.readline().decode('utf-8')
print(incoming)
incoming = incoming.strip()
print(incoming)
incoming = incoming.split(" ")
print(incoming)
incoming = incoming[1]
incoming = int(incoming)
print (incoming)

string = ("par angleOffsetRoll")
print(string)
ser.write(bytearray(string, 'ascii'))
time.sleep(1)

ser.flushInput()
incoming = ser.readline().decode('utf-8')
print(incoming)
incoming = incoming.strip()
print(incoming)
incoming = incoming.split(" ")
print(incoming)
incoming = incoming[1]
incoming = int(incoming)
print (incoming)



#string = incoming.split(" ")
#current_y = string[1]
#current_y = int(current_y)
#print (10*current_y)

