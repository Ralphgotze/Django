from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def indexView(request):
    return render(request,'users/index.html')
@login_required()
def dashboardView(request):
    return render(request,'users/dashboard.html')
def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users/login.html')
    else:
        form = UserCreationForm()
    return render(request,'users/register.html',{'form':form})