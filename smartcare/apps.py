from django.apps import AppConfig


class SmartcareConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'smartcare'
    verbose_name = 'Smart Care IoT System'


from django.apps import AppConfig
import threading
from .mqtt_client import get_mqtt_client # adjust path if needed

class SmartcareConfig(AppConfig):
    name = 'smartcare'

    def ready(self):
        threading.Thread(target=get_mqtt_client, daemon=True).start()