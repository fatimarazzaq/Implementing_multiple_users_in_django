from django.contrib import admin
from .models import User,Salon,Customer

# Register your models here.
admin.site.register(User)
admin.site.register(Salon)
admin.site.register(Customer)
