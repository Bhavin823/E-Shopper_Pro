from django.contrib import admin
from cart_app.models import CartItemModel,CartModel
# Register your models here.

@admin.register(CartModel)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user','created_at']

@admin.register(CartItemModel)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['user','product','quantity']