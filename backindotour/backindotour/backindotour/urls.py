# src/your_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('navbar/', include('navbar.urls')),  # Ensure the app name is all lowercase
]
