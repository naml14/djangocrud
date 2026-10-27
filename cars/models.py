from django.db import models

# Create your models here.
class Car(models.Model):
  """Represent a car record with brand, branch and aspirant text fields."""

  marca = models.CharField(max_length=100)
  sucursal = models.CharField(max_length=100)
  aspirante = models.CharField(max_length=100)
  
  def __str__(self):
    """Return the car's brand as its human-readable label."""
    return self.marca