from django.shortcuts import render
from .models import *
# Create your views here.
def farmer(request):
    return render(request,'farmer/farmer.html')

def crops1(request):
    crop= crops.objects.filter(season=request.POST['crops'])
    return render(request,'farmer/crop.html',{'crops':crop})

