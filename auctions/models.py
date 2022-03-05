from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    seller = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=64)
    img_link = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)

class Listings(models.Model):
    seller = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    description = models.TextField()
    category = models.CharField(max_length=64)
    img_link = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)