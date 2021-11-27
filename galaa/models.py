from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class photos(models.Model):
    name = models.CharField(max_length=30)
    image = CloudinaryField('image')
    image_description = models.CharField(max_length=100)

    @classmethod
    def search_by_name(cls,search_term):
        photos = cls.objects.filter(name__icontains=search_term)
        return photos
