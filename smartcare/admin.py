from django.contrib import admin
from .models import Crop, SensorData, IrrigationLog, ActiveCrop, DiseaseDetection


@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ['name', 'moisture_min', 'moisture_max', 'optimal_temp_min', 'optimal_temp_max']
    search_fields = ['name']
    list_filter = ['created_at']


@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ['device_id', 'moisture', 'temperature', 'humidity', 'timestamp']
    list_filter = ['device_id', 'timestamp']
    date_hierarchy = 'timestamp'
    ordering = ['-timestamp']


@admin.register(IrrigationLog)
class IrrigationLogAdmin(admin.ModelAdmin):
    list_display = ['crop', 'relay_state', 'reason', 'timestamp']
    list_filter = ['relay_state', 'timestamp']
    date_hierarchy = 'timestamp'


@admin.register(ActiveCrop)
class ActiveCropAdmin(admin.ModelAdmin):
    list_display = ['crop', 'is_active', 'activated_at']
    list_filter = ['is_active']


@admin.register(DiseaseDetection)
class DiseaseDetectionAdmin(admin.ModelAdmin):
    list_display = ['predicted_disease', 'confidence', 'detected_at']
    list_filter = ['detected_at']
    date_hierarchy = 'detected_at'