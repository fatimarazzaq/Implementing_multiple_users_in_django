from django.db.models.signals import post_save
# from django.contrib.auth.models import User
from users.models import Salon,Customer
from django.dispatch import receiver
from .models import SalonProfile,CustomerProfile

@receiver(post_save,sender=Salon)
def create_profile(sender,instance,created,**kwargs):
    if created :
        SalonProfile.objects.create(salon=instance)


@receiver(post_save,sender=Salon)
def save_profile(sender,instance,**kwargs):
    instance.salonprofile.save()
    


