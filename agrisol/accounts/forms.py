from django import forms

from django.contrib.auth.models import User



class userform(forms.ModelForm):

    first_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'First Name '}),required = True,max_length=30)
    last_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Last Name'}),max_length = 30)
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Email'}),required=True,max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}),required = True,max_length= 50)
    #confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}),required=True,max_length=50)

    class Meta():
        model = User
        fields = ['first_name','last_name','email','password']
