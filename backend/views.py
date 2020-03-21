from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from django.contrib.auth.models import User
from . import models
from . import serializers
# from rest_framework import permissions
from backend.permissions import IsOwner


class NoteList(generics.ListCreateAPIView):
    permission_classes = [IsOwner]
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NoteDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer


class TodoItemList(generics.ListCreateAPIView):
    permission_classes = [IsOwner]
    queryset = models.TodoItem.objects.all()
    serializer_class = serializers.TodoItemSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TodoItemDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    queryset = models.TodoItem.objects.all()
    serializer_class = serializers.TodoItemSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
