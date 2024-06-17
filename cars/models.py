from django.db import models

# Create your models here.
class Car(models.Model):
  marca = models.CharField(max_length=100)
  sucursal = models.CharField(max_length=100)
  aspirante = models.CharField(max_length=100)
  
  def __str__(self):
    return self.marca