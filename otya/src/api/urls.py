from django.urls import path
from django.contrib import admin
from api import views

urlpatterns = [
    path('v1/test/', views.api)
]
