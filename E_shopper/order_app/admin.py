from django.contrib import admin
from order_app.models import OrderModel,OrderItem

# Register your models here.
@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','user','shipping_address','payment_type','total_amount','status','order_date',]
     
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id','order','product','quantity','price']
