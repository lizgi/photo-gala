from django.contrib import admin
from .models import Category, photos,Location

admin.site.register(photos)
admin.site.register(Category)
admin.site.register(Location)
# Register your models here.
