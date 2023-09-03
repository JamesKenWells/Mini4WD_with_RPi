import time
import MoterD


print('start')

fpower()
time.sleep(2)
powerOFF()

fpower()
time.sleep(2)
brake()

print('end')

ISD_reset()
cleanup()
