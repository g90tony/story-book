from django.db import models
from cloudinary import CloudinaryImage
import random 
import string 

# Create your models here.
class Location(models.Model):
    name: models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    title: models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Photo(models.Model):
    
    def generate_shareable_link(self):
        letters = string.ascii_letters
        numbers = string.digits
        specialCharacters = string.punctuation

        acceptable_characters = letters + numbers + specialCharacters
        generated_link = "".join(random.choice(acceptable_characters) for i in range(8))

        existing_link = Photo.objects.filter(sharable_link = generated_link)
        
        if existing_link:
            self.generate_shareable_link()
        else:
            return generated_link
    
    sharable_link = generate_shareable_link()
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE,)
    category = models.ManyToManyField(Category)
    date = models.DateTimeField(auto_now=True)
    img_url = CloudinaryImage(max_length=255, blank=True)
    sharable_link = models.CharField(default=sharable_link)

    def __str__(self):
        return self.title