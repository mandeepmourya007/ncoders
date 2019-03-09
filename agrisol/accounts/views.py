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
