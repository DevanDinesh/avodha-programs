from django.db import models

# Create your models here.
class shop(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField(max_length=50)
    price=models.IntegerField()
    img=models.ImageField()