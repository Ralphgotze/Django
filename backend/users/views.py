from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import is_valid_path
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form =  UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'account created for {username}')
            return redirect('../../blog/')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form': form})

@login_required

def editProfile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated!')
            return redirect('../profile')
        elif u_form.is_valid() == False or u_form.is_valid() == False:
            return redirect('../edit-profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        if u_form.is_valid() == None and p_form.is_valid() == None:
            return redirect('../edit-profile')

    context = {
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request,'users/edit-profile.html',context)

def profile(request):
    return render(request,'users/profile.html')