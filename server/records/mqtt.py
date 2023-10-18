import re
import paho.mqtt.client as mqtt
from datetime import datetime
from server import settings
from records.utils.callbacks import create_obj


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # pattern = re.compile(r"AUTSmartMeteringSystem/gas/#")
    client.subscribe(
        [
            ("AUTSmartMeteringSystem/gas/84:0D:8E:3D:53:60/consumption", 0),
            ("AUTSmartMeteringSystem/water/84:0D:8E:3D:53:60/consumption", 0),
            ("AUTSmartMeteringSystem/power/84:0D:8E:3D:53:60/consumption", 0),
            ("AUTSmartMeteringSystem/battery/84:0D:8E:3D:53:60/remainingPercentage", 0),
        ]
    )


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload.decode()))
    create_obj(msg)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
client.connect(
    host=settings.MQTT_SERVER,
    port=settings.MQTT_PORT,
    keepalive=settings.MQTT_KEEPALIVE,
)
