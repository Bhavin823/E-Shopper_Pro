from django.contrib import admin
from django.urls import path
from user_app.views import *

app_name = 'user_app'

urlpatterns = [
    
    # signup handle
    path('signup/', signupView, name='signup'),
    path('signuphandle', handelSignup, name='signuphandle'),

    # login handle
    path('login/', loginView, name='login'),
    path('loginhandle', handleLogin, name='loginhandle'),

    # logout handle
    path('logouthandle',logouthandle, name='logouthandle'),

    # profile 
    path('profile',profileView,name='profile'),

]