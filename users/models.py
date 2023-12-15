from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_salon    = models.BooleanField(default=False)

class Salon(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    location = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return f'/accounts/login/'

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return f'/accounts/login/'