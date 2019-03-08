from django import forms
from .models import *

class seller(forms.ModelForm):
    state = (('Punjab', 'Punjab'),
             ('Delhi', 'Delhi'),
             ('Bihar', 'Bihar'),
             ('UP', 'UP'),
             ('Orissa', 'Orissa'),
             ('Haryana', 'Haryana'),
             ('Meghalaya', 'Meghalaya'),

             )

    first_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'First Name '}),required = True,max_length=25)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name '}), required=True,max_length=25)
    images = forms.ImageField()
    state = forms.ChoiceField(choices=state,required = True,max_length=25)
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'City'}),required = True,max_length= 25)
    rate = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'rate'}),required=True)

    class Meta():
        model = seller
        fields = ['first_name','last_name','images','state','city','rate']

class customer(forms.ModelForm):

    first_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'First Name '}),required = True,max_length=25)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name '}), required=True, max_length=25)
    mobile_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'your Name '}), required=True, max_length=10)

    class Meta():
        model = customer
        fields = ['first_name','last_name','mobile_number']
