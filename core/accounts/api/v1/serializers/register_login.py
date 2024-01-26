from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from core.accounts.models import User
from django.core import exceptions


class RegisterLoginSerializer(serializers.Serializer):
    password1 = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = "__all__"

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password1'):
            raise serializers.ValidationError("your password not mach")

        try:
            validate_password(attrs.get('password'))

        except exceptions.ValidationError as e:
            raise serializers.ValidationError(list(e.message))

    def create(self, validated_data):
        validated_data.pop('password1')
        return User.objects.create(**validated_data)



class ResendActivationEmailSSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')

        try:
            user = get_object_or_404(User, email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({'detail': 'email does not exist'})

        if user.is_active:
            raise serializers.ValidationError({'detail': 'you are already activated'})

        attrs['user'] = user



