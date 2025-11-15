import paho.mqtt.client as mqtt
import json
import logging
from django.conf import settings
# from .models import SensorData, ActiveCrop, IrrigationLog

logger = logging.getLogger(__name__)


class MQTTClient:
    def __init__(self):
        self.client = mqtt.Client(client_id=settings.MQTT_CLIENT_ID)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.broker = settings.MQTT_BROKER
        self.port = settings.MQTT_PORT
        self.subscribe_topic = settings.MQTT_TOPIC_SUBSCRIBE
        self.publish_topic = settings.MQTT_TOPIC_PUBLISH

    def on_connect(self, client, userdata, flags, rc):
        """Callback when connected to MQTT broker"""
        if rc == 0:
            logger.info("Connected to MQTT Broker!")
            client.subscribe(self.subscribe_topic)
            logger.info(f"Subscribed to topic: {self.subscribe_topic}")
        else:
            logger.error(f"Failed to connect, return code {rc}")

    def on_message(self, client, userdata, msg):
        """Callback when message received from ESP32"""
        from .models import SensorData  #1
        try:
            # Parse incoming JSON data from ESP32
            payload = json.loads(msg.payload.decode())
            logger.info(f"Received data: {payload}")
            
            # Save sensor data to database
            sensor_data = SensorData.objects.create(
                device_id=payload.get('device_id', 'ESP32_001'),
                moisture=payload['moisture'],
                temperature=payload['temperature'],
                humidity=payload['humidity']
            )
            
            # Check active crop and thresholds
            self.check_and_control_irrigation(sensor_data)
            
        except Exception as e:
            logger.error(f"Error processing MQTT message: {e}")

    def check_and_control_irrigation(self, sensor_data):
        """Check moisture levels and control relay if needed"""
        from .models import ActiveCrop, IrrigationLog #2
        try:
            active_crop_obj = ActiveCrop.objects.filter(is_active=True).first()
            
            if not active_crop_obj:
                logger.warning("No active crop selected")
                return
            
            crop = active_crop_obj.crop
            moisture = sensor_data.moisture
            
            # Check if moisture is below threshold
            if moisture < crop.moisture_min:
                # Turn ON relay (start irrigation)
                self.publish_relay_command(True)
                IrrigationLog.objects.create(
                    crop=crop,
                    sensor_data=sensor_data,
                    relay_state=True,
                    reason=f"Moisture {moisture:.1f}% below minimum {crop.moisture_min}%"
                )
                logger.info(f"Irrigation started for {crop.name}")
                
            elif moisture > crop.moisture_max:
                # Turn OFF relay (stop irrigation)
                self.publish_relay_command(False)
                IrrigationLog.objects.create(
                    crop=crop,
                    sensor_data=sensor_data,
                    relay_state=False,
                    reason=f"Moisture {moisture:.1f}% above maximum {crop.moisture_max}%"
                )
                logger.info(f"Irrigation stopped for {crop.name}")
                
        except Exception as e:
            logger.error(f"Error in irrigation control: {e}")

    def publish_relay_command(self, state):
        """Publish relay command to ESP32"""
        from .models import SensorData #3
        try:
            command = {
                "relay": "ON" if state else "OFF",
                "timestamp": str(SensorData.objects.latest('timestamp').timestamp)
            }
            self.client.publish(self.publish_topic, json.dumps(command))
            logger.info(f"Published relay command: {command}")
        except Exception as e:
            logger.error(f"Error publishing relay command: {e}")

    def connect(self):
        """Connect to MQTT broker"""
        try:
            self.client.connect(self.broker, self.port, 60)
            logger.info(f"Connecting to {self.broker}:{self.port}")
        except Exception as e:
            logger.error(f"Failed to connect to MQTT broker: {e}")

    def start(self):
        """Start MQTT client loop"""
        self.connect()
        self.client.loop_forever()

    def stop(self):
        """Stop MQTT client"""
        self.client.disconnect()
        self.client.loop_stop()


# Global MQTT client instance
mqtt_client = None


def get_mqtt_client():
    """Get or create MQTT client instance"""
    global mqtt_client
    if mqtt_client is None:
        mqtt_client = MQTTClient()
    return mqtt_client