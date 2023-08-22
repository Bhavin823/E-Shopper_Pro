from django.contrib import admin
from django.urls import path
from cart_app.views import add_to_cart,cartView

app_name = 'cart_app'

urlpatterns = [

    path('add_to_cart/<slug:productdetailslug>',add_to_cart, name='add_to_cart'),
    path('usercart', cartView, name='cart'),
]