app_name = 'household'
from django.contrib import admin
from django.urls import path,include
from . import views
app_name = 'household'
urlpatterns = [
    path("",views.household,name="household"),
    #path("farmer",views.farmer,name="farmer"),
    #path("farmer/",include("farmer.urls",namespace="cust_sell")),

]