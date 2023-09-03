import serial
import time
import MoterD

readSer = serial.Serial('/dev/rfcomm0',9600, timeout=3)
MoterD.initialize()
st = time.time()

sum = b'0'
while time.time() - st < 10:

    while True:         #シリアル通信
        c = readSer.read()
        if c.isdigit():
            sum = sum + c
        else:
            i = sum.decode(encoding='utf-8')
            i = int(i)
            sum = b'0'
            break       #duty比受け取り

    duty_r = i
    
    MoterD.forced_acc(duty_r)   #モーター動作

  
MoterD.clean()
readSer.close()
