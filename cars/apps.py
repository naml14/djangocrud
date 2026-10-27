from django.apps import AppConfig


class CarsConfig(AppConfig):
    """Configure the Django application that owns car models and API routes."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'
