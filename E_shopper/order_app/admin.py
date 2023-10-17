from django.contrib import admin
from order_app.models import OrderModel

# Register your models here.
@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','shipping_address','payment_type','total_amount','status','order_date']

