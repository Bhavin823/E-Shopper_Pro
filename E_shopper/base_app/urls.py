
from django.contrib import admin
from django.urls import path,include
from base_app import views

urlpatterns = [

    path('', views.baseview),
    path('home/',views.homeview,name='home'),
    
]