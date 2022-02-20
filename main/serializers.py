from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from rest_framework import serializers

from django.contrib.auth.models import User


class RegisterValidateSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=2, max_length=10)

    def validate_username(self, username):
        users = User.objects.filter(username=username)
        if users.count()>0:
            raise ValidationError('User with this name already exists!')
