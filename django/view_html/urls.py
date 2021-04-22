from django.urls import path
from django.contrib import admin
from .views import UserList

urlpatterns = [
    path('user_list/', UserList.as_view())
]
