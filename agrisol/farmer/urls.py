
from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'farmer'
urlpatterns = [

    path("", views.farmer, name="farmer"),
    # path("farmer",views.farmer,name="farmer"),
    #path("farmer/", include("farmer.urls", namespace="cust_sell")),

]