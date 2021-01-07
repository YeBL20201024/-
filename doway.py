# 导入串口模块
import serial
from serial.serialutil import Timeout
import time

# 定义串口为x
x = serial.Serial('COM1',115200,Timeout=1)

# 简单记录串口数据功能
# 判断串口是否打开
if __name__ == "__main__":
    if x.is_open():
        print('COM3 open success')
    else:
        print('COM3 is not open')

# 定义函数：给串口发送命令    
def fasong():
    while Ture:
        time.sleep(1) #设置发送间隔
        myinput=bytes{[0x01,0x03,0x00,0x00,0x01,0x84,0x0A]}  #设置发送数据类型-现在是16进制
        x.write(myinput) #用write函数向串口发送数据
    
# 定义函数：从串口接收数据
def jieshou():
    while x.in_waiting()>0:
        myout = x.read()
        print(myout.decode())


    """
    docstring
    """
    pass

# 定义gga函数
def gga(serial):
    """
    docstring
    """
    pass