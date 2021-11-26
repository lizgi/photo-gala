from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class photos(models.Model):
    
    image_name = models.CharField(max_length=30)
    image = CloudinaryField('image')
    image_description = models.CharField(max_length=100)
