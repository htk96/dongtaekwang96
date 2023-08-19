from django.shortcuts import render


def index(request):
    return render(request, 'users/index.html')


def id(request):
    return render(request, 'users/id.html')


def password(request):
    return render(request, 'users/password.html')


def register(request):
    return render(request, 'users/register.html')


def login(request):
    return render(request, 'users/login.html')


def home(request):
    return render(request, 'exams/home.html')
