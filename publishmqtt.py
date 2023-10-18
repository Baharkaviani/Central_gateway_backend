# python 3.6

import random
import time

from paho.mqtt import client as mqtt_client
import paho.mqtt.subscribe as subscribe

broker = 'test.mosquitto.org'
port = 1884
topics = {
    1: "AUTSmartMeteringSystem/gas/84:0D:8E:3D:53:60/consumption",
    2: "AUTSmartMeteringSystem/water/84:0D:8E:3D:53:60/consumption",
    3: "AUTSmartMeteringSystem/power/84:0D:8E:3D:53:60/consumption",
    4: "AUTSmartMeteringSystem/battery/84:0D:8E:3D:53:60/remainingPercentage",
}
# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'
username = 'rw'
password = 'readwrite'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 1
    while True:
        time.sleep(5)
        msg = f"{msg_count}"
        result = client.publish(topics[msg_count], msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topics[msg_count]}`")
        else:
            print(f"Failed to send message to topic {topics[msg_count]}")
        msg_count += 1
        if msg_count > 4:
            break

def subscribe(client):
    result, mid = client.subscribe(topic, 0)
    print(type(result))
    print(type(mid))


def on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '"
        + message.topic + "' with QoS " + str(message.qos))

def on_subscribe(client, userdata, mid, granted_qos):
     print("Received on subsribe ", userdata)



def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    client.loop_stop()


if __name__ == '__main__':
    run()
