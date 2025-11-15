from rest_framework import serializers
from .models import Crop, SensorData, IrrigationLog, ActiveCrop, DiseaseDetection


class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'


class IrrigationLogSerializer(serializers.ModelSerializer):
    crop_name = serializers.CharField(source='crop.name', read_only=True)
    
    class Meta:
        model = IrrigationLog
        fields = '__all__'


class ActiveCropSerializer(serializers.ModelSerializer):
    crop_name = serializers.CharField(source='crop.name', read_only=True)
    crop_details = CropSerializer(source='crop', read_only=True)
    
    class Meta:
        model = ActiveCrop
        fields = '__all__'


class DiseaseDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseDetection
        fields = '__all__'