from django.shortcuts import render
from . forms import userform
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


app_name="accounts"
# Create your views here.
def log_out(request):
    logout(request)
    return redirect(('home'))

def sign_up(request):

    if request.method == 'POST':
        form1 = userform(request.POST)
        print(request.POST)
        if form1.is_valid():

        #    username = form1.cleaned_data['email']
            first_name = form1.cleaned_data['first_name']
            last_name = form1.cleaned_data['last_name']
            email = form1.cleaned_data['email']
            password=form1.cleaned_data['password']
            user= User.objects.create_user(username=email,first_name=first_name,last_name =last_name,email=email,password =password,is_active=False)
            login(email,password)
            return redirect('home')
    form1 = userform()

    return render(request,'home.html',{'form':form1})
