

from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'accounts'
urlpatterns = [


    path("signup", views.sign_up, name="sign_up"),
    #path("login", views.log_in, name="login"),
    # path("farmer",views.farmer,name="farmer"),
    #path("farmer/", include("farmer.urls", namespace="cust_sell")),
    path("logout",views.log_out,name="logout"),

]
