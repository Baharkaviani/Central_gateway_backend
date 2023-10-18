from django.apps import AppConfig
import paho.mqtt.client as mqtt

from server import settings


class RecordsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "records"

    def ready(self):
        from . import mqtt

        mqtt.client.loop_start()
