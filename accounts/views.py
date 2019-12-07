from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
import re

def register(request):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        #phone = request.POST['phone']
        email = request.POST['email']   
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
         #check if passwords match
        if password == password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is taken')
                return redirect('register')
            else:
                #check email
                if re.search(regex,email):
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'Email is already registerd')
                        return redirect('register')
                    else:
                        #looks good
                        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                        user.save()
                        messages.success(request, 'You are now registerd and can log in')
                        return redirect('login')
                else:
                    messages.error(request, 'Email is not valid')
                    return redirect('register')
        else:       
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')

def cart(request):
    return render(request,'accounts/cart.html')