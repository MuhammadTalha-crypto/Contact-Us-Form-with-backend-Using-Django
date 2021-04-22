# from django.contrib import admin
from django.urls import path
#importing views file from the current directory " . "
from . import views
    #Defining path for URLs
urlpatterns = [
    path('', views.index, name="Home"),
    path('home',views.index, name="Home"),
    path('contact', views.contact, name="contact")
]