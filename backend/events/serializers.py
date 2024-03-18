from rest_framework import serializers
from .models import *
from expeditions.serializers import MainImgSerializer, CommentListSerializer, ImgListSerializer


class EventListSerializer(serializers.ModelSerializer):
    imgs = MainImgSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    imgs = ImgListSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'


class CommentEventSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    event = serializers.SlugRelatedField(slug_field='slug', read_only=True)
    class Meta:
        model = CommentEvent
        fields = '__all__'

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user

        validated_data['event'] = Event.objects.get(slug=(self.context['request'].META['HTTP_REFERER'].split('/'))[-2])
        return CommentEvent.objects.create(**validated_data)
