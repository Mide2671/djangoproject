from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from . models import Food
def Home(request):
    return render(request,'Home.html')

def menu(request):
    foods= Food.objects.all()
    return render(request, 'menu.html', {'foods': foods}) 
   
def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email is already used')
                return redirect('Register')
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'Username already used')
                return redirect('Register')
            else:
                user = User.objects.create_user(username = username,email= email, password=password)
                user.save()
                return redirect('Sign')
        else:
            messages.info(request, 'Password not the same')
            return redirect( 'Register')
    else:        
      return render(request, 'Register.html')
def Sign(request):
    if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username = username, password = password)
      if user is not None:
          auth.login(request, user)
          return redirect("Home")
      else:
          messages.info(request, 'credentials invalid')
          return redirect('Sign')
    else:
      return render(request, 'Sign.html')
def logout(request):
    auth.logout(request)
    return redirect('Home')
def order(request):
    return render (request,'order.html')