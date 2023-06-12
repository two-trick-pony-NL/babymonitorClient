import requests
import RPi.GPIO as GPIO
import requests
import time

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

def detect_temperature():
    return 30

def detect_humidity():
    return 50

def detect_movement():
    return True

def detect_cry():
    return False

while True:
    try: 
        print("New measurement")
        newReading = [detect_temperature(), detect_humidity(), detect_movement(), detect_cry()]
        if newReading == lastMeasurement:
            print("Data stayed the same no update")
        else:
            print("Detected change:")
            lastMeasurement = newReading
            x = requests.put(endpoint, json = create_measurement(detect_temperature(), detect_humidity(),detect_movement(), detect_cry()))
            print(x.text)
    except:
        print("Something went wrong, trying again in 10 seconds")        
    time.sleep(10)