from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.deletion import CASCADE


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    

    def save_category(self):
        self.save()

    def __str__(self):
        return self.name

class photos(models.Model):
    name = models.CharField(max_length=30)
    image = CloudinaryField('image')
    image_description = models.CharField(max_length=100)
    category = models.ForeignKey('Category',on_delete=models.CASCADE, null=True)

    def save_photos(self):
        self.save()

    # update image
    def update_photos(self, name, description, category):
        self.name = name
        self.category = category
        self.description = description
        # self.location = location
    
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


