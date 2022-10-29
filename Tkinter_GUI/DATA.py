import serial
import time

def BigData():
    print("DATA file is OK, data sent")
    ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=1)
    cmd="AT+MODE=LWOTAA"
    ser.write(cmd.encode())
    print(ser.read(40))
    cmd="AT+DR=EU868"
    ser.write(cmd.encode())
    print(ser.read(40))
    cmd="AT+KEY=APPKEY,\"BE3D4D9951757E75A75F9D0DD2B8BC5E\""
    ser.write(cmd.encode())
    print(ser.read(40))
    cmd="AT+JOIN"
    ser.write(cmd.encode())
    print(ser.read(40))
    time.sleep(8)
    cmd="AT+CMSGHEX=\"4641524953\""
    ser.write(cmd.encode())
    msg=ser.read(64)
    print(msg)