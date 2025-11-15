from django.core.management.base import BaseCommand
from smartcare.mqtt_client import get_mqtt_client
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Starts the MQTT client to receive sensor data from ESP32'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting MQTT client...'))
        
        try:
            mqtt_client = get_mqtt_client()
            mqtt_client.start()
        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING('\nStopping MQTT client...'))
            mqtt_client.stop()
            self.stdout.write(self.style.SUCCESS('MQTT client stopped'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))