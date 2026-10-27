"""Viewsets for the cars API."""

from rest_framework import viewsets
from .serializer import CarSerializer
from .models import Car

# Create your views here.
class CarView(viewsets.ModelViewSet):
  """Provide standard CRUD actions over all cars using `CarSerializer`."""

  serializer_class = CarSerializer
  queryset=Car.objects.all()
