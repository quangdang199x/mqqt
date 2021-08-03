import paho.mqtt.client as mqqt
import time
from random import randrange, uniform

mqqtBroker = "mqtt.eclipseprojects.io"
client = mqqt.Client('Temperature_Outside')
client.connect(mqqtBroker)

while True:
    randomNumber = randrange(10)
    client.publish("TEMPERATURE", randomNumber)
    print("Just publish " + str(randomNumber) + " to Topic TEMPERATURE")
    time.sleep(2)

