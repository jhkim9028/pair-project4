from django.shortcuts import render,redirect
from .forms import CustomUserCreationFrom
# Create your views here.

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect("account:signup")
    else:
        form = CustomUserCreationFrom()
    context={
        "form":form
    }
    return render(request, 'account/signup.html',context)