import os
import sys
import django

# Add the backend directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'housing_analyzer.settings')
django.setup()

from django.contrib.auth.models import User
from properties.models import Property
from datetime import timezone
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    logger.info("Starting sample data creation...")
    
    # Create sample user
    user, created = User.objects.get_or_create(
        username='owner1',
        email='owner1@example.com',
        defaults={'is_staff': False}
    )

    if created:
        user.set_password('password123')
        user.save()
        logger.info(f"Created user: {user.username}")

    # Create sample properties
    properties_data = [
        {
            'title': 'Modern Downtown Apartment',
            'description': 'Beautiful modern apartment in downtown area',
            'address': '123 Main St, Downtown',
            'rent_price': 1500.00,
            'bedrooms': 2,
            'bathrooms': 1,
            'area_sqm': 85,
            'property_type': 'apartment',
            'status': 'available',
            'verification_status': 'verified',
            'owner': user,
            'created_at': timezone.now(),
        },
        {
            'title': 'Cozy Studio Near Park',
            'description': 'Perfect studio apartment near the park',
            'address': '456 Park Ave',
            'rent_price': 1200.00,
            'bedrooms': 1,
            'bathrooms': 1,
            'area_sqm': 55,
            'property_type': 'studio',
            'status': 'available',
            'verification_status': 'verified',
            'owner': user,
            'created_at': timezone.now(),
        },
        {
            'title': 'Spacious Family Home',
            'description': 'Large family home with garden',
            'address': '789 Family Rd',
            'rent_price': 2500.00,
            'bedrooms': 4,
            'bathrooms': 2,
            'area_sqm': 200,
            'property_type': 'house',
            'status': 'available',
            'verification_status': 'verified',
            'owner': user,
            'created_at': timezone.now(),
        }
    ]

    for prop_data in properties_data:
        prop, created = Property.objects.get_or_create(
            title=prop_data['title'],
            defaults=prop_data
        )
        if created:
            logger.info(f"Created property: {prop.title}")
        else:
            logger.info(f"Property already exists: {prop.title}")

    logger.info(f"Total properties in database: {Property.objects.count()}")
    logger.info("Sample data creation completed successfully!")
    
except Exception as e:
    logger.error(f"Error creating sample data: {e}")
    import traceback
    traceback.print_exc()
