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
    # fetch detail from post page for return after login
    retpath = request.GET.get('retpath', '')
    subcatslug = request.GET.get('subcatslug', '')
    productslug = request.GET.get('productslug', '')
    # print(retpath)
    # print(subcatslug)
    # print(productslug)
    context={
        'retpath':retpath,
        'subcateslug':subcatslug,
        'productslug':productslug,
    }
    return render(request,'user_app/login.html',context)

def handleLogin(request):
    if request.method == "POST":
        # retrive from login form
        retpath = request.POST.get('retpath', '')
        subcatslug = request.POST.get('subcatslug', '')
        productslug = request.POST.get('productslug', '')

        
        # print("repath:",retpath)
        # print("subcatslug:",subcatslug)
        # print('productslug',productslug)

        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpass']

        user = authenticate(username = loginusername, password = loginpassword)

        if user is not None:
            # If the user is authenticated, log them in and redirect to the home page
            login(request,user)
            print('login successfully')
            # check in url and then redirect to return page
            if retpath == "prolog":
                return redirect('product_app:products',subcatslug=subcatslug)
            elif retpath == 'prodet':
                return redirect('product_app:productdetail',productslug=productslug)
            return redirect('home')
        else:
            # If authentication fails, render the login page with an error message
            return render(request,'user_app/login.html', {'messagekey':" Inavalid Credentials !"})
    # If the request method is not POST, return a 404 response
    return HttpResponse('404 - Not Found')

def logouthandle(request):
    logout(request)
    print("logout")
    return redirect('home')