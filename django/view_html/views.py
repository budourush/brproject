from django.shortcuts import render
from django.views.generic import ListView
from .models import SampleModel


# Create your views here.

class UserList(ListView):
    template_name = 'list.html'
    model = SampleModel
