from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def helloworldfunc(request):
    return HttpResponse("<h1>hello world</h1>")
