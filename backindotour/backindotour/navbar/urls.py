# src/navbar/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import  MenuItemViewSet, DropdownMenuItemViewSet, MegaMenuItemViewSet

router = DefaultRouter()
router.register(r'menu-items', MenuItemViewSet)
router.register(r'dropdown-items', DropdownMenuItemViewSet)
router.register(r'mega-items', MegaMenuItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
