from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login ,logout
from django.db.models import Q
from django.http import JsonResponse,HttpResponse
from user_app.models import UserProfile

# Create your views here.
def signupView(request):
    return render(request,'user_app/signup.html')

def handelSignup(request):
    if request.method == "POST":
        # get the POST Value
        username = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        password1 = request.POST['pass']
        password2 = request.POST['re_pass']
        
        # check password1 and password2 are same!
        if password1 == password2:
            # Check if a user with the same email or username already exists
            data = User.objects.filter(Q(email=email) | Q(username=username)) 
            if len(data) <= 0:
                myuser = User.objects.create_user(username, email, password1)
                user_profile = UserProfile.objects.create(user=myuser, contact=contact)
                return render(request,'user_app/login.html',{'messagekey':'Registration Successful!'})
            else:
                return render(request,'user_app/signup.html',{'messagekey':'User Already Exists'})
        else:
            return render(request,'user_app/signup.html',{'messagekey':'Password Does Not Match'})
    else:
        return HttpResponse('404 - Not Found')


def loginView(request):
    return render(request,'user_app/login.html')