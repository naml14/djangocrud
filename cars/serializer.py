"""Serialize car model records for Django REST Framework."""

from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
  """Convert car records to and from the API representation."""

  class Meta:
    """Expose every model field through the serializer."""
    model=Car
    fields = '__all__'