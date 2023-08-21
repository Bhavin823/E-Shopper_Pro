from django.contrib import admin
from django.urls import path
from user_app.views import signupView

app_name = 'user_app'

urlpatterns = [
    
    path('signup/',signupView,name='signup'),

]