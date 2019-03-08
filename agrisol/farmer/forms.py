from django import forms
from .models import *


class crops(forms.ModelForm):


    name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'First Name '}),required = True,max_length=30)
    images = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name '}), required=True,max_length=30)
    description = forms.ImageField()
    season = forms.ChoiceField(choices=state,required = True)
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'City'}),required = True,max_length= 50)
    rate = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'rate'}),required=True,max_length=50)

    class Meta():
        model = crops
        fields = ['first_name','last_name','images','state','city','rate']
