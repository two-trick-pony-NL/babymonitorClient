import requests
import requests
import time
from gpiozero import MotionSensor
from take_measurement import measure

url = "https://iom7vetorqgo7rg77bo5o2mmee0vcpgy.lambda-url.eu-central-1.on.aws"
endpoint = url +"/create-measurement"
lastMeasurement = []

def create_measurement(temperature, humidity, movementDetected, cryDetected):
    body = {
        "cryDetected": cryDetected,
        "soundDetected": cryDetected,
        "movementDetected": movementDetected,
        "shouldNotifyClient": True,
        "humidity": humidity,
        "temperature": temperature,
        "lastUpdate": 0,
        "userId": 'test_baby'
    }
    return body

def detect_cry():
    return False

i = 0
while True:
    humidity, temperature, movement = measure()
    print("New measurement")
    newMeasurement = [humidity, temperature, movement]
    if newMeasurement == lastMeasurement:
        print("Same values")
        time.sleep(5)
        i = i + 1 
        print(i % 10)
        if i % 10 == 0: #updating the backend every 10th try
            x = requests.put(endpoint, json = create_measurement(temperature, humidity, movement, True))
    else:
        print("Values changed")
        print('from : ', lastMeasurement)
        print('to   :', newMeasurement)
        lastMeasurement = newMeasurement
        x = requests.put(endpoint, json = create_measurement(temperature, humidity, movement, True))
        #print(x.text)
        time.sleep(5)