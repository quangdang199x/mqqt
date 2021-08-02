import paho.mqtt.client as mqqt
import time
from random import randrange, uniform

mqqtBroker = "mqtt.eclipseprojects.io"
client = mqqt.Client('Temperature_Inside')
client.connect(mqqtBroker)

while True:
    randomNumber = uniform(20.0, 21.0)
    client.publish("TEMPERATURE", randomNumber)
    print("Just publish " + str(randomNumber) + " to Topic TEMPERATURE")
    time.sleep(2)

