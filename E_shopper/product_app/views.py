from django.shortcuts import render

# Create your views here.
def productView(request,productslug):
    return render(request,'product.html')
