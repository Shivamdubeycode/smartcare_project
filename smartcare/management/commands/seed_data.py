from django.core.management.base import BaseCommand
from smartcare.models import Crop


class Command(BaseCommand):
    help = 'Seeds the database with initial crop data'

    def handle(self, *args, **kwargs):
        crops_data = [
            {
                'name': 'Tomato',
                'moisture_min': 60.0,
                'moisture_max': 80.0,
                'optimal_temp_min': 20.0,
                'optimal_temp_max': 30.0,
                'optimal_humidity_min': 60.0,
                'optimal_humidity_max': 80.0,
                'description': 'Requires consistent moisture and warm temperatures'
            },
            {
                'name': 'Wheat',
                'moisture_min': 50.0,
                'moisture_max': 70.0,
                'optimal_temp_min': 15.0,
                'optimal_temp_max': 25.0,
                'optimal_humidity_min': 50.0,
                'optimal_humidity_max': 70.0,
                'description': 'Tolerates cooler temperatures, moderate water needs'
            },
            {
                'name': 'Rice',
                'moisture_min': 70.0,
                'moisture_max': 90.0,
                'optimal_temp_min': 25.0,
                'optimal_temp_max': 35.0,
                'optimal_humidity_min': 70.0,
                'optimal_humidity_max': 90.0,
                'description': 'High water requirements, thrives in warm humid conditions'
            },
            {
                'name': 'Corn',
                'moisture_min': 55.0,
                'moisture_max': 75.0,
                'optimal_temp_min': 18.0,
                'optimal_temp_max': 32.0,
                'optimal_humidity_min': 55.0,
                'optimal_humidity_max': 75.0,
                'description': 'Moderate water needs, warm season crop'
            },
            {
                'name': 'Potato',
                'moisture_min': 60.0,
                'moisture_max': 75.0,
                'optimal_temp_min': 15.0,
                'optimal_temp_max': 25.0,
                'optimal_humidity_min': 60.0,
                'optimal_humidity_max': 80.0,
                'description': 'Prefers cool temperatures and consistent moisture'
            },
            {
                'name': 'Cotton',
                'moisture_min': 45.0,
                'moisture_max': 65.0,
                'optimal_temp_min': 20.0,
                'optimal_temp_max': 35.0,
                'optimal_humidity_min': 50.0,
                'optimal_humidity_max': 70.0,
                'description': 'Drought tolerant, requires warm temperatures'
            },
            {
                'name': 'Sugarcane',
                'moisture_min': 65.0,
                'moisture_max': 85.0,
                'optimal_temp_min': 25.0,
                'optimal_temp_max': 35.0,
                'optimal_humidity_min': 70.0,
                'optimal_humidity_max': 85.0,
                'description': 'High water requirements, tropical crop'
            },
            {
                'name': 'Lettuce',
                'moisture_min': 70.0,
                'moisture_max': 85.0,
                'optimal_temp_min': 10.0,
                'optimal_temp_max': 20.0,
                'optimal_humidity_min': 65.0,
                'optimal_humidity_max': 80.0,
                'description': 'Cool season crop, requires consistent moisture'
            },
        ]

        for crop_data in crops_data:
            crop, created = Crop.objects.get_or_create(
                name=crop_data['name'],
                defaults=crop_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created crop: {crop.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Crop already exists: {crop.name}'))

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))