# Use the updated code I provided earlier with lazy loading

web: gunicorn smartcare.wsgi:application --bind 0.0.0.0:$PORT --workers 1 --threads 4 --timeout 120 --max-requests 1000
worker: python mqtt_client.py