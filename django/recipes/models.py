from django.db import models

# Create your models here.
class recipe(models.Model):
    Title = models.CharField(max_length=255, null=False)
    Cooking_Time = models.CharField(max_length=255, null=False)
    Serving_Size = models.CharField(max_length=255)
    Ingredients = models.TextField(default= "", null=False)
    Directions = models.TextField(default="", null=False)
