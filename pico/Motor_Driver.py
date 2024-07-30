from machine import Pin 
from time import sleep

# Defining motor pins

#OUT1  and OUT2

#top left wheel
In1=Pin(6,Pin.OUT) #6 - gpio 7
In2=Pin(7,Pin.OUT)  #7 = gpio 6
EN_A=Pin(8,Pin.OUT)


#OUT3  and OUT4

#top right wheel
In3=Pin(4,Pin.OUT)  
In4=Pin(3,Pin.OUT)  
EN_B=Pin(2,Pin.OUT)


#middle left wheel
In5 =Pin(15,Pin.OUT)  
In6  =Pin(14,Pin.OUT) 

#middle right wheel
In7 =Pin(13,Pin.OUT)
In8 =Pin(12,Pin.OUT)
EN_A.high()
EN_B.high()

#bottom left wheel
In9 =Pin(16,Pin.OUT)
In10 =Pin(17,Pin.OUT)

#bottom right wheel
In11 =Pin(18,Pin.OUT)
In12 =Pin(19,Pin.OUT)



# Forward
def move_forward():    
    #top left wheel
    In1.high()
    In2.low()

    #middle left wheel
    In5.low()
    In6.high()

    #back left wheel
    In9.low()
    In10.high()

    #rop right wheel
    In3.high()
    In4.low()

    #middle right wheel
    In7.low()
    In8.high()

    #bottom right wheel
    In11.low()
    In12.high()


    
# Backward
def move_backward():
    
    #top left wheel
    In1.low()
    In2.high()

     #middle left wheel
    In5.high()
    In6.low()

      #back left wheel
    In9.high()
    In10.low()

    #top rig2t wheel
    In3.low()
    In4.high()

    #middle right wheel
    In7.high()
    In8.low()

    #bottom right wheel
    In11.high()
    In12.low()
    
#Turn Right
def turn_right():
    #top left wheel
    In1.high()
    In2.low()

#middle left wheel
    In5.low()
    In6.high()

    #back left wheel
    In9.low()
    In10.high()

    #top right wheel
    In3.low()
    In4.high()

    #middle right wheel
    In7.high()
    In8.low()

    #bottom right wheel
    In11.high()
    In12.low()
    
#Turn Left
def turn_left():
     #top left wheel
    In1.low()
    In2.high()

    #middle left wheel
    In5.high()
    In6.low()

    #back left wheel
    In9.high()
    In10.low()

   #rop right wheel
    In3.high()
    In4.low()

       #middle right wheel
    In7.low()
    In8.high()

    #bottom right wheel
    In11.low()
    In12.high()
   
#Stop
def stop():
    In1.low()
    In2.low()
    In3.low()
    In4.low()
    In5.low()
    In6.low()
    In7.low()
    In8.low()
    In9.low()
    In10.low()
    In11.low()
    In12.low()
