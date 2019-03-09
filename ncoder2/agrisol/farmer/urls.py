
from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'farmer'
urlpatterns = [

    path("", views.farmer, name="farmer"),

    path("crops",views.crops1,name="crops"),
    path("vegetables", views.farmer, name="vegetables"),

]