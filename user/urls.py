from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index),
    path('index/', views.index,name='homePage'),
    path('base/', views.base),
    path('signUp/', views.signUp),
    path('login/', views.logIn),
    path('resetPass/', views.resetPass),
    
]
