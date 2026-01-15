"""
URL configuration for housing_analyzer project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        'message': 'Housing Analyzer API',
        'version': '1.0.0',
        'endpoints': {
            'admin': '/admin/',
            'auth': '/api/auth/',
            'properties': '/api/properties/',
            'bookings': '/api/bookings/',
            'analytics': '/api/analytics/',
            'payments': '/api/payments/',
            'reviews': '/api/reviews/',
            'health': '/health/'
        }
    })

def health_check(request):
    try:
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
        return JsonResponse({
            'status': 'healthy',
            'database': 'connected',
            'tables': [table[0] for table in tables]
        })
    except Exception as e:
        return JsonResponse({
            'status': 'unhealthy',
            'error': str(e)
        }, status=500)

urlpatterns = [
    path('', api_root, name='api-root'),
    path('health/', health_check, name='health-check'),
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/properties/', include('properties.urls')),
    path('api/bookings/', include('bookings.urls')),
    path('api/analytics/', include('analytics.urls')),
    path('api/payments/', include('payments.urls')),
    path('api/reviews/', include('reviews.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
