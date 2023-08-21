from django.contrib import admin
from django.urls import path
from user_app.views import signupView,loginView

app_name = 'user_app'

urlpatterns = [
    
    path('signup/',signupView,name='signup'),
    path('login/',loginView,name='login'),

]