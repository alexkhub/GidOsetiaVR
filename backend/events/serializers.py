from rest_framework import serializers
from .models import *
from expeditions.serializers import MainImgSerializer,  CommentListSerializer ,  ImgListSerializer


class EventListSerializer(serializers.ModelSerializer):
    imgs = MainImgSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        exclude = ('comments',)


class EventSerializer(serializers.ModelSerializer):
    comments = CommentListSerializer(many=True, read_only=True)
    imgs = ImgListSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'