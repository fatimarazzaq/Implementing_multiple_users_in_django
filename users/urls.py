from django.urls import path
from . import views
from django.contrib.auth import views as login_views
from user_profile import views as profile_views

urlpatterns = [
    path("",views.index,name='home'),
    path('accounts/register/customer/', views.CustomerSignupView.as_view(),name='customer_register'),
    path('accounts/register/salon/', views.SalonSignupView.as_view(),name='salon_register'),
    path('accounts/login/',login_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('accounts/logout/',views.custom_logout,name='logout'),

    # profile urls
    path("edit/salon/profile/",profile_views.edit_profile_salon,name='edit_profile_salon'),
    path("edit/customer/profile/",profile_views.edit_profile_cutomer,name='edit_profile_customer'),

]
