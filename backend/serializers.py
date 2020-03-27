from rest_framework import serializers
from backend.models import TodoItem, Note
from django.contrib.auth import authenticate, get_user_model


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('id', 'created', 'updated', 'due', 'title', 'description', 'priority', 'user_id')

    user_id = serializers.ReadOnlyField(source='owner.id')


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'created', 'updated', 'title', 'description', 'user_id')

    user_id = serializers.ReadOnlyField(source='owner.id')


class UserSerializer(serializers.ModelSerializer):
    # notes = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all(), allow_null=True)
    # todoitems = serializers.PrimaryKeyRelatedField(many=True, queryset=TodoItem.objects.all(), allow_null=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        write_only_fields = ['password']
        read_only_fields = ['id']

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")
