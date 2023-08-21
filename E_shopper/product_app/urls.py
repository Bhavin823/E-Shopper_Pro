from django.contrib import admin
from django.urls import path
from product_app.views import ProductView,ProductDetailView

app_name = 'product_app'

urlpatterns = [
    path('products/<slug:productslug>', ProductView, name='products'),
    path('productdetail/<slug:productdetailslug>',ProductDetailView, name = 'productdetail'),
    # ... other product app URL patterns ...
]