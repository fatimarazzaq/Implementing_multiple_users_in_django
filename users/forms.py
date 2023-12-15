from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Salon,User,Customer

class SalonSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    location = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model=User
        fields = ['username','email','password1','password2','location','phone_number']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_salon =True
        user.save()
        salon = Salon.objects.create(user=user)
        salon.location = self.cleaned_data.get('location')
        salon.phone_number = str(self.cleaned_data.get('phone_number'))
        salon.save()
        return salon


    

class CustomerSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','password1','password2']
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer=Customer.objects.create(user=user)
        customer.save()
        return customer

    