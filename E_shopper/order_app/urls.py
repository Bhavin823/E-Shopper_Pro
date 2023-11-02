from django.contrib import admin
from django.urls import path
from order_app.views import *

app_name = 'order_app'

urlpatterns = [
    path('create_order/',create_order, name='create_order'),
    path('order_detail<int:id>/',order_detail,name='order_detail'),

]