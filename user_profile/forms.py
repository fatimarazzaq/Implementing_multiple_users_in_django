from django import forms
from users.models import Salon
from django.contrib.auth.models import User
from .models import SalonProfile,CustomerProfile


class SalonUserUpdationForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model = User
        fields=['username','email']

class SalonAddressUpdationForm(forms.ModelForm):
    class Meta:
        model = Salon
        fields = ['location','phone_number']

    
class SalonImageUpdationForm(forms.ModelForm):
    class Meta:
        model = SalonProfile
        fields = ['image']


# customer profile

class CustomerUserUpdationForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model = User
        fields=['username','email']


class CustomerImageUpdationForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ['image']