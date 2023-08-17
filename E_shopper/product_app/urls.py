from django.contrib import admin
from django.urls import path
from product_app.views import productView

app_name = 'product_app'


urlpatterns = [

    path('products/<slug:productslug>',productView,name='product'),
    
]