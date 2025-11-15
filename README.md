# Smart Care - IoT Plant Monitoring System

## Features
- Real-time plant moisture, temperature, and humidity monitoring
- Crop-specific threshold management
- Automated irrigation control via MQTT
- AI-powered disease detection
- Weather API integration
- Professional dashboard with analytics
- Day/Night theme toggle

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Create a `.env` file in the project root:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
MQTT_BROKER=broker.hivemq.com
MQTT_PORT=1883
MQTT_TOPIC_SUBSCRIBE=smartcare/sensor/data
MQTT_TOPIC_PUBLISH=smartcare/control/relay
WEATHER_API_KEY=your-openweathermap-api-key
```

### 3. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Seed Initial Data
```bash
python manage.py seed_data
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```

### 7. Start MQTT Client (in separate terminal)
```bash
python manage.py start_mqtt
```

## ESP32 Setup

### Hardware Requirements
- ESP32 Development Board
- Soil Moisture Sensor
- DHT22 (Temperature & Humidity Sensor)
- Relay Module
- Water Pump

### ESP32 Code Integration
The ESP32 should:
1. Connect to WiFi
2. Connect to MQTT broker (same as configured in Django)
3. Read sensor data every 30 seconds
4. Publish data to topic: `smartcare/sensor/data`
5. Subscribe to topic: `smartcare/control/relay`
6. Format: `{"moisture": 45.2, "temperature": 28.5, "humidity": 65.3, "device_id": "ESP32_001"}`

## API Endpoints
- `/api/sensor-data/` - GET: List all sensor readings
- `/api/crops/` - GET: List all crops with thresholds
- `/api/control/relay/` - POST: Manual relay control
- `/api/detect-disease/` - POST: Upload image for disease detection

## Weather API
Sign up at https://openweathermap.org/ for free API key

## Project Structure
```
smartcare_project/
├── manage.py
├── requirements.txt
├── project/ (Django settings)
├── smartcare/ (Main app)
├── templates/ (HTML templates)
├── static/ (CSS, JS, Images)
└── media/ (Uploaded images)
```

## License
MIT License