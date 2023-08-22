from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login ,logout
from django.db.models import Q
from django.http import JsonResponse,HttpResponse
from user_app.models import UserProfile

# Create your views here.
def signupView(request):  
     # Render the signup.html template
    return render(request,'user_app/signup.html')

def handelSignup(request):
    if request.method == "POST":
         # Get the POST values from the form
        username = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        password1 = request.POST['pass']
        password2 = request.POST['re_pass']
        
        # Check if password1 and password2 match
        if password1 == password2:
            
            # Check if a user with the same email or username already exists
            data = User.objects.filter(Q(email=email) | Q(username=username)) 
            if len(data) <= 0:
                
                # Create a new User instance
                myuser = User.objects.create_user(username, email, password1)
                
                # Create a UserProfile instance and associate it with the user
                user_profile = UserProfile.objects.create(user=myuser, contact=contact)
                
                # Render a success message
                return render(request,'user_app/login.html',{'messagekey':'Registration Successful!'})
            else:
                # Render a message for existing user
                return render(request,'user_app/signup.html',{'messagekey':'User Already Exists'})
        else:
            # Render a message for password mismatch
            return render(request,'user_app/signup.html',{'messagekey':'Password Does Not Match'})
    else:
        # Return a 404 response for non-POST requests
        return HttpResponse('404 - Not Found')


def loginView(request):
    return render(request,'user_app/login.html')