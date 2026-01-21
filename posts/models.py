from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=100)

class Tag(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # OneToMany
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
