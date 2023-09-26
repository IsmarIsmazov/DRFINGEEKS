from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=155)
    descriptions = models.TextField()
    created_at = models.DateField(auto_now=True)
    modifite_at = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
