from django.db import models
from django.utils import timezone


class Crop(models.Model):
    """Crop types with specific moisture requirements"""
    name = models.CharField(max_length=100, unique=True)
    moisture_min = models.FloatField(help_text="Minimum moisture threshold (%)")
    moisture_max = models.FloatField(help_text="Maximum moisture threshold (%)")
    optimal_temp_min = models.FloatField(default=15.0, help_text="Minimum temperature (°C)")
    optimal_temp_max = models.FloatField(default=35.0, help_text="Maximum temperature (°C)")
    optimal_humidity_min = models.FloatField(default=40.0, help_text="Minimum humidity (%)")
    optimal_humidity_max = models.FloatField(default=80.0, help_text="Maximum humidity (%)")
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Removed default
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class SensorData(models.Model):
    """Real-time sensor readings from ESP32"""
    device_id = models.CharField(max_length=50, default="ESP32_001")
    moisture = models.FloatField(help_text="Soil moisture level (%)")
    temperature = models.FloatField(help_text="Temperature (°C)")
    humidity = models.FloatField(help_text="Air humidity (%)")
    timestamp = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-timestamp']
        verbose_name_plural = "Sensor Data"

    def __str__(self):
        return f"{self.device_id} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"


class IrrigationLog(models.Model):
    """Log of irrigation events"""
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, null=True, blank=True)
    sensor_data = models.ForeignKey(SensorData, on_delete=models.CASCADE)
    relay_state = models.BooleanField(help_text="True=ON, False=OFF")
    reason = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        state = "ON" if self.relay_state else "OFF"
        return f"Relay {state} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"


class ActiveCrop(models.Model):
    """Currently selected crop for monitoring"""
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    activated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-activated_at']

    def __str__(self):
        return f"{self.crop.name} - {'Active' if self.is_active else 'Inactive'}"

    def save(self, *args, **kwargs):
        if self.is_active:
            # Deactivate all other crops
            ActiveCrop.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)


class DiseaseDetection(models.Model):
    """Disease detection results"""
    image = models.ImageField(upload_to='disease_images/')
    predicted_disease = models.CharField(max_length=200)
    confidence = models.FloatField()
    remedy = models.TextField()
    detected_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-detected_at']

    def __str__(self):
        return f"{self.predicted_disease} - {self.confidence:.2f}%"