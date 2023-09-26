import serial
import threading
import time

line = ''
port = '/dev/ttyAMA0'
baud = 115200

ser = serial.Serial(port, baud, timeout=3)

alivethread = True


#thread

def readthread(ser):
  global line

  while alivethread:
    for c in ser.read():
      line+=(chr())
      if line.startswitch('[') and line.endswith(']'):
        print('receive data=' + line)
        line=''

  ser.close()

#thread end
  
def main():

  thread = threading.Thread(target=readthread, args=(ser,))
  thread.start()

  count=10

  while count > 0:
    strcmd = '[test' + str(count) + ']'
    print('send data=' + strcmd)
    ser.write(strcmd.encode())
    time.sleep(1)
    count-=1
  alivethread = False

main()