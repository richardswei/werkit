from rest_framework import serializers
from backend.models import TodoItem, Note


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('id', 'created', 'updated', 'due', 'title', 'description', 'priority')


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'created', 'updated', 'title', 'description')
