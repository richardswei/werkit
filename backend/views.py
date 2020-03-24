from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from . import models
from . import serializers
# from rest_framework import permissions
from backend.permissions import IsOwner
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token


class NoteList(generics.ListCreateAPIView):
    permission_classes = [IsOwner, IsAuthenticated]
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NoteDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner, IsAuthenticated]
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer


class TodoItemList(generics.ListCreateAPIView):
    permission_classes = [IsOwner, IsAuthenticated]
    queryset = models.TodoItem.objects.all()
    serializer_class = serializers.TodoItemSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TodoItemDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner, IsAuthenticated]
    queryset = models.TodoItem.objects.all()
    serializer_class = serializers.TodoItemSerializer


class UserList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    # permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = [IsOwner, IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class Ping(generics.RetrieveAPIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return Response({'success': 'true'})


class Registration(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.UserSerializer


class Authentication(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = Token.objects.get_or_create(user=user)
        print(token)
        return Response({
            "user": serializers.UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token[0].key
        })


# @login_required()
# def secret_page(request, *args, **kwargs):
#     return HttpResponse('Secret contents!', status=200)
