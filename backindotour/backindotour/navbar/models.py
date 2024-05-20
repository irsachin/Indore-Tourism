from django.db import models

class Navbar(models.Model):
    logo = models.ImageField(upload_to='logos/')
    account_icon = models.ImageField(upload_to='icons/', blank=True, null=True)
    wishlist_icon = models.ImageField(upload_to='icons/', blank=True, null=True)
    social_icons = models.JSONField(default=dict, blank=True, null=True) 

    def __str__(self):
        return "Navbar"

class MenuItem(models.Model):
    navbar = models.ForeignKey(Navbar, related_name='menu_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)
    is_dropdown = models.BooleanField(default=False)
    is_mega_menu = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class DropdownMenuItem(models.Model):
    menu_item = models.ForeignKey(MenuItem, related_name='dropdown_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name

class MegaMenuItem(models.Model):
    menu_item = models.ForeignKey(MenuItem, related_name='mega_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name
