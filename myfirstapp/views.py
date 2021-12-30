from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return  render(request, 'myfirstapp/home.html')

def about(request):
    return  render(request, 'myfirstapp/about.html')


def password(request):

    charecters = list('abcdefghijklmnopqrstuvwxyz')

    if  request.GET.get('uppercase'):
        charecters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYX'))
    if request.GET.get('number'):
        charecters.extend(list('0123456789'))
    if request.GET.get('special'):
        charecters.extend(list('!@#$%^&*'))


    length = int(request.GET.get('length'))

    thepassword = ' '
    for x in range(length):
        thepassword += random.choice(charecters)


    return render(request, 'myfirstapp/password.html',{'password': thepassword})
