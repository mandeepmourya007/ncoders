from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User

def home(request):
    # events=event.objects.all()
    # print(events[0].image)
    # print(events)
    if request.method=="POST":
        print(request.POST)
        u=request.POST.get("username")
        p=request.POST.get("password")
        user=authenticate(request,username=u,password=p)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request, 'Welcome to TechFest '+ u )
            return redirect("home")
    return render(request,"home.html")

def farmer(request):
    return render(request,"farmer.html")
