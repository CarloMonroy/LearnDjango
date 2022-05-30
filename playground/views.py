from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request habndler

def calculate():
    x=1
    y=2
    return x


def say_hello(request):
    ##Fo stuff
    x = calculate()
    return render(request, 'hello.html', {'name': 'Mosh'})
    