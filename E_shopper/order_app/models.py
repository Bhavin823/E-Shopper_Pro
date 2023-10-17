from django.db import models
from django.contrib.auth.models import User
from user_app.models import UserAddress

# Create your models here.
class OrderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(UserAddress, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Pending')
    order_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Order {self.id}'