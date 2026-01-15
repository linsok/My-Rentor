from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from properties.models import Property


class Command(BaseCommand):
    help = 'Create sample data for the application'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create sample user
        user, created = User.objects.get_or_create(
            username='admin',
            defaults={'email': 'admin@example.com'}
        )
        
        if created:
            user.set_password('password123')
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Created user: {user.username}'))
        else:
            self.stdout.write(self.style.WARNING(f'User already exists: {user.username}'))

        # Create sample property
        property_data = {
            'title': 'Test Property',
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
        
        prop, created = Property.objects.get_or_create(
            title=property_data['title'],
            defaults=property_data
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created property: {prop.title}'))
        else:
            self.stdout.write(self.style.WARNING(f'Property already exists: {prop.title}'))

        self.stdout.write(self.style.SUCCESS(f'Total properties in database: {Property.objects.count()}'))
        self.stdout.write(self.style.SUCCESS('Sample data creation completed!'))
