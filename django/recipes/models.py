from django.db import models

# Create your models here.
class recipe(models.Model):
    rName = models.CharField(max_length=255)
    rTime = models.CharField(max_length=255)
    rSize = models.CharField(max_length=255)
    ingredients = models.TextField(default= "")
    directions = models.TextField(default="")
