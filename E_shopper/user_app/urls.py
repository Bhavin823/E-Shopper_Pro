from django.contrib import admin
from django.urls import path
from user_app.views import *

app_name = 'user_app'

urlpatterns = [
    
    path('signup/',signupView,name='signup'),
    # path('signuphandle/',handelSignup,name='signuphandle'),
    path('signuphandle',handelSignup, name='signuphandle'),

    path('login/',loginView,name='login'),

]