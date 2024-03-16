from rest_framework import serializers
from .models import *
from expeditions.serializers import MainImgListSerializer


class EventSerializer(serializers.ModelSerializer):
    imgs = MainImgListSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'
