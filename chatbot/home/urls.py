from django.contrib import admin
from django.urls import path
from home.views import chat,about,chatAPI

urlpatterns = [
    path('chat', chat ,name='home'),
    path('about', about, name='about'),
    path('api',chatAPI,name='chatAPI')
]
