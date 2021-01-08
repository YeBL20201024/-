# enc
import serial
if __name__ == "__main__":
    ser = serial.Serial('com1',115200,Timeout=1)
    ser.open()
    print(ser.name)
    print(ser.port)
    print(ser.baudrate)
    print(ser.bytesize)
    print(ser.parity)
    print(ser.stopbits)
    print(ser.timeout)
    print(ser.writeTimeout)
    print(ser.xonxoff)
    print(ser.rtscts)
    print(ser.dsrdtr)
    print(ser.interCharTimeout)
    ser.close()