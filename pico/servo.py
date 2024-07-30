from machine import Pin,PWM
from time import sleep

servoPin1=0
servoPin2 = 1
servoPin3 = 5
servo1 = PWM(Pin(servoPin1))
servo2 = PWM(Pin(servoPin2))
servo3 = PWM(Pin(servoPin3))

servo1.freq(50)
servo2.freq(50)
servo3.freq(50)


#rotate servo by input angle
def rotate_servo1(angle):
    value = 6553/180*angle+1638
    servo1.duty_u16(int(value))
    sleep(.02)

def rotate_servo2(angle):
    value = 6553/180*angle+1638
    servo2.duty_u16(int(value))
    sleep(.02)

def rotate_servo3(angle):
    value = 6553/180*angle+1638
    servo3.duty_u16(int(value))
    sleep(.02)
