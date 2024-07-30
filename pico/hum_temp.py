from machine import Pin
from time import sleep
from dht import DHT11

Temp_Hum_Pin = Pin(9, Pin.OUT, Pin.PULL_DOWN) #defines pin for temp and humidity
TempHum_sensor = DHT11(Temp_Hum_Pin)       # defines sensor for hum and tem

 # print tempurature and Humidity
def print_TempHum():
    TempHum_sensor.measure()
    tempC = TempHum_sensor.temperature() # store temperature
    humidity = TempHum_sensor.humidity() # store humidity
    print('temp =',tempC, 'humidity =', humidity)
    sleep(1)

def getHumTemp():
    TempHum_sensor.measure()
    tempC = TempHum_sensor.temperature() # store temperature'
    humidity = TempHum_sensor.humidity() # store humidity
    return humidity, tempC
