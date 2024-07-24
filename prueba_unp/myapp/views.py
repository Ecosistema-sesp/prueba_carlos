# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import LoginForm

def home(request):
     return render(request, 'myapp/home.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('success')
    else:
        form = LoginForm()
    return render(request, 'myapp/login.html', {'form': form})

def success_view(request):
    return render(request, 'myapp/success.html', {'message': 'You have successfully logged in!'})
