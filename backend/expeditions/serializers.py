from rest_framework import serializers

from .models import *


class User_RegistrationSerializer(serializers.ModelSerializer):
    repeat_password = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'repeat_password', 'last_name', 'email', 'phone',
                  'subscribe_to_the_newsletter')
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


class MainImgSerializer(serializers.ModelSerializer):
    """вывод главной картинки """

    class Meta:
        model = Img
        fields = ('img', 'first_img')


class ImgListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Img
        fields = ('img',)


# class CommentListSerializer(serializers.ModelSerializer):
#     user = serializers.SlugRelatedField(slug_field='username', read_only=True)
#
#     class Meta:
#         model = Comment
#         fields = '__all__'
#
#
# class CommentSerializer(serializers.ModelSerializer):
#     user = serializers.SlugRelatedField(slug_field='username', read_only=True)
#
#     class Meta:
#         model = Comment
#         fields = '__all__'
#
#     def create(self, validated_data):
#         validated_data['user'] = self.context['request'].user
#         return Comment.objects.create(**validated_data)
