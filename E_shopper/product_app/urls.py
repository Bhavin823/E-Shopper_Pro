from django.contrib import admin
from django.urls import path
from product_app.views import ProductView

app_name = 'product_app'

urlpatterns = [
    path('products/<slug:productslug>', ProductView, name='products'),
    # ... other product app URL patterns ...
]