from django.shortcuts import render,redirect
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth 
# Create your views here.


def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None :
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect ('login')
    else:
        return render(request, 'login.html')
    
def register(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']

        if password==c_password:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('register')
            else:
                user= User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'password is not same')
            return redirect('register')
    else:
        return render(request, 'register.html')
    
def home(request):
    return render(request,'home.html')