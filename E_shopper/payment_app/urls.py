# dj_razorpay/urls.py

from django.contrib import admin
from django.urls import path
from payment_app import views

app_name = 'payment_app'

urlpatterns = [
    
	path('initialize_razorpay/<int:order_id>/', views.initialize_razorpay, name='initialize_razorpay'),
    path('razorpay_payment_success/', views.razorpay_payment_success, name='razorpay_payment_success'),
	
]
