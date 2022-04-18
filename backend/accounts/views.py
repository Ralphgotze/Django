from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from .models import User


def home(req):
    return render(req,'users/index.html')

# def login(req):
#     if req.method=="POST":
#         user = User()
#         user.name= req.POST['name']
#         user.email= req.POST['email']
#         user.password= req.POST['password']
#         user.repassword= req.POST['repassword']

    # return render(req,'users/login.html')



def login(req):
    if req.method=="POST":
        user = User()
        user.email= req.POST['email']
        user.password= req.POST['password']
        def authenticated():
            if(User.objects.filter(email=user.email) and (User.objects.filter(password=user.password))):
                return redirect('../../blog/')
            elif (User.objects.exclude(email=user.email) or (User.objects.exclude(password=user.password))):
                return redirect('register.html')
            elif (User.objects.filer(email="") or (User.objects.filer(password=""))):
                messages.info(req,"some fields are empty")
                return redirect('register.html')

        

    return render(req,'users/login.html')

    

def register(req):
    if req.method=="POST":
        user = User()
        user.name= req.POST['name']
        user.email= req.POST['email']
        user.password= req.POST['password']
        user.repassword= req.POST['repassword']
        if user.password != user.repassword:
            return redirect('register.html')
        elif user.name =="" or user.password =="":
            messages.info(req,"some fields are empty")
            return redirect('register.html')
        else:
            user.save()

    return render(req,'users/register.html')