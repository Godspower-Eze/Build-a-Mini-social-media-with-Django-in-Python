from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreationForm, Login_Form
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def user_creation(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = CreationForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account successfully created for {user}')
            return redirect('login')
    elif request.method == 'GET':
        form = CreationForm()
    return render(request, 'users/creation_form.html', context)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = Login_Form()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = Login_Form(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Wrong credentials')
    elif request.method == 'GET':
        form = Login_Form()
    return render(request, 'users/login_user.html', context)


def user_logout(request):
    logout(request)
    messages.success(request, 'You have logged out successfully')
    return redirect('home')


def account(request):
    return render(request, 'users/account.html')
