# src/navbar/admin.py

from django.contrib import admin
from .models import  MenuItem, DropdownMenuItem, MegaMenuItem

class DropdownMenuItemInline(admin.TabularInline):
    model = DropdownMenuItem
    extra = 1

class MegaMenuItemInline(admin.TabularInline):
    model = MegaMenuItem
    extra = 1

class MenuItemAdmin(admin.ModelAdmin):
    inlines = [DropdownMenuItemInline, MegaMenuItemInline]
    list_display = ('name', 'url', 'is_dropdown', 'is_mega_menu')
    list_filter = ('is_dropdown', 'is_mega_menu')
    search_fields = ('name',)

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(DropdownMenuItem)
admin.site.register(MegaMenuItem)
