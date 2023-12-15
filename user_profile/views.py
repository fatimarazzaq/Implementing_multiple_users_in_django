from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SalonUserUpdationForm,SalonAddressUpdationForm,SalonImageUpdationForm
from users.decorators import salon_required,customer_required
from django.contrib import messages


@login_required
@salon_required
def edit_profile_salon(request):
    if request.method=='POST':
        try:
            su_form = SalonUserUpdationForm(request.POST,instance=request.user)
            sa_form = SalonAddressUpdationForm(request.POST,instance=request.user.salon)
            si_form = SalonImageUpdationForm(request.POST,request.FILES,instance=request.user.salon.salonprofile)
            if su_form.is_valid() and sa_form.is_valid() and si_form.is_valid():
                su_form.save()
                sa_form.save()
                si_form.save()
                messages.success(request,f"{request.user.salon}'s Profile Updated successfully.")

        except Exception as e:
            print(e)
    else:
        su_form = SalonUserUpdationForm(instance=request.user)
        sa_form = SalonAddressUpdationForm(instance=request.user.salon)
        si_form = SalonImageUpdationForm(instance=request.user.salon.salonprofile)
    context = {
        'su_form':su_form,
        'sa_form':sa_form,
        'si_form':si_form,
    }
    return render(request,'user_profile/profile.html',context)

@login_required
@customer_required
def edit_profile_cutomer(request):
    if request.method=='POST':
        try:
            su_form = SalonUserUpdationForm(request.POST,instance=request.user)
            si_form = SalonImageUpdationForm(request.POST,request.FILES,instance=request.user.customer.customerprofile)
            if su_form.is_valid() and si_form.is_valid():
                su_form.save()
                si_form.save()
                messages.success(request,f"{request.user.salon}'s Profile Updated successfully.")

        except Exception as e:
            print(e)
    else:
        su_form = SalonUserUpdationForm(instance=request.user)
        si_form = SalonImageUpdationForm(instance=request.user.customer.customerprofile)
    context = {
        'su_form':su_form,
        'si_form':si_form,
    }
    return render(request,'user_profile/cust_profile.html',context)


