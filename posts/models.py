from django.db import models
from cloudinary.models import CloudinaryField
from .link_generator import generate_shareable_link

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    title = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.title

class Photo(models.Model):
    
    sharable_link = generate_shareable_link()
   
    title = models.CharField(max_length=255, default=None)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE,)
    category = models.ManyToManyField(Category)
    date = models.DateTimeField(auto_now=True)
    img_url = CloudinaryField('image')
    sharable_link = models.CharField(max_length=255, unique=True, default=sharable_link)

    def __str__(self):
        return self.title