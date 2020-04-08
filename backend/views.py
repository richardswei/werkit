from . import serializers
from . import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from backend.permissions import IsOwner


class Ping(generics.RetrieveAPIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return Response({'success': 'true'})


class AuthPing(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({'authenticated': 'true'})


class Registration(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.UserSerializer


class Signin(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = Token.objects.get_or_create(user=user)
        return Response({
            "user": serializers.UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token[0].key
        })


class Signout(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.LoginUserSerializer

    def delete(self, request, *args, **kwargs):
        request.auth.delete()
        return Response({
            "signed_out": "true"
        })


class NoteList(generics.ListCreateAPIView):
    permission_classes = [IsOwner, IsAuthenticated]
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return models.Note.objects.filter(owner=user)


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

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return models.TodoItem.objects.filter(owner=user)


class TodoItemDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner, IsAuthenticated]
    queryset = models.TodoItem.objects.all()
    serializer_class = serializers.TodoItemSerializer


class UserList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = [IsOwner, IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
