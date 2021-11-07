from django.contrib import admin
from django.urls import path, include
from signup import views

urlpatterns = [
    path('', views.signupPage,name='sign up'),
    path('signup', views.signupPage,name='sign up'),
    path('login',views.login,name='login'),
    path('home',views.home),
    path('addResponse',views.addResponse),
]