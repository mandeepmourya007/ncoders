from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User
from accounts.forms import userform
from django.core.mail import EmailMessage

#email
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'akaaalinc@gmail.com'
EMAIL_HOST_PASSWORD = 'mandeepakaal'
EMAIL_PORT = 587


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
            user= User.objects.create_user(username=email,first_name=first_name,last_name =last_name,email=email,password =password)
            login(email,password)
            return redirect('home')
    form1 = userform()

    return render(request,'home.html',{'form':form1})
def Email(request):
    mail_subject = 'notification'
    to_email = ["sanyamjhingan99@gmail.com"]
    message='sanyam ka bhai ka laptop'
    email = EmailMessage(mail_subject, message, to=to_email)
    email.send()
