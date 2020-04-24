
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm

from . import views

urlpatterns = [
    path('home',views.home,name="home"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup',views.signup_view,name="register"),
    path('logout',views.logout,name="logout"),
    path('user-profile/<str:usp_id>', views.ShowUserPage, name='userProfile'),
    path('posts',views.posts,name="posts")
]
