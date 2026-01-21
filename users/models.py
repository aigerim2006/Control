from django.db import models
from django.contrib.auth.models import User

# Профиль пользователя (OneToOne)
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="user_profile"  # уникальное имя, чтобы не конфликтовать
    )
    age = models.PositiveIntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to="profiles/", null=True, blank=True)
    def __str__(self):
        return f"{self.user.username} Profile"


# Продукты пользователя (OneToMany)


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to="products/", null=True, blank=True)
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
