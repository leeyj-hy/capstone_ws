import serial
from tkinter import *

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.1)

def format_3memory(value):
    # 정수를 3자리 문자열로 포맷
    return f"{value:03}"

def format_4memory(value):
    # 정수를 3자리 문자열로 포맷
    return f"{value:04X}"

def extract_last_4bytes_to_int(data_str):
    # 마지막 4문자를 가져옵니다.
    hex_str = data_str[-5:]
    
    # 문자열에서 '\x03'와 같은 문자를 제거
    clean_hex_str = ''.join([c for c in hex_str if '0' <= c <= '9' or 'a' <= c <= 'f' or 'A' <= c <= 'F'])
    
    return int(clean_hex_str, 16)

###
# memory : plc memory location
# data : set data
def write_data(memory, data):
    message = b'\x0500WSS0106%DW' + format_3memory(memory).encode() + format_4memory(data).encode() + b'\x04'
    ser.write(message)
    readOut = ser.readline().decode('ascii')
    print(readOut)

###
# memory : plc memory location
def read_data(memory):
    message = b'\x0500RSS0106%DW' + format_3memory(memory).encode() + b'\x04'
    ser.write(message)
    readOut = ser.readline().decode('ascii')
    val =extract_last_4bytes_to_int(readOut)
    return val

###
def send_ID(val):
    write_data(100, val)

def read_money():
    ID1 = read_data(201)
    ID2 = read_data(202)
    ID3 = read_data(203)
    print(ID1, ID2, ID3)

def send_vision(val):
    write_data(301, val)

def send_weight(val):
    write_data(302, val)


###ex
#send_ID(1)
#send_ID(2)
#send_ID(3)

#read_money()

#send_vision(100)
#send_weight(1000)
 