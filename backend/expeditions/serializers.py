from rest_framework import serializers

from .models import *


class User_RegistrationSerializer(serializers.ModelSerializer):
    repeat_password = serializers.CharField(max_length=100,  write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'repeat_password', 'last_name', 'email', 'phone',
                  'subscribe_to_the_newsletter', 'user_photo')
        extra_kwargs = {'password': {'write_only': True}}


    def validate(self, attrs):
        password, repeat_password = attrs.get('password', None), attrs.pop('repeat_password', None)

        if password is None or repeat_password is None:
            raise serializers.ValidationError("Вы забыли заполнить пароль")
        if password != repeat_password:
            raise serializers.ValidationError("Пароль не совпадает")

        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)