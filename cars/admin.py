"""Register car models with the Django administration site."""

from django.contrib import admin
from .models import Car

# Register your models here.
admin.site.register(Car)