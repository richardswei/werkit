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
from django.urls import include, path
# from rest_framework import routers
from backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/notes/', views.NoteList.as_view(), name="notes"),
    path('api/v1/notes/<int:pk>/', views.NoteDetails.as_view(), name="notes_details"),
    path('api/v1/todoitems/', views.TodoItemList.as_view(), name="todo_items"),
    path('api/v1/todoitems/<int:pk>/', views.TodoItemDetails.as_view(), name="todo_items_details"),
    path('api/v1/users/', views.UserList.as_view()),
    path('api/v1/users/<int:pk>/', views.UserDetail.as_view()),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
