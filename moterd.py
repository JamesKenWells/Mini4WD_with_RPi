
import RPi.GPIO as GPIO
import time

#ピン番号の定義 pin_definision
LRG = 22
MODE = 36
STBY = 38
IN1 = 32
IN2 = 40
#PWM制御周波数 PWM_frequency
Hz = 100

GPIO.setmode(GPIO.BOARD)
for l in [LRG, MODE, STBY, IN1, IN2]:
  GPIO.setup(l, GPIO.OUT)
  GPIO.output(l, GPIO.LOW)
fowardp = GPIO.PWM(IN1, Hz)
reversep = GPIO.PWM(IN2, Hz)
forcedp = GPIO.PWM(STBY, Hz)

def cleanup():
  GPIO.cleanup()

def fpower():
  GPIO.output(MODE, GPIO.LOW)
  GPIO.output(LRG, GPIO.HIGH)
  GPIO.output(STBY, GPIO.HIGH)
  GPIO.output(IN1, GPIO.HIGH)
  GPIO.output(IN2, GPIO.LOW)

def brake():
  GPIO.output(MODE, GPIO.LOW)
  GPIO.output(LRG, GPIO.HIGH)
  GPIO.output(STBY, GPIO.HIGH)
  GPIO.output(IN1, GPIO.HIGH)
  GPIO.output(IN2, GPIO.HIGH)

def acceralate(dc=100, reverse=False):
  if dc<0:
    dc = 0
  elif 100<dc:
    dc = 100
  GPIO.output(MODE, GPIO.LOW)
  GPIO.output(LRG, GPIO.HIGH)
  GPIO.output(STBY, GPIO.HIGH)
  if not reverse:
    fowardp.start(dc)
    GPIO.output(IN2, GPIO.LOW)
  else:
    reversep.start(dc)
    GPIO.output(IN1, GPIO.LOW)

def forced_acc(dc=100, reverse=False):
  if dc<0:
    dc = 0
  elif 100<dc:
    dc = 100
  GPIO.output(MODE, GPIO.LOW)
  GPIO.output(LRG, GPIO.HIGH)
  if not reverse:
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
  else:
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
  forcedp.start(dc)

def ISD_reset():
  GPIO.output(STBY, GPIO.LOW)
  GPIO.output(STBY, GPIO.HIGH)

def powerOFF():
  GPIO.output(STBY, GPIO.LOW)

def powerON():
  GPIO.output(STBY, GPIO.HIGH)


#--------------------


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
