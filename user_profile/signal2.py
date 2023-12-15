from django.db.models.signals import post_save
# from django.contrib.auth.models import User
from users.models import Customer
from django.dispatch import receiver
from .models import CustomerProfile

# customer profile


@receiver(post_save,sender=Customer)
def create_profile(sender,instance,created,**kwargs):
    if created :
        CustomerProfile.objects.create(customer=instance)


@receiver(post_save,sender=Customer)
def save_profile(sender,instance,**kwargs):
    instance.customerprofile.save()