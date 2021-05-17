from django.db import models

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
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE,)
    category = models.ManyToManyField(Category)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title