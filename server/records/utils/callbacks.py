import pytz
import json
import paho.mqtt.client as mqtt
from datetime import datetime

from records.models import DataRecord
from records.constants import DATA_TYPES


def create_obj(msg):
    split_topic = msg.topic.split("/")
    print(msg.topic + " " + str(msg.payload.decode()))
    try:
        data = json.loads(str(msg.payload.decode()))
        data_keys = list(data.keys())
        print("consumption: ", data[data_keys[0]][data[data_keys[1]]])
        DataRecord.objects.create(
            board_id=split_topic[2],
            data_type=split_topic[1][0].lower(),
            consumption=data[data_keys[0]][data[data_keys[1]]],
            time=datetime.now(tz=pytz.timezone("Asia/Tehran")),
        )
    except:
        print("Device first connection to database")
