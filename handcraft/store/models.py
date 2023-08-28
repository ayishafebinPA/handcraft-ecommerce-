
from django.db import models

# Create your models here.

class craft(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=400)
    price=models.IntegerField()
    picture=models.ImageField(upload_to='craft_images')
