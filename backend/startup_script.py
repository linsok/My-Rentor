#!/usr/bin/env python
import os
import sys
import django
from django.core.management import execute_from_command_line

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'housing_analyzer.settings')
django.setup()

def create_sample_data():
    """Create sample data if tables are empty"""
    try:
        from django.contrib.auth.models import User
        from properties.models import Property
        
        if Property.objects.count() == 0:
            print("📝 Creating sample data...")
            
            # Create admin user
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
                print("✅ Created admin user")
            
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
                    'owner': user
                },
                {
                    'title': 'Cozy Studio Near Park',
                    'description': 'Perfect studio apartment near park',
                    'address': '456 Park Ave',
                    'rent_price': 1200.00,
                    'bedrooms': 1,
                    'bathrooms': 1,
                    'area_sqm': 55,
                    'property_type': 'studio',
                    'status': 'available',
                    'verification_status': 'verified',
                    'owner': user
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
                    'owner': user
                }
            ]
            
            for prop_data in properties_data:
                prop, created = Property.objects.get_or_create(
                    title=prop_data['title'],
                    defaults=prop_data
                )
                if created:
                    print(f"✅ Created property: {prop.title}")
            
            print(f"📊 Total properties: {Property.objects.count()}")
        else:
            print(f"📊 Database already has {Property.objects.count()} properties")
            
    except Exception as e:
        print(f"❌ Failed to create sample data: {e}")

if __name__ == '__main__':
    print("🚀 Starting Housing Analyzer Backend Setup")
    
    # Create sample data (migrations already run by startCommand)
    create_sample_data()
    print("✅ Setup completed successfully")
