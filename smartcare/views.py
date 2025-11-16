
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Crop, SensorData, IrrigationLog, ActiveCrop, DiseaseDetection
from .serializers import (CropSerializer, SensorDataSerializer, 
                          IrrigationLogSerializer, ActiveCropSerializer,
                          DiseaseDetectionSerializer)
from .mqtt_client import get_mqtt_client
import requests
import json
import logging
from datetime import datetime, timedelta
import numpy as np
from PIL import Image
import io

logger = logging.getLogger(__name__)


# Template Views
def home_view(request):
    """Home dashboard view"""
    context = {
        'active_crop': ActiveCrop.objects.filter(is_active=True).first(),
        'latest_sensor': SensorData.objects.first(),
        'total_crops': Crop.objects.count(),
        'total_readings': SensorData.objects.count(),
    }
    return render(request, 'home.html', context)

from django.utils import timezone

def analytics_view(request):
    """Analytics dashboard with charts"""
    # Get last 24 hours of data
    # last_24h = datetime.now() - timedelta(hours=24)
    last_24h = timezone.now() - timedelta(hours=24)

    sensor_data = SensorData.objects.filter(timestamp__gte=last_24h).order_by('timestamp')
    
    context = {
        'sensor_data': sensor_data,
        'active_crop': ActiveCrop.objects.filter(is_active=True).first(),
    }
    return render(request, 'analytics.html', context)


def disease_detection_view(request):
    """Disease detection view"""
    recent_detections = DiseaseDetection.objects.all()[:10]
    context = {
        'recent_detections': recent_detections,
    }
    return render(request, 'disease_detection.html', context)


# API ViewSets
class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer


class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer


class IrrigationLogViewSet(viewsets.ModelViewSet):
    queryset = IrrigationLog.objects.all()
    serializer_class = IrrigationLogSerializer


class ActiveCropViewSet(viewsets.ModelViewSet):
    queryset = ActiveCrop.objects.all()
    serializer_class = ActiveCropSerializer


