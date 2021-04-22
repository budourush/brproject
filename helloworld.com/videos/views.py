from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Video
from django.urls import reverse_lazy


class VideoList(generic.ListView):
    model = Video


class VideoCreate(generic.ListView):
    model = Video
    fields = '__all__'
    success_url = reverse_lazy('videos:video_list')


class VideoDetail(generic.DetailView):
    model = Video
