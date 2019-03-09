app_name = 'household'
from django.contrib import admin
from django.urls import path,include
from . import views
app_name = 'household'
urlpatterns = [

    path("flowers1",views.flowers1,name="flowers"),
    path("vegetables",views.vegetables1,name="vegetables"),
    path("",views.household,name="household"),
    #path("farmer/",include("farmer.urls",namespace="cust_sell")),

]