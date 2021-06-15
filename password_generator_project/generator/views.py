from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):

    charactrs = list('qwertyuiopasdfghjklzxcvbnm')

    if request.GET.get('uppercase'):
        charactrs.extend('QWERTYUIOPASDFGHJKLZXCVBNM')
    if request.GET.get('numbers'):
        charactrs.extend('1234567890')
    if request.GET.get('special'):
        charactrs.extend('!@#$%^&*()_+=')

    length = int(request.GET.get('length', 8))

    if length > 30:
        raise Exception('Слишком большая длина пароля')

    thepassword = ''

    for letters in range(length):
        thepassword += random.choice(charactrs)


    return render(request, 'generator/password.html', {'password': thepassword})