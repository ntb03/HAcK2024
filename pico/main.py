from connections import connect_mqtt, connect_internet
from time import sleep
from constants import ssid, mqtt_server, mqtt_user, mqtt_pass, pwd
from ultrasonic_sensor import distance
from hum_temp import getHumTemp
import Motor_Driver as Motor
import servo as Servo


# Function to handle an incoming message
def cb(topic, msg):
    # print(f"Topic: {topic}, Message: {msg}")
    
    # Reading data for topic "direction"
    if topic == b"direction":
        if msg == b"forward":
            Motor.move_forward()
        elif msg == b"left":
            Motor.turn_left()
        elif msg == b"back":
            Motor.move_backward()
        elif msg == b"right":
            Motor.turn_right()
        elif msg == b"stop":
            Motor.stop()
    
    # Reading data for topic "arm"
    elif topic == b"arm":
        if msg == b"up":
            Servo.rotate_servo1(1)
        elif msg == b"down":
            Servo.rotate_servo1(-1)
        elif msg == b"counterClockwise":
            Servo.rotate_servo2(1)
        elif msg == b"clockwise":
            Servo.rotate_servo2(-1)

    
    # Reading data for topic "pinch"
    elif topic == b"pinch":
        if msg == b"grab":
            Servo.rotate_servo3(1)
        elif msg == b"release":
            Servo.rotate_servo3(-1)


def main():
    try:

        if not connect_internet(ssid, pwd):
            print("Error: Could not connect to internet")
            return

        client = connect_mqtt(mqtt_server, mqtt_user, mqtt_pass)
        if not client:
            print("Error connecting to MQTT broker")
            return
        print("MQTT broker")

        client.set_callback(cb)
        client.subscribe("direction") # What the pico listens for
        client.subscribe("motorPower")
        client.subscribe("arm")
        client.subscribe("pinch")


        loopCounter = 0
        while True:
            if loopCounter >= 100: # After 100 or more loops
                loopCounter = 0
                
                client.publish("ultrasonic", str(distance())) # Send Distance
            
                humTemp = getHumTemp() # Two values in same return
                (hum, temp) = humTemp
                client.publish("humidity", str(hum)) # Send humidity
                client.publish("temp", str(temp)) # Send temperature
                
            client.check_msg() # Check MQTT Server for subscribed messages
            sleep(0.01)
            loopCounter += 1          
        
        

    except KeyboardInterrupt:
        print('keyboard interrupt')
        
        
if __name__ == "__main__":
    main()
