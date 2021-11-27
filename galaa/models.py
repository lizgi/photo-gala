from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class photos(models.Model):
    name = models.CharField(max_length=30)
    image = CloudinaryField('image')
    image_description = models.CharField(max_length=100)


    def save_photos(self):
        self.save()


    # update image
    def update_photos(self, name, description):
        self.name = name
        self.description = description
        # self.location = location
        self.category = category
        self.save()

    # get all images
    @classmethod
    def get_all_images(cls):
        photo = photos.objects.all()
        return photos

    @classmethod
    def search_by_name(cls,search_term):
        photos = cls.objects.filter(name__icontains=search_term)
        return photos
