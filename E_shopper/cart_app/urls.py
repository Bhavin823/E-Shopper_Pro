from django.contrib import admin
from django.urls import path
from cart_app.views import add_to_cart,cartView,delete_cart_item,clear_cart

app_name = 'cart_app'

urlpatterns = [
    # for add items in cart
    path('add_to_cart/<slug:productdetailslug>',add_to_cart, name='add_to_cart'),
    # for cart page
    path('usercart', cartView, name='cart'),
    path('deleteitem/<int:item_id>', delete_cart_item, name='delete_cart_item'),
    path('clearcart', clear_cart, name='clear_cart'),

]