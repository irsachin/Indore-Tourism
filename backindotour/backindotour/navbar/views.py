

from rest_framework import viewsets
from .models import Navbar, MenuItem, DropdownMenuItem, MegaMenuItem
from .serializers import  MenuItemSerializer, DropdownMenuItemSerializer, MegaMenuItemSerializer



class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class DropdownMenuItemViewSet(viewsets.ModelViewSet):
    queryset = DropdownMenuItem.objects.all()
    serializer_class = DropdownMenuItemSerializer

class MegaMenuItemViewSet(viewsets.ModelViewSet):
    queryset = MegaMenuItem.objects.all()
    serializer_class = MegaMenuItemSerializer
