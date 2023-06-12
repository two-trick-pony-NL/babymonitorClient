import Adafruit_DHT
import time
from gpiozero import MotionSensor

#Setup motion sensor
MOTIONSENSOR = MotionSensor(4)
#Set up humidity and temperature sensor
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 3


def measure():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return round(humidity, 0), round(temperature, 0), MOTIONSENSOR.motion_detected