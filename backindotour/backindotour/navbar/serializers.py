

from rest_framework import serializers
from .models import  MenuItem, DropdownMenuItem, MegaMenuItem

class DropdownMenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropdownMenuItem
        fields = ['id', 'name', 'url']

class MegaMenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MegaMenuItem
        fields = ['id', 'name', 'url']

class MenuItemSerializer(serializers.ModelSerializer):
    dropdown_items = DropdownMenuItemSerializer(many=True, read_only=True)
    mega_items = MegaMenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'url', 'is_dropdown', 'is_mega_menu', 'dropdown_items', 'mega_items']

