from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationFrom

# Create your views here.

def index(request):
    return render(request, 'account/index.html')

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect("account:index")
    else:
        form = CustomUserCreationFrom()
    context={
        "form":form
    }
    return render(request, 'account/signup.html',context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('account:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'account/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('account:index')