# 导入pyserial模块
import serial

# 打开串口
ser = serial.Serial('com1',115200,timeout=1)
# 关闭串口
ser.close()
# 打印设备名称
print(ser.name)
# 打印设备名
print(ser.port)
# 打开端口
ser.open()
# 从端口读数据
s = ser.read()
# 向端口写数据
ser.write('')
# 设置波特率
ser.baudrate = 115200
# 查看串口是否打开
ser.isOpen()
# 读一行，以/n结尾，不然一直读取
data = ser.readline()

# 一些常用属性
ser = serial.Serial('com1',115200,timeout=1)
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


