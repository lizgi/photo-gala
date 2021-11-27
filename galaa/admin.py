from django.contrib import admin
from .models import Category, photos

admin.site.register(photos)
admin.site.register(Category)
# Register your models here.
