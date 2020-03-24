"""werkit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
# from rest_framework import routers
from rest_framework.authtoken import views as auth_views
from backend import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/ping/', views.Ping.as_view(), name="ping"),
    path('api/v1/auth-ping/', views.AuthPing.as_view(), name="auth_ping"),
    path('api/v1/registration/', views.Registration.as_view(), name="registration"),
    path('api/v1/signin/', views.Signin.as_view(), name="signin"),
    path('api/v1/signout/', views.Signout.as_view(), name="signout"),

    path('api/v1/users/', views.UserList.as_view(), name="user_list"),
    path('api/v1/users/<int:pk>/', views.UserDetail.as_view(), name="user_profile"),
    path('api/v1/notes/', views.NoteList.as_view(), name="notes"),
    path('api/v1/notes/<int:pk>/', views.NoteDetails.as_view(), name="notes_details"),
    path('api/v1/todoitems/', views.TodoItemList.as_view(), name="todo_items"),
    path('api/v1/todoitems/<int:pk>/', views.TodoItemDetails.as_view(), name="todo_items_details"),
]
