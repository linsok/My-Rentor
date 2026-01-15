# Generated migration for creating sample data

from django.db import migrations
from django.contrib.auth.models import User
from properties.models import Property


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            code='create_sample_data',
            reverse_code=migrations.RunPython.noop
        ),
    ]


def create_sample_data(apps, schema_editor):
    # Create sample user
    user, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@example.com',
            'first_name': 'Admin',
            'last_name': 'User'
        }
    )
    
    if created:
        user.set_password('password123')
        user.save()

    # Create sample property
    Property.objects.get_or_create(
        title='Test Property',
        defaults={
            'description': 'Test property for demonstration',
            'address': '123 Test Street',
            'city': 'Phnom Penh',
            'rent_price': 1000.00,
            'bedrooms': 2,
            'bathrooms': 1,
            'area_sqm': 100,
            'property_type': 'apartment',
            'status': 'available',
            'verification_status': 'verified',
            'owner': user
        }
    )
