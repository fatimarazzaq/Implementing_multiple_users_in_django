from django.db import models
from users.models import Salon,Customer
from PIL import Image

# Create your models here.


class SalonProfile(models.Model):
    salon = models.OneToOneField(Salon,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return self.salon.user.username

    # def save(self):
    #     super().save()

    #     img=Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         remain_size=(300,300)
    #         img.thumbnail(remain_size)
    #         img.save(self.image.path)




class CustomerProfile(models.Model):
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return self.customer.user.username