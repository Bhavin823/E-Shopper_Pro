from django.db import models
from django.contrib.auth.models import User
from user_app.models import UserAddress
from cart_app.models import CartItemModel
from product_app.models import ProductModel

# Create your models here.
class OrderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(UserAddress, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Pending')
    order_date = models.DateTimeField(auto_now_add=True)    
    ordered_items = models.ManyToManyField(ProductModel, through='OrderItem')
    razorpay_order_id = models.CharField(max_length=100,null=True)
    razorpay_payment_id = models.CharField(max_length=100,null=True)
    razorpay_signature = models.CharField(max_length=100,null=True)

    
class OrderItem(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    @property
    def subtotal(self):
        return self.quantity * self.price