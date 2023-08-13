from django.shortcuts import render

# Create your views here.
def baseview(request):
    return render(request,'base_app/base.html')