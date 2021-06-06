from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):

    charactrs = list('qwertyuiopasdfghjklzxcvbnm')
    length = 10
    thepassword = ''

    for letters in range(length):
        thepassword += random.choice(charactrs)


    return render(request, 'generator/password.html', {'password': thepassword})