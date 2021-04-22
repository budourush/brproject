from django.urls import path
from django.contrib import admin
from .views import UserList, HelloView

urlpatterns = [
    path('user_list/', UserList.as_view(), name='ul'),
    path('hello', HelloView.as_view(), name='hello')
]
