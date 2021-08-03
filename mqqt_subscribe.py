import paho.mqtt.client as mqqt
import time

def on_message(client, userdata, message):
    print("Received massage: ", str(message.payload.decode("utf-8")))

mqqtBroker = "mqtt.eclipseprojects.io"
client = mqqt.Client("Smartphone")
client.connect(mqqtBroker)

client.loop_start()
client.subscribe("TEMPERATURE")
client.on_message = on_message
time.sleep(30)
client.loop_stop()