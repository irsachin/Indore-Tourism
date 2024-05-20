# src/navbar/apps.py

from django.apps import AppConfig

class NavbarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'navbar'  # Ensure this matches the directory name
