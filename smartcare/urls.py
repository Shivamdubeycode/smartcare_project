from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'crops', views.CropViewSet)
router.register(r'sensor-data', views.SensorDataViewSet)
router.register(r'irrigation-logs', views.IrrigationLogViewSet)
router.register(r'active-crops', views.ActiveCropViewSet)

urlpatterns = [
    # Template views
    path('', views.home_view, name='home'),
    path('analytics/', views.analytics_view, name='analytics'),
    path('disease-detection/', views.disease_detection_view, name='disease_detection'),
    
    # API endpoints
    path('api/', include(router.urls)),
    path('api/latest-sensor/', views.get_latest_sensor_data, name='latest_sensor'),
    path('api/chart-data/', views.get_chart_data, name='chart_data'),
    path('api/set-active-crop/', views.set_active_crop, name='set_active_crop'),
    path('api/relay-control/', views.manual_relay_control, name='relay_control'),
    path('api/weather/', views.get_weather_data, name='weather'),
    path('api/detect-disease/', views.detect_disease, name='detect_disease'),
    path('api/detection/<int:pk>/', views.get_detection_detail, name='get_detection_detail'),

]