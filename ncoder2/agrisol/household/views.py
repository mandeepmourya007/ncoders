from django.shortcuts import render

from farmer.models import vegetables
from  .models  import flowers
from django.contrib.auth.models import User

#from .models import flowers
# Create your views here.


def household(request):
    return render(request,'household/household.html')

def flowers1(request):

    flower = flowers.objects.filter(season=request.POST['flowers'])

    print(flower[0].images)


    return render(request,"household/flowers.html",{"flowers":flower})

def vegetables1(request):
    veg= vegetables.objects.filter(season=request.POST['vegetables'])
    return render(request,'household/vegetables.html',{'veg':veg})