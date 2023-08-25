from django.db import models
from django.contrib.auth.models import User
from product_app.models import ProductModel
# Create your models here.
class CartItemModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.product.ProductPrice * self.quantity
    
    def __str__(self) -> str:
        return f"{self.user.username} Has {self.product.ProductName} With {self.quantity} Quantity"
    
class CartModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItemModel)
    created_at = models.DateTimeField(auto_now_add=True)

     
