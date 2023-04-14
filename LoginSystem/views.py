from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request,'home.html')


def login_fun(request):
    return render(request,'login.html')


def login_read(request):
    uname=request.POST['tbusername']
    password=request.POST['tbpass']
    myuser = authenticate(username=uname, password=password)
    if myuser is not None:
        login(request,myuser)
        return redirect('displaystudent')
    else:
        return render(request,'login.html')


def register_fun(request):
    return render(request,'register.html')


def register_read(request):
    uname = request.POST['tbusername']
    email = request.POST['tbemail']
    password = request.POST['tbpass']
    user = User.objects.create_superuser(username=uname,email=email,password=password)
    user.save()
    return render(request,'login.html',{'name': user, 'msg': f'user created successfully username is {uname}'})


def logout_fun(request):
    logout(request)
    return redirect('login')
