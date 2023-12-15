from django.shortcuts import render
from .forms import SalonSignupForm,CustomerSignupForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import login
from django.shortcuts import redirect

# Create your views here.

def index(request):
    return render(request,'users/home.html')


class CustomerSignupView(CreateView):
    model = User
    form_class = CustomerSignupForm
    template_name = 'users/custRegistration.html'

class SalonSignupView(CreateView):
    model = User
    form_class = SalonSignupForm
    template_name = 'users/register.html'
    success_message = f'Your Account has been created.You can now Login.'

def custom_logout(request):
    logout(request)
    return render(request,'users/logout.html') 


# Create your views here.

