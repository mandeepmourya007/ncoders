from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
#from .forms import studentreg , userform


from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site

def sign_up(request):
    if request.method == 'POST':
        form1 = userform(request.POST)
        if form1.is_valid():
            username = form1.cleaned_data['email']
            first_name = form1.cleaned_data['first_name']
            last_name = form1.cleaned_data['last_name']
            email = form1.cleaned_data['email']
            password=form1.cleaned_data['password']
            user= User.objects.create_user(username=username,first_name=first_name,last_name =last_name,email=email,password =password,is_active=False)

            #encod = user.email.encode('base64','strict'),


            return HttpResponseRedirect('/')

    else:
        form1 = userform()
    return render(request,'accounts/register.html',{'form':form1})






# Create your models here.
