"""Root URL configuration for the project.

Mounts the Django admin and includes the cars application under `/cars/`.
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/',include('cars.urls'))
]
