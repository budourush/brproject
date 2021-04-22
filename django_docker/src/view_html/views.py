from django.shortcuts import render
from django.views.generic import ListView, View
from .models import SampleModel


# Create your views here.

class UserList(ListView):
    template_name = 'list.html'
    model = SampleModel


class HelloView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'message': "Hello World! from View!!",
        }
        return render(request, 'hello.html', context)

    def post(self, request, *args, **kwargs):
        context = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message']
        }
        return render(request, 'hello.html', context)
