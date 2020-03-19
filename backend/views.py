from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from . import models
from . import serializers


class NoteList(generics.ListCreateAPIView):
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer


class NoteDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer


class TodoItemList(generics.ListCreateAPIView):
    queryset = models.TodoItem.objects.all()
    serializer_class = serializers.TodoItemSerializer


class TodoItemDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TodoItem.objects.all()
    serializer_class = serializers.TodoItemSerializer
