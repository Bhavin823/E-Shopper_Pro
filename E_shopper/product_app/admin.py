from django.contrib import admin
from product_app.models import ProductModel

# Register your models here.
@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['ProductName','ProductImage','category','subcategory','ProductPrice']