# API Endpoints
@api_view(['GET'])
def get_latest_sensor_data(request):
    """Get latest sensor reading"""
    try:
        latest = SensorData.objects.first()
        if latest:
            serializer = SensorDataSerializer(latest)
            return Response(serializer.data)
        return Response({'message': 'No data available'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=500)


@api_view(['GET'])
def get_chart_data(request):
    """Get sensor data for charts"""
    try:
        hours = int(request.GET.get('hours', 24))
        # time_threshold = datetime.now() - timedelta(hours=hours)
        time_threshold = timezone.now() - timedelta(hours=hours)

        
        data = SensorData.objects.filter(timestamp__gte=time_threshold).order_by('timestamp')
        
        chart_data = {
            # 'labels': [d.timestamp.strftime('%H:%M') for d in data],
            'labels': [timezone.localtime(d.timestamp).strftime('%H:%M') for d in data],
            'moisture': [d.moisture for d in data],
            'temperature': [d.temperature for d in data],
            'humidity': [d.humidity for d in data],
        }
        
        return Response(chart_data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)


@api_view(['POST'])
def set_active_crop(request):
    """Set active crop for monitoring"""
    try:
        crop_id = request.data.get('crop_id')
        crop = Crop.objects.get(id=crop_id)
        
        # Deactivate all crops
        ActiveCrop.objects.filter(is_active=True).update(is_active=False)
        
        # Activate selected crop
        active_crop, created = ActiveCrop.objects.get_or_create(
            crop=crop,
            defaults={'is_active': True}
        )
        if not created:
            active_crop.is_active = True
            active_crop.save()
        
        return Response({
            'message': f'{crop.name} set as active crop',
            'crop': CropSerializer(crop).data
        })
    except Crop.DoesNotExist:
        return Response({'error': 'Crop not found'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=500)


@api_view(['POST'])
def manual_relay_control(request):
    """Manually control relay"""
    try:
        state = request.data.get('state')  # 'ON' or 'OFF'
        
        mqtt_client = get_mqtt_client()
        mqtt_client.publish_relay_command(state == 'ON')
        
        return Response({'message': f'Relay turned {state}'})
    except Exception as e:
        return Response({'error': str(e)}, status=500)


@api_view(['GET'])
def get_weather_data(request):
    """Get weather data from OpenWeatherMap API"""
    try:
        api_key = settings.WEATHER_API_KEY
        city = settings.WEATHER_CITY
        
        if not api_key:
            return Response({
                'error': 'Weather API key not configured',
                'temp': 25,
                'humidity': 60,
                'description': 'Clear',
                'icon': '01d'
            })
        
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        weather_data = {
            'temp': round(data['main']['temp'], 1),
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'].title(),
            'icon': data['weather'][0]['icon'],
            'city': city,
            'sunrise': datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M'),
            'sunset': datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M'),
        }
        
        return Response(weather_data)
    except Exception as e:
        logger.error(f"Weather API error: {e}")
        return Response({
            'temp': 25,
            'humidity': 60,
            'description': 'Data unavailable',
            'icon': '01d',
            'city': city
        })


@api_view(['POST'])
@csrf_exempt
def detect_disease(request):
    """Detect plant disease from uploaded image using trained ML model"""
    try:
        if 'image' not in request.FILES:
            return Response({'error': 'No image provided'}, status=400)
        
        image_file = request.FILES['image']
        
        # Validate image
        try:
            img = Image.open(image_file)
        except Exception as e:
            return Response({'error': 'Invalid image file'}, status=400)
        
        # Import ML predictor and remedy database
        from smartcare.ml_model.disease_predictor import get_predictor
        from smartcare.ml_model.disease_remedies import get_remedy, format_remedy_text
        
        # Get predictor instance
        predictor = get_predictor()
        
        # Make prediction
        prediction_result = predictor.predict(img)
        
        disease_name = prediction_result['disease']
        confidence = prediction_result['confidence']
        top_3 = prediction_result['top_3_predictions']
        
        # Get comprehensive remedy information with flexible matching
        remedy_info = get_remedy(disease_name)
        remedy_text = format_remedy_text(disease_name, remedy_info)
        
        # Save image file again (it was consumed by PIL)
        image_file.seek(0)
        
        # Save detection result
        detection = DiseaseDetection.objects.create(
            image=image_file,
            predicted_disease=disease_name,
            confidence=confidence,
            remedy=remedy_text
        )
        
        # Prepare response
        response_data = {
            'id': detection.id,
            'image': detection.image.url,
            'predicted_disease': disease_name,
            'confidence': confidence,
            'remedy': remedy_text,
            'detected_at': detection.detected_at,
            'top_3_predictions': top_3,
            'remedy_details': {
                'description': remedy_info.get('description', ''),
                'symptoms': remedy_info.get('symptoms', []),
                'treatment': remedy_info.get('treatment', []),
                'prevention': remedy_info.get('prevention', []),
                'organic_solutions': remedy_info.get('organic_solutions', [])
            }
        }
        
        logger.info(f"Disease detected: {disease_name} with {confidence:.2f}% confidence")
        
        return Response(response_data)
        
    except Exception as e:
        logger.error(f"Disease detection error: {e}")
        import traceback
        traceback.print_exc()
        return Response({
            'error': 'Error processing image. Please try again.',
            'details': str(e)
        }, status=500)



from django.http import JsonResponse, Http404
from rest_framework.decorators import api_view 
from .models import DiseaseDetection

@api_view(['GET'])
def get_detection_detail(request, pk):
    """
    Return detailed disease detection info for the popup modal.
    """
    try:
        detection = DiseaseDetection.objects.get(pk=pk)
        data = {
            "id": detection.id,
            "predicted_disease": detection.predicted_disease,
            "confidence": round(detection.confidence, 2),
            "remedy": detection.remedy,
            "image": detection.image.url if detection.image else "",
            "detected_at": detection.detected_at.strftime("%b %d, %Y, %I:%M %p"),
        }
        return JsonResponse(data)
    except DiseaseDetection.DoesNotExist:
        raise Http404("Detection not found")


