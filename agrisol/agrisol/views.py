from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User
from accounts.forms import userform


def log_out(request):
    logout(request)
    return redirect(('home'))
def home(request):
    if request.method=="POST":
        print(request.POST)
        u=request.POST.get("email")
        p=request.POST.get("password")
        user=authenticate(request,username=u,password=p)
        if user is not None:
            login(request,user)
            messages.success(request, ' Welcome to  kissan '+ u )
            return redirect("home")
    return render(request,"home.html",{'form':userform})

def farmer(request):
    return render(request,"farmer.html")
