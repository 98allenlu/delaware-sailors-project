"""
URL configuration for api_project project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This includes the URLs from our 'voyages' app
    path('api/', include('voyages.urls')), 
]
